# Deliver on AWS

This file covers stage 5 of the data pipeline on AWS: the services consumers use to query and see the data, and AWS's purpose-built databases.

## Services

| Service | Typical consumer |
| --- | --- |
| [redshift.md](../../aws-services/aws-analytics/redshift.md) | Analysts, BI |
| [athena.md](../../aws-services/aws-analytics/athena.md) | Analysts, engineers (ad hoc) |
| [emr.md](../../aws-services/aws-analytics/emr.md) | Data scientists, engineers |
| Purpose-built databases (below) | Applications, specialized analytics |
| [opensearch-service.md](../../aws-services/aws-databases/opensearch-service.md) | Engineers, ops (search, logs) |
| [quicksight.md](../../aws-services/aws-analytics/quicksight.md) | Business analysts, executives |
| Machine learning: [sagemaker.md](../../aws-services/aws-ai/sagemaker.md) (the course doesn't name the service) | Data scientists |

## Purpose-built databases

AWS offers **more than 14** databases to store, query and analyze large datasets. What each type is for is in [modern-data-architecture.md](../../../data-engineering/modern-data-architecture.md). Example AWS service per type:

| Type | AWS service |
| --- | --- |
| Relational | [RDS, Aurora](../../aws-services/aws-databases/rds.md) |
| Key-value | [DynamoDB](../../aws-services/aws-databases/dynamodb.md) |
| Document | DocumentDB (MongoDB-compatible) |
| In-memory | ElastiCache, MemoryDB |
| Graph | Neptune |
| Time series | Timestream |
| Wide column | Keyspaces (Apache Cassandra-compatible) |
| Ledger | QLDB, which is discontinued; AWS points to Aurora PostgreSQL instead |

## How earlier stages pay off here

- **Ingest:** Parquet/ORC conversion in Firehose means Athena and Spectrum scan less and cost less.
- **Catalog:** Athena, EMR and Redshift Spectrum read table definitions from the Glue Data Catalog.

## Related

- [modern-data-architecture.md](../../../data-engineering/modern-data-architecture.md): its "5. Deliver" section lists the ways to deliver and the purpose-built database types; this file names the AWS services.
- [choosing-delivery-services.md](../choosing-delivery-services.md): pick-rules between these services, such as Athena vs Redshift vs Spectrum.
- [process-on-aws.md](process-on-aws.md): the previous stage; it writes the curated data these services serve.
