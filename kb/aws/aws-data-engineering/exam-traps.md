# Exam traps

This file holds the DEA-C01 keyword-to-service table, the older service names exam material may use, and the places where the course text is wrong or loose.

All content here is _(added)_ general knowledge; verify names and availability against current AWS docs.

## Exam keywords: all stages

| Keywords in the question | Service | Stage |
| --- | --- | --- |
| Migrate or replicate a database, change data capture | [DMS](../aws-services/aws-databases/dms.md) | Ingest |
| Streaming delivery to S3/Redshift, no servers, convert to Parquet | [Data Firehose](../aws-services/aws-analytics/data-firehose.md) | Ingest |
| Apache Kafka | [MSK](../aws-services/aws-analytics/msk.md) | Ingest |
| Millions of devices, MQTT | [IoT Core](../aws-services/aws-iot/iot-core.md) | Ingest |
| On-premises NFS/SMB/HDFS, scheduled sync | [DataSync](../aws-services/aws-migration-and-transfer/datasync.md) | Ingest |
| Partners upload via SFTP | [Transfer Family](../aws-services/aws-migration-and-transfer/transfer-family.md) | Ingest |
| Petabytes, limited bandwidth, offline transfer | [Snow Family](../aws-services/aws-migration-and-transfer/snow-family.md) | Ingest |
| Store any data type cheaply at any scale, data lake | [S3](../aws-services/aws-general-services/s3.md) | Store |
| Transactions, ACID, the app's database | [RDS / Aurora](../aws-services/aws-databases/rds.md) | Source |
| Discover schema automatically | [Glue crawler](../aws-services/aws-analytics/glue.md) | Catalog |
| Central metadata repository, make S3 data queryable | [Glue Data Catalog](../aws-services/aws-analytics/glue.md) | Catalog |
| Serverless ETL, least operational overhead | [Glue](../aws-services/aws-analytics/glue.md) | Process |
| Existing Spark/Hadoop, full cluster control | [EMR](../aws-services/aws-analytics/emr.md) | Process |
| Real-time stream analytics | [Managed Service for Apache Flink](../aws-services/aws-analytics/managed-service-for-apache-flink.md) | Process |
| Ad hoc SQL on S3, serverless, pay per query | [Athena](../aws-services/aws-analytics/athena.md) | Deliver |
| Data warehouse, complex queries, petabytes, BI | [Redshift](../aws-services/aws-analytics/redshift.md) | Deliver |
| Full-text search, log analytics | [OpenSearch](../aws-services/aws-databases/opensearch-service.md) | Deliver |
| Dashboards, business users | [QuickSight](../aws-services/aws-analytics/quicksight.md) | Deliver |
| Train a model, predictions | [SageMaker](../aws-services/aws-ai/sagemaker.md) | Deliver |
| Fine-grained (column/row) access to the lake | [Lake Formation](../aws-services/aws-analytics/lake-formation.md) | All |
| Find PII | [Macie](../aws-services/aws-security/macie.md) | All |
| Business catalog, self-service sharing | [DataZone](../aws-services/aws-analytics/datazone.md) | All |
| Prove compliance, audit evidence | [Audit Manager](../aws-services/aws-security/audit-manager.md) | All |
| Collect security logs in one place | Amazon Security Lake | — |
| Near real-time analytics on transactional data without building pipelines | Zero-ETL ([zero-etl-and-serverless-on-aws.md](zero-etl-and-serverless-on-aws.md)) | — |

More pick-rules per stage: [choosing-ingestion-services.md](choosing-ingestion-services.md), [choosing-storage-and-processing-services.md](choosing-storage-and-processing-services.md), [choosing-delivery-services.md](choosing-delivery-services.md), [choosing-orchestration-services.md](choosing-orchestration-services.md), [choosing-security-and-monitoring-services.md](choosing-security-and-monitoring-services.md).

## Names in exam material

| Current name | Name exam material may use |
| --- | --- |
| Amazon Data Firehose | Kinesis Data Firehose |
| Amazon Managed Service for Apache Flink | Kinesis Data Analytics |
| Amazon OpenSearch Service | Amazon Elasticsearch Service |
| Amazon SageMaker AI (the ML service) | Amazon SageMaker. "SageMaker" is now the broader unified data, analytics and AI platform |
| Amazon QuickSight | Same name; it's now sold under the **Amazon Quick Suite** branding |
| Control Tower controls | Guardrails |

Services that are new or gone:

- **S3 Tables** and **SageMaker Lakehouse** are recent and may not appear in exam material.
- **QLDB** is discontinued; AWS points to Aurora PostgreSQL instead.
- **Snow Family:** AWS no longer offers several Snow devices to new customers and points to DataSync and the AWS Data Transfer Terminal. Exam questions may still feature Snowball.

## Course errata

- **KMS and "in transit":** the course says KMS encrypts data at rest and in transit. KMS keys protect data **at rest**. Data **in transit** is protected by **TLS**, with certificates from [ACM](../aws-services/aws-apis/acm.md). KMS is involved in transit mostly when an app encrypts data itself before sending it.
- **Transfer Family protocols:** the course text says "SFTP, FTPS, and SFTP". Transfer Family supports **SFTP, FTPS, FTP and AS2**.
- **Lake Formation lineage:** the course says Lake Formation "automatically catalogs… transformations". Lake Formation records **where tables live** and controls access. Full **lineage** is a feature of **DataZone / SageMaker Catalog**.
- **Systems Manager:** the course calls it "application-level monitoring for EC2". It's mainly an **operations management** toolkit; most metrics and alarms come from CloudWatch.
- **Control Tower:** the course lists it under data and network security. It's really an **account governance** service.
- **XML:** the course lists XML as both structured and semi-structured. Plain XML is structured; **XML with attributes** is semi-structured.
