# Example Corp: the store stage on AWS

This file follows Example Corp through stage 2 of its pipeline: the data lake as three S3 buckets, one per zone, with the storage classes and lifecycle rules chosen per zone to comply with industry regulations and optimize costs.

## Three buckets, one per zone

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

## Raw and cleaned: S3 Standard, then lifecycle rules

**S3 Standard** suits the high-transaction workload while the data is active. **Once data is curated, its raw and cleaned copies are rarely accessed**, so lifecycle rules archive them:

1. After **1 year**, move all files to **S3 Standard-IA**.
2. After **2 years in Standard-IA**, move them to **S3 Glacier Deep Archive**.
3. After **7 years in Deep Archive**, **expire** (delete) the data.

```
 Standard ─1 yr─► Standard-IA ─+2 yrs─► Deep Archive ─+7 yrs─► gone
 (created)         (year 1)             (year 3)              (yr 10)
```

When configured, rules count days since the object was created, so these are day 365, day 1,095 and expiry at day 3,650.

## Curated: S3 Intelligent-Tiering instead of rules

Many consumers and use cases read the curated bucket, each with its own access pattern, so no single age-based rule fits. **Intelligent-Tiering** moves each object to the most cost-effective tier as it cools, so there are no rules to manage.

## Archived data can't be queried directly

S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive **can't be queried directly with analytics tools**. From year 3, when the lifecycle rules move it to Deep Archive, Example Corp's raw and cleaned data is out of reach of direct queries.

## Related

- [store-on-aws.md](store-on-aws.md): the stage this example works through. S3 is the lake, with one bucket per zone.
- [example-corp-ingest-on-aws.md](example-corp-ingest-on-aws.md): the previous stage of the same example. DMS and DataSync write the three sources into the raw bucket set up here.
- [data-lake-zones.md](../../../data-engineering/data-lake-zones.md): defines the raw, cleaned and curated zones these three buckets implement.
- [s3.md](../../aws-services/aws-general-services/s3.md): the storage classes, lifecycle rules and Intelligent-Tiering this example chooses between, and the minimum storage durations to watch for.
- [replicating-databases-to-the-lake.md](../../../data-engineering/replicating-databases-to-the-lake.md): expiring the raw files in year 10 also deletes the change history the DMS files keep there.
