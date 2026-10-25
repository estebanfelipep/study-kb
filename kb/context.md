# Glossary

This file holds the vocabulary shared across the subjects in this KB: terms, abbreviations, and service nicknames. Entries follow `../.claude/skills/kb-intake/references/glossary-format.md`.

## Language

**ACM**: AWS Certificate Manager. Provisions and renews the SSL/TLS certificates behind encryption in transit. See [acm.md](aws/aws-services/aws-apis/acm.md).

**Automation**: Running a single repetitive task without manual effort. See [orchestration-and-automation.md](data-engineering/orchestration-and-automation.md).

**CDC**: Change data capture. Replicating a database's ongoing inserts, updates and deletes rather than reloading it. See [replicating-databases-to-the-lake.md](data-engineering/replicating-databases-to-the-lake.md).

**CDO**: Chief data officer. The executive who builds a data-driven culture and owns data and AI strategy. See [data-personas.md](data-engineering/data-personas.md).

**CIA triad**: Confidentiality, integrity and availability, the three goals of data security. See [data-security-and-monitoring.md](data-engineering/data-security-and-monitoring.md).

**Columnar format**: A file or storage layout that stores each column together, so queries read only the columns they need. Parquet and ORC are columnar file formats. See [data-lakes-and-warehouses.md](data-engineering/data-lakes-and-warehouses.md).

**Crawler**: A Glue component that scans data, infers format and schema, and writes tables to the Data Catalog. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**DAG**: Directed acyclic graph. A workflow of tasks and their dependencies, as defined in Apache Airflow. See [orchestration-and-automation.md](data-engineering/orchestration-and-automation.md).

**Data catalog**: The metadata store that makes a data lake's contents findable: what data exists, where, its quality and how it's used. It stores metadata, not the data. See [modern-data-architecture.md](data-engineering/modern-data-architecture.md).

**Data discovery**: Finding and understanding an organization's relevant data sources and how they relate; the first step of a data project. See [data-discovery.md](data-engineering/data-discovery.md).

**Data lake**: A centralized repository for structured, semi-structured and unstructured data at scale, stored without extensive preprocessing. On AWS, built on S3. See [data-lakes-and-warehouses.md](data-engineering/data-lakes-and-warehouses.md).

**Data silo**: An isolated, incompatible data store optimized for one department or use case. See [modern-data-architecture.md](data-engineering/modern-data-architecture.md).

**Data swamp**: A data lake without a catalog: files nobody can find or trust. See [modern-data-architecture.md](data-engineering/modern-data-architecture.md).

**Data warehouse**: A columnar SQL analytics database for curated, modeled data, with schema-on-write. On AWS, Redshift. See [data-lakes-and-warehouses.md](data-engineering/data-lakes-and-warehouses.md).

**DLQ**: Dead-letter queue. Holds messages that failed processing too many times, so they don't block the queue. See [sqs.md](aws/aws-services/aws-application-coordination/sqs.md).

**DPU**: Data processing unit. The capacity and billing unit of Glue jobs. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**Entity resolution**: Matching records that refer to the same real-world entity, such as one customer under different IDs in different systems. See [unified-customer-data.md](data-engineering/unified-customer-data.md).
_Avoid:_ record linkage, identity resolution

**Envelope encryption**: KMS encrypts a small data key, and the data key encrypts the data. See [kms.md](aws/aws-services/aws-security/kms.md).

**ETL**: Extract, transform, load. Get data from sources, make it useful, and serve it to stakeholders. See [data-engineer-role.md](data-engineering/data-engineer-role.md).

**Fan-out**: Delivering one message to many consumers, often SNS to several SQS queues. See [orchestration-and-automation.md](data-engineering/orchestration-and-automation.md).

**Federated query**: Querying an external database in place from Athena or Redshift, without loading it. See [athena.md](aws/aws-services/aws-analytics/athena.md).

**Full load**: Copying every row of a database's tables once, usually before CDC takes over. See [replicating-databases-to-the-lake.md](data-engineering/replicating-databases-to-the-lake.md).

**Golden record**: The single trusted, merged record for one entity, built by matching and survivorship rules. See [unified-customer-data.md](data-engineering/unified-customer-data.md).
_Avoid:_ customer 360, single customer view

**Job bookmark**: Glue's record of data a job already processed, so each run handles only new data. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**Lake house**: A lake and a warehouse used together: the lake holds everything, and the warehouse serves the curated, high-performance part and can query the lake in place. See [data-lakes-and-warehouses.md](data-engineering/data-lakes-and-warehouses.md).

**Least privilege**: Granting only the permissions a role needs. See [iam.md](aws/aws-services/aws-identity/iam.md).

**MDM**: Master data management. The ongoing practice of keeping one trusted version of core entities, such as customers or products, across systems. See [unified-customer-data.md](data-engineering/unified-customer-data.md).

**Micro-batch**: Ingesting data in small, frequent batches, between batch and streaming. See [batch-and-streaming.md](data-engineering/batch-and-streaming.md).

**MPP**: Massively parallel processing. Spreading a query's work across many nodes, as Redshift does. See [data-lakes-and-warehouses.md](data-engineering/data-lakes-and-warehouses.md).

**MTTD / MTTR**: Mean time to detection and mean time to recovery. See [data-discovery.md](data-engineering/data-discovery.md).

**OLAP**: Online analytical processing. Large scans and aggregations for analytics, on columnar storage. See [data-lakes-and-warehouses.md](data-engineering/data-lakes-and-warehouses.md).

**OLTP**: Online transaction processing. Many small reads and writes for an application, on row-based storage. See [data-lakes-and-warehouses.md](data-engineering/data-lakes-and-warehouses.md).

**Open table format**: A table layer over lake files, such as Apache Iceberg, that adds updates, deletes and merges. See [replicating-databases-to-the-lake.md](data-engineering/replicating-databases-to-the-lake.md).

**Orchestration**: Coordinating multiple services and their dependencies through a series of steps. See [orchestration-and-automation.md](data-engineering/orchestration-and-automation.md).

**Partition key**: A producer-chosen value that decides which shard or partition a stream record goes to, keeping one key's records in order. See [batch-and-streaming.md](data-engineering/batch-and-streaming.md).

**PII**: Personally identifiable information. See [macie.md](aws/aws-services/aws-security/macie.md).

**Pub/sub**: Publish/subscribe. Publishers send to a topic, and every subscriber gets a copy. See [orchestration-and-automation.md](data-engineering/orchestration-and-automation.md).

**Reverse ETL**: Pushing cleaned data back into operational tools, such as a CRM. See [data-engineer-role.md](data-engineering/data-engineer-role.md).

**RPU**: Redshift Processing Unit. The capacity unit of Redshift Serverless. See [redshift.md](aws/aws-services/aws-analytics/redshift.md).

**Schema-on-read / schema-on-write**: Applying structure when data is read (lakes) vs defining it before loading (warehouses, databases). See [data-lakes-and-warehouses.md](data-engineering/data-lakes-and-warehouses.md).

**Serverless**: Building and running applications without managing infrastructure, paying only while code runs. See [orchestration-and-automation.md](data-engineering/orchestration-and-automation.md).

**Shard**: An ordered unit of a Kinesis stream, with about 1 MB/s in and 2 MB/s out. See [kinesis-data-streams.md](aws/aws-services/aws-analytics/kinesis-data-streams.md).

**Spectrum**: Redshift Spectrum, which queries files in S3 from Redshift without loading them. See [redshift.md](aws/aws-services/aws-analytics/redshift.md).

**State machine**: A Step Functions workflow made of states such as task, choice, parallel, wait and map. See [step-functions.md](aws/aws-services/aws-application-coordination/step-functions.md).

**Stream**: A continuous, ordered sequence of small records, appended as events happen and kept for a retention period. See [batch-and-streaming.md](data-engineering/batch-and-streaming.md).

**Structured / semi-structured / unstructured data**: Data in fixed tables, data with flexible structure (JSON, logs), and data with no data model (documents, images, audio, video). See [data-discovery.md](data-engineering/data-discovery.md).

**Survivorship**: The rules that decide which source wins for each field when records are merged into a golden record. See [unified-customer-data.md](data-engineering/unified-customer-data.md).

**Visibility timeout**: How long an SQS message stays hidden from other consumers while one processes it. See [sqs.md](aws/aws-services/aws-application-coordination/sqs.md).

**VPC endpoint**: Private access from a VPC to AWS services such as S3, Glue or KMS without the internet. See [vpc.md](aws/aws-services/aws-networking/vpc.md).

**Zero-ETL**: Querying or replicating data without building ETL pipelines. See [orchestration-and-automation.md](data-engineering/orchestration-and-automation.md).

## Service names

**Amazon Data Firehose**: Managed delivery of streaming data to S3, Redshift, OpenSearch and more. See [data-firehose.md](aws/aws-services/aws-analytics/data-firehose.md).
_Avoid:_ Kinesis Data Firehose

**Amazon Managed Service for Apache Flink**: Real-time stream processing. See [managed-service-for-apache-flink.md](aws/aws-services/aws-analytics/managed-service-for-apache-flink.md).
_Avoid:_ Kinesis Data Analytics

**Amazon OpenSearch Service**: Managed search and log analytics. See [opensearch-service.md](aws/aws-services/aws-databases/opensearch-service.md).
_Avoid:_ Amazon Elasticsearch Service

**Amazon QuickSight**: BI dashboards, sold under the Amazon Quick Suite branding. See [quicksight.md](aws/aws-services/aws-analytics/quicksight.md).
_Avoid:_ Quick Suite (when meaning the BI service)

**Amazon SageMaker AI**: The ML build, train and deploy service; "SageMaker" alone is the broader data, analytics and AI platform. See [sagemaker.md](aws/aws-services/aws-ai/sagemaker.md).

**Control Tower control**: A preventive or detective rule in a Control Tower landing zone. See [control-tower.md](aws/aws-services/aws-security/control-tower.md).
_Avoid:_ guardrail

**DMS**: AWS Database Migration Service. See [dms.md](aws/aws-services/aws-databases/dms.md).

**KDS**: Amazon Kinesis Data Streams. See [kinesis-data-streams.md](aws/aws-services/aws-analytics/kinesis-data-streams.md).

**MSK**: Amazon Managed Streaming for Apache Kafka. See [msk.md](aws/aws-services/aws-analytics/msk.md).

**MWAA**: Amazon Managed Workflows for Apache Airflow. See [mwaa.md](aws/aws-services/aws-application-coordination/mwaa.md).
