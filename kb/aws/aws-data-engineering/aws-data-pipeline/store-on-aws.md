# Store on AWS

This file covers stage 2 of the data pipeline on AWS: S3 as the data lake, its zones as buckets, and the other AWS "lake" services.

## The data lake on S3

[s3.md](../../aws-services/aws-general-services/s3.md) is the foundation of the data lake: virtually unlimited scale, high durability, pay for what you use. You **build** it first, and processed data is usually written back to it after stage 4.

The lake's zones (raw, cleaned, curated, and optional landing, logs, archived and sandbox) are commonly one S3 bucket each, with a storage class and lifecycle rules per zone. The zones are defined in [data-lake-zones.md](../../../data-engineering/data-lake-zones.md), and the S3 setup, with the Example Corp example, is in [s3.md](../../aws-services/aws-general-services/s3.md).

## AWS "lake" services

**S3 is the data lake storage layer.** Other "lake" services either build and govern a lake on S3, or are purpose-built lakes for one kind of data.

**Build, manage or govern a lake on S3** (data stays in your S3 buckets):

| Service | What it adds |
| --- | --- |
| [Lake Formation](../../aws-services/aws-analytics/lake-formation.md) | Builds and governs a lake on S3: central, fine-grained permissions (table, column, row) |
| [Glue Data Catalog](../../aws-services/aws-analytics/glue.md) | The metadata layer, so files in S3 look like queryable tables |
| **S3 Tables** ([s3.md](../../aws-services/aws-general-services/s3.md)) | S3 buckets built for tabular data in **Apache Iceberg** format, with automatic maintenance |
| [SageMaker Lakehouse](../../aws-services/aws-ai/sagemaker.md) | Unifies S3 lakes and Redshift warehouses under one catalog and one set of permissions |

**Purpose-built lakes for one kind of data:**

| Service | What it stores | Storage underneath |
| --- | --- | --- |
| **Amazon Security Lake** | Security logs from AWS, on-premises and SaaS sources, normalized to OCSF | **Your S3 buckets** |
| **AWS CloudTrail Lake** ([cloudtrail.md](../../aws-services/aws-monitoring/cloudtrail.md)) | CloudTrail audit events, queryable with SQL | AWS-managed |
| **AWS HealthLake** | Healthcare data in the FHIR standard | AWS-managed |

**Not lakes, but often mistaken for them:** Athena, EMR, Glue jobs and Redshift Spectrum are **engines** that read the lake. Redshift is a **warehouse**. RDS is a **source**.

## Related

- [modern-data-architecture.md](../../../data-engineering/modern-data-architecture.md): its "2. Store" section lists what lake storage needs; S3 is how AWS meets those needs.
- [data-lake-zones.md](../../../data-engineering/data-lake-zones.md): the zones that organize this stage; on AWS each is usually an S3 bucket.
- [choosing-storage-and-processing-services.md](../choosing-storage-and-processing-services.md): compares S3 with Redshift (lake vs warehouse) and RDS (why a database isn't a lake).
- [ingest-on-aws.md](ingest-on-aws.md): the previous stage; its services write into this lake.
- [catalog-on-aws.md](catalog-on-aws.md): the next stage; crawlers catalog what lands here.
