# aws-analytics — index

Streaming, ETL, big data processing, warehousing, querying, BI, and data lake governance and catalogs.

## How to read this folder

- **Before:** The five stages, in [modern-data-architecture.md](../../../data-engineering/modern-data-architecture.md), and [s3.md](../aws-general-services/s3.md).
- **Order:** Follow the pipeline: each group feeds the next.
- **After:** the `choosing-*` files in [aws-data-engineering](../../aws-data-engineering/aws-data-engineering.md).

## Files (in reading order)

**Ingest streams**

- [kinesis-data-streams.md](kinesis-data-streams.md): Amazon Kinesis Data Streams: records, shards, capacity modes, retention, replay, consumers. Read when: you need how KDS stores and serves streams, or its throughput and retention limits.
- [data-firehose.md](data-firehose.md): Amazon Data Firehose: managed stream delivery, Parquet/ORC conversion, buffering, destinations. Read when: you need how streaming data gets delivered to S3, Redshift or OpenSearch without servers.
- [msk.md](msk.md): Amazon MSK and MSK Serverless: managed Apache Kafka. Read when: a workload needs Kafka, or you need what MSK Serverless manages for you.

**Catalog and process**

- [glue.md](glue.md): AWS Glue: jobs, DPUs, job bookmarks, crawlers, Data Catalog, workflows, Glue Studio, Data Quality, sensitive data detection and KMS encryption. Read when: you need any part of Glue, how data gets cataloged, or how Glue protects PII.
- [emr.md](emr.md): Amazon EMR on EC2, EKS and Outposts, and EMR Serverless: frameworks, control, pricing. Read when: you need how EMR runs Spark/Hadoop workloads or what EMR Serverless removes.
- [managed-service-for-apache-flink.md](managed-service-for-apache-flink.md): Amazon Managed Service for Apache Flink: real-time stream processing (SQL, Java, Scala, Python) for filtering, aggregating, joining and windowing. Read when: you need real-time analytics on a stream.
- [entity-resolution.md](entity-resolution.md): AWS Entity Resolution: rule-based, ML-based or provider-based matching of records for the same entity, with match IDs written to S3. Read when: you need to match one customer's records across systems.

**Deliver**

- [athena.md](athena.md): Amazon Athena: serverless SQL directly on S3 (zero-ETL), billed per TB scanned, cheaper with Parquet/ORC and partitioning, plus federated query. Read when: you need how to query S3 data in place, or what makes Athena cost less.
- [redshift.md](redshift.md): Amazon Redshift data warehouse: columnar storage, MPP, Spectrum, federated query, streaming ingestion, auto copy, zero-ETL target, Redshift Serverless. Read when: you need how Redshift loads or queries data, or how Serverless is priced.
- [quicksight.md](quicksight.md): Amazon QuickSight: BI dashboards for business users, and pipeline and data-quality KPIs. Read when: you need visualization, dashboards, or business-facing monitoring reports.

**Govern**

- [lake-formation.md](lake-formation.md): Lake Formation permissions down to column, row and cell, tag-based access, cross-account sharing, audit logging, and the course correction on lineage. Read when: you need fine-grained data lake access or data lake governance.
- [datazone.md](datazone.md): DataZone business catalog, business glossary, self-service access requests, data mesh and lineage. Read when: you need business-facing data discovery and sharing across teams.
