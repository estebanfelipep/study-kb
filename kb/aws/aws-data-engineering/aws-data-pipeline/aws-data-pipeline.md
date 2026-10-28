# aws-data-pipeline — index

This folder maps the five stages of a modern data architecture to AWS services, one file per stage, plus the data engineer's functions and the personas.

The vendor-neutral stages are in [modern-data-architecture.md](../../../data-engineering/modern-data-architecture.md).

## How to read this folder

- **Before:** [modern-data-architecture.md](../../../data-engineering/modern-data-architecture.md), which defines each stage.
- **Order:** the stages in pipeline order, 1 to 5, each followed by its Example Corp worked example where there is one, then the functions and personas, which cut across the stages.
- **After:** the `choosing-*` files in [aws-data-engineering](../aws-data-engineering.md), to pick between the services of a stage.

## The flow

```
Sources: databases, files, logs, IoT, SaaS, streams
   │
   ▼
1. Ingest    DMS, Data Firehose, MSK, IoT Core, DataSync,
             Transfer Family, Snow Family
   │
   ▼
2. Store     S3 data lake (raw, cleaned, curated zones)
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

Specialized services bring each type of source into the lake: DMS for databases, Firehose and MSK for streams, IoT Core for devices, DataSync, Transfer Family and Snow Family for files and bulk data.

- [ingest-on-aws.md](ingest-on-aws.md): the ingest services and what each one ingests. Read when: you need which AWS service brings a type of source into the lake.
- [example-corp-ingest-on-aws.md](example-corp-ingest-on-aws.md): Example Corp ingests an on-premises MySQL table and an Aurora table with DMS, and NAS files with DataSync, into the raw bucket over a Site-to-Site VPN. Read when: you need a worked example of setting up DMS endpoints and tasks, a DataSync agent and task, or securing on-premises ingestion.

## 2. Store

S3 is the data lake, built first, with one bucket per zone. Other "lake" services build and govern a lake on S3, or are purpose-built lakes for one kind of data.

- [store-on-aws.md](store-on-aws.md): S3 as the data lake, zones as buckets, and the AWS "lake" services (Lake Formation, S3 Tables, SageMaker Lakehouse, Security Lake, CloudTrail Lake, HealthLake). Read when: you need where lake data lives on AWS, or what a service with "lake" in its name does.
- [example-corp-store-on-aws.md](example-corp-store-on-aws.md): Example Corp's three zone buckets, S3 Standard plus lifecycle rules on raw and cleaned, Intelligent-Tiering on curated, and why archived data can't be queried directly. Read when: you need a worked example of choosing storage classes and lifecycle rules per zone.

## 3. Catalog

The Glue Data Catalog and Glue crawlers make lake data findable and queryable; DataZone holds the business glossary.

- [catalog-on-aws.md](catalog-on-aws.md): the Glue Data Catalog, crawlers and DataZone in this stage. Read when: you need how lake data becomes discoverable and queryable on AWS.

## 4. Process

Glue (managed ETL), EMR (open-source frameworks) and Managed Service for Apache Flink (real time) transform the data, moving it between the lake's zones.

- [process-on-aws.md](process-on-aws.md): the processing services, their modes, and how they move data from raw to cleaned to curated. Read when: you need which AWS service transforms data, batch or real time.

## 5. Deliver

Redshift, Athena, EMR, OpenSearch, QuickSight and SageMaker serve the data to consumers, alongside AWS's purpose-built databases.

- [deliver-on-aws.md](deliver-on-aws.md): the delivery services by consumer, the purpose-built databases by type, and how earlier stages pay off here. Read when: you need how consumers query or see the data on AWS, or which database fits a data type.

## Security and governance, across the stages

| Service | Security or governance? | Stages |
| --- | --- | --- |
| [lake-formation.md](../../aws-services/aws-analytics/lake-formation.md) | Both | Store, catalog, deliver |
| [iam.md](../../aws-services/aws-identity/iam.md) | Security | All |
| [kms.md](../../aws-services/aws-security/kms.md) | Security | All |
| [macie.md](../../aws-services/aws-security/macie.md) | Security (and governance input) | Store |
| [datazone.md](../../aws-services/aws-analytics/datazone.md) | Governance | Catalog, deliver |
| [audit-manager.md](../../aws-services/aws-security/audit-manager.md) | Governance (compliance) | All |

The full security and monitoring picture is in [security-and-monitoring-on-aws.md](../security-and-monitoring-on-aws.md).

## Functions and personas

- [functions-and-personas-on-aws.md](functions-and-personas-on-aws.md): the six data engineer functions and the personas mapped to AWS services; Glue appears in five of the six functions. Read when: you need which AWS services a function or persona uses.

## Related

- [data-lake-zones.md](../../../data-engineering/data-lake-zones.md): the zones that organize stage 2. On AWS they're S3 buckets, and the stage 4 services move data between them.
- [unified-customer-data-on-aws.md](../unified-customer-data-on-aws.md): applies this stage-to-service map to one project. Each row of its table names the pipeline stage, so a service there can be traced back to its stage file here.
