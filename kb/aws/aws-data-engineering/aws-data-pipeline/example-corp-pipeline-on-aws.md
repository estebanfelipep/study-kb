# Example Corp: a data pipeline on AWS

This file follows Example Corp through the stages of its data pipeline on AWS, one section per stage: ingesting two databases and a NAS folder with DMS, DataSync and a Site-to-Site VPN, storing them in three zone buckets with storage classes and lifecycle rules per zone, and cataloging the raw zone with Glue crawlers.

## The whole pipeline

```
 ON PREMISES                AWS
 MySQL (marketing) ══VPN══► 1. Ingest   DMS (two tasks)
 NAS (website_clicks) ═VPN═►            DataSync (hourly)
                            Aurora (sales) ─► DMS
                                 │
                                 ▼
                            2. Store    S3 raw ─► cleaned ─► curated
                                 │
                                 ▼
                            3. Catalog  Glue crawlers ─► db_raw
```

Example Corp **builds the lake first**: the three buckets of section 2 exist before anything is ingested. The sections follow the pipeline's stage order.

## 1. Ingest

Example Corp ingests three sources into the S3 data lake: two databases with DMS and files from an on-premises NAS with DataSync, all secured in transit with a Site-to-Site VPN. Every source lands in the **raw** bucket.

### The three sources

| Source | Where it lives | Data | Service | Lands in the raw bucket as | How it stays current |
| --- | --- | --- | --- | --- | --- |
| MySQL database | On premises | Marketing campaigns table | [DMS](../../aws-services/aws-databases/dms.md) | A marketing campaigns folder (own target endpoint) | Full load, then CDC |
| Aurora database | AWS | Sales table | [DMS](../../aws-services/aws-databases/dms.md) | A sales folder (own target endpoint) | Full load, then CDC |
| NAS | On premises | `website_clicks` folder | [DataSync](../../aws-services/aws-migration-and-transfer/datasync.md) | `website_clicks/` prefix | Incremental copy every hour |

### How the sources reach the raw bucket

```
 ON PREMISES              AWS
 MySQL         ══VPN══► DMS task 1 ───────────┐
 (marketing)                                  │
                        Aurora ─► DMS task 2 ─┼──► S3 raw bucket
                        (sales)               │
 NAS           ══VPN══► DataSync, hourly ─────┘
 (website_clicks,
  DataSync agent)

 Both DMS tasks run on one replication instance.
```

### Step by step

**Databases, with DMS**

1. **Create a replication instance,** the compute that runs the replication tasks.
2. **Create two source endpoints:** the marketing campaigns table in the on-premises MySQL database, and the sales table in Aurora.
3. **Create two target endpoints,** both pointing at the raw bucket: one for the marketing campaigns data, one for the sales data.
4. **Create one migration task per source,** each paired with its target. Each task starts with a **full load** of the existing data, then switches to **ongoing replication (CDC)** to keep source and target in sync. The phases are in [dms.md](../../aws-services/aws-databases/dms.md).

**Files, with DataSync**

5. **Deploy a DataSync agent on premises** and register it with the DataSync service.
6. **Configure a DataSync task:**
   - Source location: the NAS folder holding the `website_clicks` data.
   - Destination location: the S3 raw bucket, prefix `website_clicks`.
   - Schedule: an incremental load every hour.

**Security in transit**

7. **Set up a Site-to-Site VPN** between the data center and AWS: a virtual private gateway on the AWS side and a customer gateway on premises. Data from the on-premises MySQL database and the NAS travels through an encrypted tunnel ([site-to-site-vpn.md](../../aws-services/aws-networking/site-to-site-vpn.md)).

### Why each service

- **The two databases use DMS,** because they're tables whose rows keep changing: DMS copies them once, then follows their changes from the transaction log. Whether a source is on premises (MySQL) or already on AWS (Aurora) doesn't change the service.
- **The NAS uses DataSync,** because `website_clicks` is a folder of files, not a database. The pick-rules are in [choosing-ingestion-services.md](../choosing-ingestion-services.md), "DMS vs DataSync".

## 2. Store

The data lake is three S3 buckets, one per zone, with the storage classes and lifecycle rules chosen per zone to comply with industry regulations and optimize costs.

### Three buckets, one per zone

```
   1. Ingest       4. Process        4. Process       5. Deliver
 ───────────► raw ───────────► cleaned ──────────► curated ────────►
              bucket           bucket              bucket
```

| Zone | What it holds at Example Corp | Storage class | Then |
| --- | --- | --- | --- |
| **Raw** | The marketing, sales and `website_clicks` data as ingested, in its original format, kept for future auditing or reprocessing | S3 Standard | Lifecycle rules |
| **Cleaned** | The processed data: anomalies filtered, formats standardized, invalid values corrected | S3 Standard | Lifecycle rules |
| **Curated** | The processed data merged or joined with other datasets, for specific analytics and ML use cases | S3 Intelligent-Tiering | No lifecycle rules |

The zones themselves are defined in [data-lake-zones.md](../../../data-engineering/data-lake-zones.md).

### Raw and cleaned: S3 Standard, then lifecycle rules

**S3 Standard** suits the high-transaction workload while the data is active. **Once data is curated, its raw and cleaned copies are rarely accessed**, so lifecycle rules archive them:

1. After **1 year**, move all files to **S3 Standard-IA**.
2. After **2 years in Standard-IA**, move them to **S3 Glacier Deep Archive**.
3. After **7 years in Deep Archive**, **expire** (delete) the data.

```
 Standard ─1 yr─► Standard-IA ─+2 yrs─► Deep Archive ─+7 yrs─► gone
 (created)         (year 1)             (year 3)              (yr 10)
```

When configured, rules count days since the object was created, so these are day 365, day 1,095 and expiry at day 3,650.

### Curated: S3 Intelligent-Tiering instead of rules

Many consumers and use cases read the curated bucket, each with its own access pattern, so no single age-based rule fits. **Intelligent-Tiering** moves each object to the most cost-effective tier as it cools, so there are no rules to manage.

### Archived data can't be queried directly

S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive **can't be queried directly with analytics tools**. From year 3, when the lifecycle rules move it to Deep Archive, Example Corp's raw and cleaned data is out of reach of direct queries.

## 3. Catalog

With its databases and files in the raw zone, and ongoing replication keeping the lake in sync with the data center, Example Corp wants to:

- access its data as tables, in a SQL-like way,
- keep its quality consistent,
- have clear data ownership and access rules.

The solution is to catalog all incoming data in the Glue Data Catalog, with one Glue crawler per raw-zone folder writing to the database `db_raw`.

### From folders to tables

```
 S3 raw bucket          Glue crawlers         Data Catalog: db_raw
 sales folder ────────► crawler 1 ──────────► db_raw.sales
 marketing campaigns ─► crawler 2 ──────────► db_raw.marketing_
   folder                                       campaigns
 website_clicks/ ─────► crawler 3 ──────────► db_raw.website_clicks

 Each crawler has its own schedule and an IAM role with access
 to the data lake.
```

### Step by step

1. **Create a Glue database** named `db_raw`, before the crawlers.
2. **Create three crawlers,** one for each folder in the raw bucket:

   | Crawler | Data source | Target | IAM role | Schedule |
   | --- | --- | --- | --- | --- |
   | 1 | The raw bucket's sales folder | `db_raw` | Role with access to the data lake | Its own |
   | 2 | The raw bucket's marketing campaigns folder | `db_raw` | Same | Its own |
   | 3 | The raw bucket's `website_clicks` folder | `db_raw` | Same | Its own |

3. **Let the schedules run them.** Each crawler infers the initial schema and partition structure of its folder and writes the metadata to its table: `db_raw.sales`, `db_raw.marketing_campaigns` and `db_raw.website_clicks`.

### What it unlocks

Once cataloged, the raw data is ready to be queried and transformed consistently by purpose-built AWS data services. [Athena](../../aws-services/aws-analytics/athena.md) relies on the catalog for the tables, columns and data types it queries, and [EMR](../../aws-services/aws-analytics/emr.md) reads it for the structure and location of the data it processes. The tables hold only metadata: queries read the files in the raw bucket directly ([glue.md](../../aws-services/aws-analytics/glue.md), "How a query uses a table").

## Related

- [ingest-on-aws.md](ingest-on-aws.md): the stage section 1 works through. DMS and DataSync are two of its services, applied here to real sources.
- [store-on-aws.md](store-on-aws.md): the stage section 2 works through. S3 is the lake, with one bucket per zone.
- [catalog-on-aws.md](catalog-on-aws.md): the stage section 3 works through. The Glue Data Catalog and crawlers make the lake's data findable and queryable.
- [data-lake-zones.md](../../../data-engineering/data-lake-zones.md): defines the raw, cleaned and curated zones the three buckets implement. Every source is ingested into raw, and the crawlers catalog raw.
- [replicating-databases-to-the-lake.md](../../../data-engineering/replicating-databases-to-the-lake.md): the two DMS tasks are the full load + CDC that file describes, so their raw files still need its merge step to become current tables in the cleaned zone. Expiring the raw files in year 10 also deletes the change history they keep.
- [dms.md](../../aws-services/aws-databases/dms.md): the DMS components and task phases section 1 configures.
- [datasync.md](../../aws-services/aws-migration-and-transfer/datasync.md): the agent, task and schedule section 1 configures for the NAS.
- [site-to-site-vpn.md](../../aws-services/aws-networking/site-to-site-vpn.md): the encrypted tunnel the on-premises data travels through.
- [choosing-ingestion-services.md](../choosing-ingestion-services.md): why the databases go to DMS and the NAS files to DataSync.
- [s3.md](../../aws-services/aws-general-services/s3.md): the storage classes, lifecycle rules and Intelligent-Tiering section 2 chooses between, and the minimum storage durations to watch for.
- [glue.md](../../aws-services/aws-analytics/glue.md): the crawler parameters section 3 sets (source, target, IAM role, schedule), what each run does, and what each Data Catalog table holds.
- [iam.md](../../aws-services/aws-identity/iam.md): each crawler runs with an IAM role that grants access to the data lake.
