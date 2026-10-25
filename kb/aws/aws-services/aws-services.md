# aws-services — index

This folder holds one file per AWS service, grouped into category subfolders. A service's facts live in its one file, whichever certification or track they came up in. A service that belongs to two or more categories goes in `aws-general-services/` instead of being split or copied. Once a service outgrows one file, it moves into its own subfolder with an index (`glue/glue.md`).

Every service file has the same shape: **What it is**, **Characteristics**, **Example**, and **Related** links. Comparisons between services and exam pick-rules don't live here; they're in the `choosing-*` files of [aws-data-engineering](../aws-data-engineering/aws-data-engineering.md).

## How to read this folder

- **Before:** the concept behind a service, in [data-engineering](../../data-engineering/data-engineering.md). For the exam, start from [aws-data-engineering](../aws-data-engineering/aws-data-engineering.md) instead.
- **Order:** this is a reference to dip into. To read it through anyway, follow the groups below. Inside a service file, Related says where to go next.
- **After:** the matching `choosing-*` file, to see how a service compares with its alternatives.

## Subfolders (in reading order)

**Foundations** that almost every other service relies on

- [aws-general-services/](aws-general-services/aws-general-services.md): services that belong to two or more categories (S3). Read when: the service is used across many parts of an architecture.
- [aws-identity/](aws-identity/aws-identity.md): IAM. Read when: you need how users, roles and services get permissions.
- [aws-networking/](aws-networking/aws-networking.md): VPC, subnets, VPC endpoints, security groups and network ACLs. Read when: you need how resources are kept off the public internet.

**The pipeline,** from sources to delivery

- [aws-migration-and-transfer/](aws-migration-and-transfer/aws-migration-and-transfer.md): DataSync, Transfer Family and Snow Family. Read when: you need to move files or bulk data into AWS.
- [aws-iot/](aws-iot/aws-iot.md): IoT Core. Read when: you need to ingest data from devices.
- [aws-databases/](aws-databases/aws-databases.md): RDS and Aurora, DMS, DynamoDB and OpenSearch Service. Read when: you need an operational database, search, or database migration.
- [aws-analytics/](aws-analytics/aws-analytics.md): Kinesis Data Streams, Data Firehose, MSK, Glue, EMR, Managed Service for Apache Flink, Athena, Redshift, QuickSight, Lake Formation and DataZone. Read when: you need streaming, ETL, warehousing, querying, BI, or data lake governance.
- [aws-ai/](aws-ai/aws-ai.md): SageMaker. Read when: you need machine learning.

**Glue between steps**

- [aws-compute/](aws-compute/aws-compute.md): Lambda. Read when: you need to run code, especially on an event.
- [aws-application-coordination/](aws-application-coordination/aws-application-coordination.md): SQS, SNS, EventBridge, Step Functions and MWAA. Read when: you need to orchestrate, trigger or decouple pipeline steps.
- [aws-apis/](aws-apis/aws-apis.md): API Gateway and ACM. Read when: you need to expose an API or serve HTTPS.

**Wrapping everything**

- [aws-security/](aws-security/aws-security.md): KMS, Macie, GuardDuty, WAF, Shield, Control Tower and Audit Manager. Read when: you need encryption, PII discovery, threat detection, web or DDoS protection, account governance or compliance evidence.
- [aws-monitoring/](aws-monitoring/aws-monitoring.md): CloudWatch, X-Ray, Managed Grafana, CloudTrail, Config and Systems Manager. Read when: you need metrics, logs, traces, auditing or operational dashboards.
