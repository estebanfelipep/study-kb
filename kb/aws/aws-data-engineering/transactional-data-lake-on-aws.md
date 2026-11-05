# Transactional data lake on AWS

This file covers how a transactional data lake is built on AWS with an open table format, mainly Apache Iceberg: the services it works with, the four usual steps, and a reference architecture.

## Sources

- [Understanding Apache Iceberg on AWS with the new technical guide](https://aws.amazon.com/blogs/big-data/understanding-apache-iceberg-on-aws-with-the-new-technical-guide/): AWS Big Data Blog, Iceberg on AWS.
- [Using the Delta Lake framework in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-delta-lake.html): AWS Glue User Guide, Delta Lake in Glue.
- [Build your Apache Hudi data lake on AWS using Amazon EMR – Part 1](https://aws.amazon.com/blogs/big-data/part-1-build-your-apache-hudi-data-lake-on-aws-using-amazon-emr/): AWS Big Data Blog, Hudi on EMR.

## Why Iceberg

Iceberg is the format most widely adopted for data lakes on AWS, for its performance and scalability. It works with open-source engines such as Apache Spark and Trino, and with these AWS services: [Glue](../aws-services/aws-analytics/glue.md), [EMR](../aws-services/aws-analytics/emr.md), [Athena](../aws-services/aws-analytics/athena.md) and Redshift Spectrum ([redshift.md](../aws-services/aws-analytics/redshift.md)).

## Using Iceberg: the four steps

These are the steps to set up and use an Iceberg table with AWS services, in the order you do them. They aren't the five pipeline stages ([aws-data-pipeline.md](aws-data-pipeline/aws-data-pipeline.md)), but each one maps onto a stage:

| Step | What happens | Services | Pipeline stage |
| --- | --- | --- | --- |
| 1. Create | Create an Iceberg table and write data to it | Athena, or another compatible tool | 2. Store (setup) |
| 2. Catalog | The new table is available in the Glue Data Catalog | Glue Data Catalog | 3. Catalog |
| 3. Ingest | Batch or streaming ingestion. The data and metadata files are stored in S3 | EMR, Glue, Managed Service for Apache Flink | 1. Ingest and 4. Process |
| 4. Query | Query the tables | Athena, Redshift Spectrum, or another compatible tool | 5. Deliver |

They differ from the pipeline in two ways:

- **Catalog comes before ingest.** With plain files, data lands first and a [Glue crawler](../aws-services/aws-analytics/glue.md) discovers its schema afterward. An Iceberg table has its schema from the moment it's created, so it's in the Data Catalog before any data is written, and no crawler is needed.
- **Ingest and process are one step.** The engines that write into the table (EMR, Glue, Flink) are the processing engines, so the course doesn't separate the two stages.

## Reference architecture

The Iceberg dataset in S3 is the output of the ingest and process stages. The diagram follows the pipeline more closely than the four steps do. It still draws ingest and process as one layer, and it shows the catalog as governance beside the store.

```
Sources
  S3 (raw storage)            Amazon MSK (streams)
        │                           │
        └─────────────┬─────────────┘
                      ▼
Ingest and process
  EMR   │   Glue ETL   │   Managed Service for Apache Flink
                      │  write
                      ▼
Store
  Apache Iceberg dataset in S3 (data and metadata files)
  Governed by: Glue Data Catalog and Lake Formation
                      │  read
                      ▼
Consume
  Redshift   │   Athena   │   EMR   │   SageMaker
```

## Other formats on AWS

| Format | Where the course points |
| --- | --- |
| Delta Lake | The Delta Lake framework in Glue (see Sources) |
| Apache Hudi | A Hudi data lake built on EMR (see Sources) |

## Related

- [open-table-formats.md](../../data-engineering/open-table-formats.md): the concept this file implements: the problems a table format solves, and what Iceberg, Hudi and Delta Lake add.
- [s3.md](../aws-services/aws-general-services/s3.md): stores the Iceberg data and metadata files. S3 Tables are S3 buckets built for Iceberg tables, with automatic maintenance.
- [athena.md](../aws-services/aws-analytics/athena.md): creates Iceberg tables and writes data to them (step 1), and queries them (step 4).
- [glue.md](../aws-services/aws-analytics/glue.md): the Data Catalog makes the Iceberg table available to every engine (step 2), and Glue ETL ingests into it (step 3).
- [emr.md](../aws-services/aws-analytics/emr.md): ingests into Iceberg tables in batch or streaming (step 3), and consumes them.
- [managed-service-for-apache-flink.md](../aws-services/aws-analytics/managed-service-for-apache-flink.md): the streaming ingest path into Iceberg tables (step 3).
- [msk.md](../aws-services/aws-analytics/msk.md): a streaming source in the reference architecture, read by the ingest engines.
- [redshift.md](../aws-services/aws-analytics/redshift.md): Redshift Spectrum queries the Iceberg tables in S3 (step 4).
- [lake-formation.md](../aws-services/aws-analytics/lake-formation.md): governs access to the Iceberg tables, together with the Glue Data Catalog.
- [sagemaker.md](../aws-services/aws-ai/sagemaker.md): consumes the Iceberg dataset for machine learning.
- [store-on-aws.md](aws-data-pipeline/store-on-aws.md): the Iceberg dataset lives in the store stage, in the S3 lake.
- [aws-data-pipeline.md](aws-data-pipeline/aws-data-pipeline.md): the five stages that the four Iceberg steps map onto. The steps put catalog before ingest, and treat ingest and process as one step.
- [exam-traps.md](exam-traps.md): maps "update or delete rows in the lake" to Iceberg on S3. It also notes that an Iceberg table created in Athena is already in the Data Catalog, so it needs no crawler.
