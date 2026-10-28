# Choosing storage and processing services

This file holds the comparisons and exam pick-rules for where data lives (lake, warehouse, databases, block and file storage) and what transforms it (Glue, EMR, Flink).

Service details are in each service's file in [aws-services](../aws-services/aws-services.md). The vendor-neutral concepts are in [data-lakes-and-warehouses.md](../../data-engineering/data-lakes-and-warehouses.md).

## Storage

### S3 vs Redshift: lake vs warehouse

**S3 is storage. Redshift is a query engine with its own storage, built for analytics.** They usually work together.

|  | **S3 (data lake)** | **Redshift (data warehouse)** |
| --- | --- | --- |
| What it is | Object storage | Managed, columnar SQL analytics database |
| Data it holds | Anything: structured, semi-structured, unstructured, raw files | Mostly structured, modeled tables |
| Schema | **Schema-on-read** | **Schema-on-write** |
| Queries data itself? | No. Add an engine: Athena, EMR, Glue | Yes. Tuned for fast, complex SQL at high concurrency |
| Cost | Very cheap per GB | More expensive (compute plus storage) |
| Typical users | Data engineers, data scientists | Analysts, BI dashboards |

**Why they seem to overlap:** Redshift Spectrum runs SQL directly over files in S3, and Redshift can export results back to S3 in open formats. AWS calls the combination a **lake house**. Redshift *reaches into* the lake but isn't the lake.

### RDS vs Redshift: OLTP vs OLAP

**RDS runs the application (OLTP). Redshift analyzes the data (OLAP).**

|  | **RDS** | **Redshift** |
| --- | --- | --- |
| Workload | **OLTP** | **OLAP** |
| Storage layout | **Row-based** | **Columnar** |
| Scale | GB to a few TB; scale up plus read replicas | TB to PB; **MPP** across nodes |
| Users | The application | Analysts, BI tools, dashboards |
| Engines | MySQL, PostgreSQL, MariaDB, Oracle, SQL Server (plus Aurora) | Redshift (PostgreSQL-compatible SQL) |

**In the flow, RDS is a source:** the app writes to RDS, Glue, DMS or zero-ETL integration copies the data to S3 and/or Redshift, and analysts query Redshift without touching the production database.

### Is RDS a data lake? No.

| Requirement | S3 | RDS |
| --- | --- | --- |
| **Centralized repository** for the whole organization | ✅ One place every source lands in | ❌ Usually one database per application, a silo by design |
| **Structured** data | ✅ | ✅ |
| **Semi-structured** data | ✅ JSON, logs, Parquet, anything | ⚠️ Partly: JSON columns exist, but data must still fit tables |
| **Unstructured** data (images, video, audio, documents) | ✅ Stored natively as objects | ❌ Only as binary blobs, which is slow, costly and an anti-pattern |
| **At scale** | ✅ Practically unlimited, GB to PB, no disruption | ❌ Capped at tens of TB per instance; you provision and resize |
| **No extensive preprocessing** | ✅ Drop raw files in as is | ❌ Schema first (schema-on-write) |
| **Pay for what you use** | ✅ Per GB stored | ❌ Running instance plus provisioned storage, used or not |

### DynamoDB vs RDS/Aurora

- **DynamoDB:** NoSQL, access by key, massive scale, fully serverless, predictable millisecond latency. No joins or complex ad hoc SQL.
- **RDS/Aurora:** relational SQL, joins, transactions across tables, flexible queries. You choose instance sizes (except Aurora Serverless).

### S3 vs EBS vs EFS

- **S3:** object storage over HTTP; serverless and unlimited. Use it for files, data lakes and static sites.
- **EBS:** block storage attached to **one EC2 instance**. It needs a server.
- **EFS:** a shared file system (NFS) for **many EC2 instances, containers or Lambda functions** that need a mounted file system.

### Redshift Serverless vs provisioned Redshift

- **Serverless:** variable or unpredictable workloads, new projects, least management.
- **Provisioned:** steady, heavy, 24/7 workloads, where reserved instances make it cheaper, and where you want control over node types and counts.

## Processing

### If the question says… pick

| If the question says… | Pick |
| --- | --- |
| "Serverless ETL", "least operational overhead", "crawl and catalog", "visual ETL editor" | [Glue](../aws-services/aws-analytics/glue.md) |
| "Existing **Spark/Hadoop/Hive/Presto** jobs", "migrate on-premises Hadoop", "full control over the cluster", "petabyte-scale batch", "custom frameworks" | [EMR](../aws-services/aws-analytics/emr.md) |
| "Analyze streaming data in **real time**", "windowed aggregations on a stream", "Apache Flink" | [Managed Service for Apache Flink](../aws-services/aws-analytics/managed-service-for-apache-flink.md) |

**Glue vs EMR in one line:** both run Apache Spark. Glue is **serverless and opinionated** (less to manage). EMR gives you **control and a wider range of frameworks** (more to manage, unless you use EMR Serverless).

**Firehose vs processing:** Firehose does light, in-flight transformation such as format conversion. Heavier logic belongs in Glue, EMR or Flink.

### EMR Serverless vs EMR on EC2 vs Glue

|  | **EMR Serverless** | **EMR on EC2** | **AWS Glue** |
| --- | --- | --- | --- |
| Management | No clusters | You manage clusters | No clusters |
| Frameworks | Spark, Hive | Spark, Hive, Presto, HBase, Flink and more; custom software | Spark (and Python shell, Ray) |
| Control | Medium | **Full** (instance types, Spot, configuration, SSH) | Lowest |
| Extras | Open-source Spark experience | Widest flexibility | **Crawlers, Data Catalog, visual editor, data quality** |
| Pick it when | Existing Spark/Hive code, no cluster management | Need full control, other frameworks or long-running clusters | Serverless ETL integrated with the catalog |

### Glue vs EMR Serverless

- **Glue:** ETL-first, tightly integrated with the catalog, crawlers, visual editor and data quality. Best for **building pipelines**.
- **EMR Serverless:** open-source Spark and Hive, closer to the frameworks themselves. Best for **existing big-data code** and data science workloads.

## Streaming platforms

### MSK Serverless vs provisioned MSK vs Kinesis Data Streams on-demand

- **MSK Serverless:** Kafka without operations. Best for variable workloads and smaller teams.
- **Provisioned MSK:** Kafka with full control over broker types, configuration and very high, steady throughput.
- **Kinesis Data Streams on-demand:** also serverless streaming, but **AWS-native** rather than Kafka. Pick it when you're not tied to Kafka.
