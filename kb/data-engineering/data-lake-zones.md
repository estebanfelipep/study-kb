# Data lake zones

This file covers how a data lake is split into zones (layers): the three core zones, the extra zones to consider, and what each one is for.

## Sources

- [Data lake foundation](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/data-lake-foundation.html): AWS whitepaper (Storage Best Practices for Data and Analytics Applications), the zones of a data lake.

## Why zones

A zones (layers) strategy helps with **data organization**, **data integrity** and **access control**. The common approach has three zones that line up with the stages of the pipeline: data moves from one zone to the next as it's processed.

**Zones are how stage 2 (store) is organized.** Each zone is a part of the lake where data sits. The other stages move data between them: stage 1 (ingest) writes into raw, stage 4 (process) turns raw into cleaned and cleaned into curated, and stage 5 (deliver) reads from curated. The stages are in [modern-data-architecture.md](modern-data-architecture.md).

```
 1. Ingest     2. Store (the zones)                     5. Deliver
 sources ─► raw ─────────► cleaned ─────────► curated ─► analytics, ML
            as ingested    filtered,          merged, joined,
            original       standardized,      aggregated,
            format         corrected          quality-assured
               └─ 4. Process ─┘  └─ 4. Process ──┘
```

## The three core zones

| Zone | What it holds | Why | Stage that writes it |
| --- | --- | --- | --- |
| **Raw** | Data as it's ingested from the sources, in its **original format** | **Data integrity:** the original is kept for future auditing or reprocessing. Turn on versioning | 1. Ingest |
| **Cleaned** | Processed or transformed data: **anomalies filtered, formats standardized, invalid values corrected** | A trustworthy, uniform version of each source | 4. Process |
| **Curated** | Data **merged, joined or aggregated** with other datasets and **quality-assured**, in a **consumption-ready format** | Made available for specific analytics and machine learning use cases | 4. Process (read by 5. Deliver) |

A rule of thumb: cleaned still has **one dataset per source**, fixed but not combined. Curated is where sources are **combined** for a use case.

## Extra zones to consider

| Zone | What it's for | Stage it serves |
| --- | --- | --- |
| **Landing** | A first stop for **sensitive data**, such as PII. The data is **masked before it moves into the raw zone** | 1. Ingest, plus security |
| **Logs** | Logs of the lake's storage and the other services in the architecture, such as storage access logs, monitoring logs and audit trails | Monitoring, across all stages |
| **Archived** | Infrequently accessed, historical or compliance-related data | 2. Store (long-term) |
| **Sandbox** | Exploratory analysis and experimentation | 5. Deliver (data scientists, analysts) |

With a landing zone, the flow starts one step earlier:

```
 sources ─► landing ─► raw ─► cleaned ─► curated
            (mask PII)
```

## Related

- [modern-data-architecture.md](modern-data-architecture.md): the zones organize stage 2 (store). Stage 1 (ingest) writes into raw, stage 4 (process) moves data from raw to cleaned to curated, and stage 5 (deliver) reads curated.
- [store-on-aws.md](../aws/aws-data-engineering/aws-data-pipeline/store-on-aws.md): on AWS, stage 2 is S3, so the zones are S3 buckets or prefixes, and the process-stage services (Glue, EMR) move data between them.
- [data-lakes-and-warehouses.md](data-lakes-and-warehouses.md): defines the data lake these zones divide; the curated zone is the part a warehouse usually serves.
- [replicating-databases-to-the-lake.md](replicating-databases-to-the-lake.md): a database copy lands in the raw zone as load and change files, and the merge into one current row per key writes to the cleaned zone.
- [unified-customer-data.md](unified-customer-data.md): a worked example through all three zones: CRM changes land in raw, each source is standardized into cleaned, and the matched, merged `customer_360` is curated.
- [data-security-and-monitoring.md](data-security-and-monitoring.md): zones are also access boundaries, and the landing zone is where PII is masked before anyone downstream sees it.
- [s3.md](../aws/aws-services/aws-general-services/s3.md): on AWS each zone is commonly its own S3 bucket, with a storage class and lifecycle rules chosen per zone.
- [example-corp-store-on-aws.md](../aws/aws-data-engineering/aws-data-pipeline/example-corp-store-on-aws.md): an AWS example with one S3 bucket per zone, and a storage class and lifecycle rules chosen for each.
