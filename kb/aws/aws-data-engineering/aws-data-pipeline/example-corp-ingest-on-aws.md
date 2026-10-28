# Example Corp: the ingest stage on AWS

This file follows Example Corp through stage 1 of its pipeline as it ingests three sources into the S3 data lake: two databases with DMS and files from an on-premises NAS with DataSync, all secured in transit with a Site-to-Site VPN.

## The starting point

Example Corp has already built its data lake: three S3 buckets, one per zone (raw, cleaned and curated). Every source in this stage lands in the **raw** bucket. The buckets and their storage setup are the next stage, in [example-corp-store-on-aws.md](example-corp-store-on-aws.md).

## The three sources

| Source | Where it lives | Data | Service | Lands in the raw bucket as | How it stays current |
| --- | --- | --- | --- | --- | --- |
| MySQL database | On premises | Marketing campaigns table | [DMS](../../aws-services/aws-databases/dms.md) | Marketing campaigns data (own target endpoint) | Full load, then CDC |
| Aurora database | AWS | Sales table | [DMS](../../aws-services/aws-databases/dms.md) | Sales data (own target endpoint) | Full load, then CDC |
| NAS | On premises | `website_clicks` folder | [DataSync](../../aws-services/aws-migration-and-transfer/datasync.md) | `website_clicks/` prefix | Incremental copy every hour |

## The whole picture

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

## Step by step

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

## Why each service

- **The two databases use DMS,** because they're tables whose rows keep changing: DMS copies them once, then follows their changes from the transaction log. Whether a source is on premises (MySQL) or already on AWS (Aurora) doesn't change the service.
- **The NAS uses DataSync,** because `website_clicks` is a folder of files, not a database. The pick-rules are in [choosing-ingestion-services.md](../choosing-ingestion-services.md), "DMS vs DataSync".

## Related

- [ingest-on-aws.md](ingest-on-aws.md): the stage this example works through. DMS and DataSync are two of its services, applied here to real sources.
- [example-corp-store-on-aws.md](example-corp-store-on-aws.md): the next stage of the same example. It sets up the raw bucket these sources land in, and the cleaned and curated buckets after it.
- [data-lake-zones.md](../../../data-engineering/data-lake-zones.md): every source here is ingested into the raw zone, which keeps the data as it arrived.
- [replicating-databases-to-the-lake.md](../../../data-engineering/replicating-databases-to-the-lake.md): the two DMS tasks are the full load + CDC that file describes, so their raw files still need its merge step to become current tables in the cleaned zone.
- [dms.md](../../aws-services/aws-databases/dms.md): the DMS components and task phases this example configures.
- [datasync.md](../../aws-services/aws-migration-and-transfer/datasync.md): the agent, task and schedule this example configures for the NAS.
- [site-to-site-vpn.md](../../aws-services/aws-networking/site-to-site-vpn.md): the encrypted tunnel the on-premises data travels through.
- [choosing-ingestion-services.md](../choosing-ingestion-services.md): why the databases go to DMS and the NAS files to DataSync.
