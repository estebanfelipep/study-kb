# The data pipeline on AWS

This file maps the five stages of a modern data architecture, the data engineer's functions and the personas to the AWS services for each.

The vendor-neutral stages are in [modern-data-architecture.md](../../data-engineering/modern-data-architecture.md).

## The flow

```
Sources: databases, files, logs, IoT, SaaS, streams
   │
   ▼
1. Ingest    DMS, Data Firehose, MSK, IoT Core, DataSync,
             Transfer Family, Snow Family
   │
   ▼
2. Store     S3 data lake
   │
   ▼
3. Catalog   Glue Data Catalog, Glue crawlers
   │
   ▼
4. Process   Glue, EMR, Managed Service for Apache Flink
   │
   ▼
5. Deliver   Redshift, Athena, EMR, OpenSearch, QuickSight,
             SageMaker, purpose-built databases
   │
   ▼
Consumers: analysts, scientists, business users, apps

Across every stage (security and governance):
  Lake Formation, IAM, KMS, Macie, DataZone, Audit Manager
```

You **build** the S3 data lake first, and processed data is usually written back to S3 after stage 4.

## 1. Ingest

Goal: once the data lake is in place, use **specialized AWS services** to ingest different types of data into it.

| Service | What it ingests |
| --- | --- |
| [dms.md](../aws-services/aws-databases/dms.md) | **Relational and non-relational databases** |
| [data-firehose.md](../aws-services/aws-analytics/data-firehose.md) | **Real-time data streams**, with conversion to Parquet or ORC |
| [msk.md](../aws-services/aws-analytics/msk.md) | **Real-time streaming** on Apache Kafka |
| [iot-core.md](../aws-services/aws-iot/iot-core.md) | **IoT devices** |
| [datasync.md](../aws-services/aws-migration-and-transfer/datasync.md) | **On-premises file shares, object storage and Hadoop clusters** |
| [transfer-family.md](../aws-services/aws-migration-and-transfer/transfer-family.md) | **Files over SFTP, FTPS, FTP** (and AS2 _(added)_) into and out of S3 |
| [snow-family.md](../aws-services/aws-migration-and-transfer/snow-family.md) | **Huge or sensitive data**, on physical devices |

[kinesis-data-streams.md](../aws-services/aws-analytics/kinesis-data-streams.md) is the real-time stream these services and consumers often sit around. Which service fits which source is in [choosing-ingestion-services.md](choosing-ingestion-services.md).

## 2. Store

[s3.md](../aws-services/aws-general-services/s3.md) is the foundation of the data lake: virtually unlimited scale, high durability, pay for what you use.

### AWS "lake" services _(added)_

**S3 is the data lake storage layer.** Other "lake" services either build and govern a lake on S3, or are purpose-built lakes for one kind of data.

**Build, manage or govern a lake on S3** (data stays in your S3 buckets):

| Service | What it adds |
| --- | --- |
| [Lake Formation](../aws-services/aws-analytics/lake-formation.md) | Builds and governs a lake on S3: central, fine-grained permissions (table, column, row) |
| [Glue Data Catalog](../aws-services/aws-analytics/glue.md) | The metadata layer, so files in S3 look like queryable tables |
| **S3 Tables** ([s3.md](../aws-services/aws-general-services/s3.md)) | S3 buckets built for tabular data in **Apache Iceberg** format, with automatic maintenance |
| [SageMaker Lakehouse](../aws-services/aws-ai/sagemaker.md) | Unifies S3 lakes and Redshift warehouses under one catalog and one set of permissions |

**Purpose-built lakes for one kind of data:**

| Service | What it stores | Storage underneath |
| --- | --- | --- |
| **Amazon Security Lake** | Security logs from AWS, on-premises and SaaS sources, normalized to OCSF | **Your S3 buckets** |
| **AWS CloudTrail Lake** ([cloudtrail.md](../aws-services/aws-monitoring/cloudtrail.md)) | CloudTrail audit events, queryable with SQL | AWS-managed |
| **AWS HealthLake** | Healthcare data in the FHIR standard | AWS-managed |

**Not lakes, but often mistaken for them:** Athena, EMR, Glue jobs and Redshift Spectrum are **engines** that read the lake. Redshift is a **warehouse**. RDS is a **source**.

## 3. Catalog

- [Glue Data Catalog](../aws-services/aws-analytics/glue.md) creates a **catalog of metadata** about stored assets, searchable by **name, owner, business terms** and other attributes.
- [Glue crawlers](../aws-services/aws-analytics/glue.md) scan data, determine format and schema, group data into tables and write metadata to the Data Catalog. Flow: data lands in S3 → crawlers catalog it → it becomes discoverable and queryable.
- The business glossary lives in [datazone.md](../aws-services/aws-analytics/datazone.md).

## 4. Process

| Service | Mode |
| --- | --- |
| [glue.md](../aws-services/aws-analytics/glue.md): fully managed ETL | Batch (also streaming ETL _(added)_) |
| [emr.md](../aws-services/aws-analytics/emr.md): open-source big data frameworks | Batch |
| [managed-service-for-apache-flink.md](../aws-services/aws-analytics/managed-service-for-apache-flink.md): real-time stream processing | Real time |

Glue appears across the whole flow: jobs for ingestion, crawlers and the Data Catalog, ETL, and workflows for automation. It's the central service of this training _(added)_.

## 5. Deliver

| Service                                                                                                               | Typical consumer _(added)_          |
| --------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| [redshift.md](../aws-services/aws-analytics/redshift.md)                                                              | Analysts, BI                        |
| [athena.md](../aws-services/aws-analytics/athena.md)                                                                  | Analysts, engineers (ad hoc)        |
| [emr.md](../aws-services/aws-analytics/emr.md)                                                                        | Data scientists, engineers          |
| Purpose-built databases (below)                                                                                       | Applications, specialized analytics |
| [opensearch-service.md](../aws-services/aws-databases/opensearch-service.md)                                          | Engineers, ops (search, logs)       |
| [quicksight.md](../aws-services/aws-analytics/quicksight.md)                                                          | Business analysts, executives       |
| Machine learning: [sagemaker.md](../aws-services/aws-ai/sagemaker.md) (the course doesn't name the service _(added)_) | Data scientists                     |

### Purpose-built databases

AWS offers **more than 14** databases to store, query and analyze large datasets. What each type is for is in [modern-data-architecture.md](../../data-engineering/modern-data-architecture.md). Example AWS service per type _(added)_:

| Type | AWS service |
| --- | --- |
| Relational | [RDS, Aurora](../aws-services/aws-databases/rds.md) |
| Key-value | [DynamoDB](../aws-services/aws-databases/dynamodb.md) |
| Document | DocumentDB (MongoDB-compatible) |
| In-memory | ElastiCache, MemoryDB |
| Graph | Neptune |
| Time series | Timestream |
| Wide column | Keyspaces (Apache Cassandra-compatible) |
| Ledger | QLDB, which is discontinued; AWS points to Aurora PostgreSQL instead |

### How earlier stages pay off here _(added)_

- **Ingest:** Parquet/ORC conversion in Firehose means Athena and Spectrum scan less and cost less.
- **Catalog:** Athena, EMR and Redshift Spectrum read table definitions from the Glue Data Catalog.

## Security and governance

| Service | Security or governance? _(added)_ | Stages _(added)_ |
| --- | --- | --- |
| [lake-formation.md](../aws-services/aws-analytics/lake-formation.md) | Both | Store, catalog, deliver |
| [iam.md](../aws-services/aws-identity/iam.md) | Security | All |
| [kms.md](../aws-services/aws-security/kms.md) | Security | All |
| [macie.md](../aws-services/aws-security/macie.md) | Security (and governance input) | Store |
| [datazone.md](../aws-services/aws-analytics/datazone.md) | Governance | Catalog, deliver |
| [audit-manager.md](../aws-services/aws-security/audit-manager.md) | Governance (compliance) | All |

The full security and monitoring picture is in [security-and-monitoring-on-aws.md](security-and-monitoring-on-aws.md).

## Data engineer functions on AWS

The functions are defined in [data-engineer-role.md](../../data-engineering/data-engineer-role.md).

| # | Function | AWS services named |
| --- | --- | --- |
| 1 | Build and manage data infrastructure and platforms | S3, Glue, Redshift |
| 2 | Ingest data from various sources | Glue jobs, Lambda |
| 3 | Prepare ingested data for analytics | Glue, Apache Spark, EMR |
| 4 | Catalog and document curated datasets | Glue crawlers, Glue Data Catalog |
| 5 | Automate regular workflows and pipelines | Glue workflows, Lambda, Step Functions |
| 6 | Ensure data quality, security and compliance | DataZone, Lake Formation |

**Glue appears in five of the six functions.** Apache Spark is the open-source distributed processing engine that runs under Glue and EMR.

Data discovery step 5 ([data-discovery.md](../../data-engineering/data-discovery.md)) names **Glue crawlers or custom scripts** to extract data, and **Glue and EMR** to transform it.

## Personas and services _(added)_

- **Data scientists** → EMR, SageMaker.
- **Analysts** → Athena, Redshift, QuickSight.
- **CDO** → QuickSight dashboards.
- **Data security officer** → PII protection with Macie, fine-grained access and masking with Lake Formation, regulations with Audit Manager.

The personas are defined in [data-personas.md](../../data-engineering/data-personas.md).

## Related

- [unified-customer-data-on-aws.md](unified-customer-data-on-aws.md): applies this stage-to-service map to one project. Each row of its table names the pipeline stage, so a service there can be traced back to its stage section here.
