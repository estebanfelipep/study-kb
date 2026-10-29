# AWS Glue

AWS Glue: serverless data integration, covering jobs, crawlers and classifiers, the Data Catalog, workflows, Glue Studio, Data Quality and sensitive data detection.

## Sources

- [What Is a Data Catalog?](https://aws.amazon.com/what-is/data-catalog/): AWS overview of data catalogs and the Glue Data Catalog.
- [Data discovery and cataloging in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html): AWS Glue User Guide, the Data Catalog and crawlers.
- [Optimizing query performance using column statistics](https://docs.aws.amazon.com/glue/latest/dg/column-statistics.html): AWS Glue User Guide, computing column-level statistics.
- [AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html): AWS Glue User Guide, Data Quality.

## What it is

AWS Glue is a serverless data integration service and a fully managed ETL service. It
- prepares and cleanses data from various sources
- classifies data
- extracts schema 
- and populates data catalogs. 

It **consolidates data integration capabilities into a single service**: connecting to different data sources, discovering data, cataloging, ensuring data quality and transforming the data.

It appears in five of the six data engineer functions (infrastructure, ingest, prepare, catalog, automate) and across the whole flow: jobs for ingestion, crawlers and the Data Catalog for cataloging, ETL for processing, and workflows for automation. It's the central service of the training.

**In one line: Glue turns raw files in S3 into data you can find, trust and query, without running servers.** 

It's a family of tools under one name that share one hub, the Data Catalog: crawlers and the catalog **describe** the data, and jobs **transform** it. Glue is mainly a cataloging and processing service, not an orchestrator: workflows are its only orchestration, and they chain only Glue's own crawlers and jobs.

## Characteristics

### Problems each part solves

| Problem | Without Glue | Glue's answer | Stage |
| --- | --- | --- | --- |
| Nobody knows what columns, format or partitions the S3 files have | A data swamp; each team and engine defines its own tables | **Crawlers** infer the schema and partitions and write them to the catalog | Catalog |
| Athena, EMR and Redshift Spectrum each need the table structure | Definitions per engine, drifting apart | **Data Catalog**: one definition, read by every engine | Catalog |
| Raw data is messy and too big for a script | Run your own Spark cluster, or hit Lambda's 15-minute limit | **Jobs**: serverless Spark that cleans, joins and writes partitioned Parquet | Process |
| Each run would reprocess all of history | Rereading everything, every night | **Job bookmarks**: only new data | Process |
| Bad rows or PII would reach analysts | Silent bad data, exposed contact details | **Data Quality** rules and **sensitive data detection** | Process, security |
| Crawler, then job, then the next job | Manual runs or cron | **Workflows and triggers** | Automation |

- **Serverless:** jobs scale automatically; you don't manage infrastructure and pay only per use.
- Part of the **security and auditability** story: KMS encryption, data masking, and the Data Catalog's table history.

### Jobs

- Ingest and transform data. Run on **Apache Spark**, or **Python shell** for small tasks (also Ray).
- Capacity is measured in **DPUs** (data processing units), billed per second while a job runs.
- Mostly batch; also **streaming ETL**.
- **Job bookmarks** remember what was already processed, so each run handles only new data.
- Connectors to many sources.
- Run for hours on GB to TB of data (distributed Spark), so they suit transformations that would time out in [Lambda](../aws-compute/lambda.md).
- The usual pattern is **S3 to S3**: a job reads objects from one zone's prefix or bucket and writes **new** objects to the next zone: `raw/` → `cleaned/` (filter, standardize, correct), then `cleaned/` → `curated/` (join, aggregate). Lake files are written once, so the raw objects stay unchanged as the source of truth. The zones are in [data-lake-zones.md](../../../data-engineering/data-lake-zones.md).
- S3 isn't the only target: jobs can also write to Redshift or to databases over JDBC.

### Crawlers

A crawler **scans data in all kinds of repositories, classifies it, extracts schema information from it, and stores the metadata in the Data Catalog automatically**. It adds new tables, new partitions to existing tables, and new versions of table definitions.

- Flow: data lands in S3 → crawlers catalog it → it becomes discoverable and queryable.
- Used in discovery step 5 to extract relevant data (or custom scripts).
- **Optional.** A table can also be written to the catalog by hand or with DDL, for example `CREATE EXTERNAL TABLE` in [Athena](athena.md). Crawlers pay off when there are many sources, schemas change, or new partitions keep arriving.

#### What a run does

```
 data store ─► 1. classify ─► 2. group into ─► 3. write to the
 (S3 path)     classifier     tables or        Data Catalog:
               infers the     partitions       create or update
               format and                      tables and
               schema                          partitions
```

1. **Uses a classifier** to discover and infer the structure of the data: its format, schema and associated properties.
2. **Groups the data into tables or partitions.** It infers file types and schemas, and identifies the dataset's partition structure automatically. Partitions restrict how much data each query scans, which improves performance and reduces cost ([partitioning.md](../../../data-engineering/partitioning.md)).
3. **Populates the Data Catalog.** On completion it creates or updates one or more tables with their definitions and partitions. You configure how it adds, updates and deletes tables and partitions.
4. **Creates a single schema for each S3 path,** when configured to combine compatible schemas into a common table definition:
   - If the compared schemas match (the partition threshold is higher than 70 percent), they become **partitions of one table**.
   - If they don't match, it creates **a table for each S3 path**, which means many more tables. You can set a maximum number of tables a crawler may create.

```
 .../mytable/year=2024/month=3/day=13/   schemas match
 .../mytable/year=2024/month=3/day=14/   ─► 1 table, 2 partitions

 .../a/  .../b/                          schemas don't match
                                         ─► 2 tables
```

#### Defining a crawler

| Parameter | What it is |
| --- | --- |
| **Data source** | The data store to scan, such as an S3 folder. One crawler can scan several data stores in a single run. |
| **Target** | The Glue database the tables are written to, created beforehand. |
| **IAM role** | A role with permissions to read the data ([iam.md](../aws-identity/iam.md)). |
| **Schedule** | When it runs: on a schedule, on demand, or invoked by an event, to keep the metadata up to date. |

- **Recommended:** keep the default setting of **always updating Data Catalog tables**, so the catalog stays in sync with the S3 lake.
- **Incremental crawls:** configure the crawler to scan only new subfolders, adding just the new partitions.

#### Classifiers

A classifier **determines the schema of the data** by comparing it to a known set of schema types, or to custom types you specify. On a match, the schema is extracted and written to the Data Catalog.

A crawler has a list of classifiers. **The first one in the list that recognizes the data** creates the table's schema.

| Kind | What it does |
| --- | --- |
| **Built-in** | Provided by Glue. Infers schemas from common formats, including JSON, CSV and Apache Avro. |
| **Custom** | Defined by you to control the classification result. Custom classifiers run in the order you specify, and you define them in a separate operation before defining the crawlers. |

### Data Catalog

The **central metadata repository for all the data assets** in a data lake's locations. It's a **collection of tables organized within databases**. Each table holds metadata about a dataset, such as its location, schema and runtime metrics. Once data is cataloged, engines can **access it as tables, in a SQL-like way**, and query and transform it consistently across many applications.

#### Structure

```
Data Catalog         one per AWS account per Region
 └─ database         db_raw
     └─ table        sales
         ├─ storage descriptor   format, S3 location,
         │                       SerDe, schema
         ├─ partition keys       year, month, day
         │   └─ partitions       one per S3 path
         ├─ parameters           description, creator, ...
         └─ table type           EXTERNAL_TABLE, ...
```

#### What a table holds

| Entry | What it holds | Example |
| --- | --- | --- |
| **Name** | The table's name | `mytable` |
| **DatabaseName** | The database the table belongs to | `db_raw` |
| **StorageDescriptor** | The physical storage properties: data format (CSV, Parquet), the data's location in S3, the serialization and deserialization (SerDe) libraries, and the schema (column names and data types) | `name: string`, `year: integer`, `price: double` |
| **PartitionKeys** | The columns the data is partitioned by, which can improve query performance ([partitioning.md](../../../data-engineering/partitioning.md)) | `year`, `month`, `day` |
| **Parameters** | Key-value pairs of extra metadata, such as the table's description, creator and creation time | `creator: data-eng` |
| **Table type** | The kind of table | `EXTERNAL_TABLE`, `VIRTUAL_VIEW` |

Partitions of a table partitioned by day, after two days of data:

| Partition | Values | Location |
| --- | --- | --- |
| 1 | `year=2024/month=3/day=13` | `s3://doc-example-bucket/data/mytable/year=2024/month=3/day=13/` |
| 2 | `year=2024/month=3/day=14` | `s3://doc-example-bucket/data/mytable/year=2024/month=3/day=14/` |

#### How a query uses a table

**A table holds no data and no copy of it.** The files stay in S3, and the table only describes them: schema, format, location and partitions. A crawler builds that description from the files: it reads them to infer one schema across them, reads the partition keys from the folder names, and registers each folder as a partition.

```
Data Catalog: db_raw.website_clicks        S3: raw/website_clicks/
┌──────────────────────────────────┐
│ location: s3://raw/website_clicks│──points to──► the JSON files
│ format:   JSON (JSON SerDe)      │               (the only copy
│ columns:  user_id int, page      │                of the data)
│           string, ts string      │
│ partition keys: year, month, day │
│ partitions:                      │
│   2024/3/12 ─► .../day=12/       │
│   2024/3/13 ─► .../day=13/       │
└──────────────────────────────────┘
```

1. A query names a table, for example `SELECT … FROM db_raw.website_clicks WHERE day = '13'`.
2. The engine (such as [Athena](athena.md)) reads the table's definition from the catalog: the columns, the format to parse, and which partitions match the `WHERE` clause.
3. It reads **the files in S3 directly**, only under the matching partitions' locations.

The crawler doesn't run queries. It **records** the partitions, and the engine uses them to skip folders. On later runs, the crawler adds new folders as new partitions and new fields as new columns, saved as a new table version.

#### Ways to populate it

| Way | How |
| --- | --- |
| **Crawlers** | Discover the data, recognize its structure and add the metadata automatically. See "Crawlers" above. |
| **Manually** | Add and update table details in the Glue console, or through the API with the AWS CLI. |
| **DDL queries** | For example, `CREATE EXTERNAL TABLE` in [Athena](athena.md), which stores the definition here. |
| **DMS** | Fills the catalog with the tables it writes to S3 ([dms.md](../aws-databases/dms.md)). |

#### Features and considerations

- **One Data Catalog per AWS account per Region.**
- **Stores metadata, not the data.** The data stays in S3; the catalog holds table definitions that point to it.
- **Schemas can be edited by hand:** change column data types, add columns, or modify table properties.
- **Schema version history:** each schema change creates a new table version, so you can compare versions, review how the data changed over time, or roll back.
- **Column-level statistics:** compute the minimum, maximum, total nulls and total distinct values for a table's columns, to optimize query performance.
- **Data quality:** measured and monitored with Glue Data Quality (below).
- **Tracks how data has changed over time**, including metadata changes as data moves between stores such as S3 and Redshift. This helps trace the flow of data.
- Lets you search for data sources by attributes such as name, owner and business terms, and add business-relevant attributes. Supports owners, descriptions and custom table properties; the full business glossary lives in [DataZone](datazone.md).
- **One catalog, many engines:** [Athena](athena.md) relies on it to store and retrieve the metadata (tables, columns, data types) of what it queries, [EMR](emr.md) reads it to understand the structure and location of the data it processes, and Redshift Spectrum and Glue jobs read it too. Compatible with the **Apache Hive metastore**.
- **Athena has no catalog of its own.** Tables created in Athena are stored here too, so Athena uses the Data Catalog even when no crawler or job is involved.
- [Lake Formation](lake-formation.md) permissions are applied to Data Catalog resources (databases, tables, columns), so the catalog is the anchor for governance.
- The catalog and connection passwords can be encrypted with KMS.
- For the catalog concept (single source of truth, data swamp), see [modern-data-architecture.md](../../../data-engineering/modern-data-architecture.md).

### Workflows

- Orchestrate a chain of Glue crawlers, jobs and triggers. Only Glue; serverless. (defined in the Glue console or API)

### Glue Studio

- The visual editor for building ETL jobs. It answers discovery step 5's "Do you have a visual editor?"

### Data Quality

- Measures and monitors the quality of data with rules.
- **In a job:** rules check the data as the job runs, for example failing the job when too many rows break a rule.
- **On Data Catalog tables:** rules measure and monitor the quality of cataloged data.

### Sensitive data protection

- Protects sensitive data with **encryption with KMS** and **data masking**.
- **Security configurations** encrypt job output in S3, CloudWatch logs and job bookmarks with KMS.
- **Sensitive data detection** finds PII in a job's data while the job processes it, and can **redact, hash or partially mask** it.

## Example

How the parts fit in one lake:

```
sources ─► S3 raw/ ─► crawler ─► Data Catalog ◄─ Athena, EMR and
              │                    ▲    ▲        Spectrum read the
              ▼                    │    │        tables here
          Glue job (Spark) ────────┘    │
          bookmarks, quality,           │
          PII masking             Lake Formation
              │                   permissions
              ▼
          S3 cleaned/, then curated/ (partitioned
                       Parquet, registered as tables)

Glue workflow: crawler → job → crawler, in order
```

- **Example Corp** catalogs its raw zone with three crawlers into the database `db_raw`, with the tables `sales`, `marketing_campaigns` and `website_clicks`. See the catalog section of [example-corp-pipeline-on-aws.md](../../aws-data-engineering/aws-data-pipeline/example-corp-pipeline-on-aws.md).
- Nightly ETL: a Glue job reads only new JSON order files from S3 (job bookmarks), joins them with the customer table from the Data Catalog, drops test orders, standardizes country codes, and writes partitioned Parquet back to S3. A data-quality rule fails the job if more than 1% of orders have no customer ID. Nothing is billed between nights.
- Masking: a job copies customer records from the `landing/` zone to `raw/`, replaces emails with a hash and keeps only the last four digits of phone numbers. Analysts can count unique customers but can't see contact details.
- Table versions: a source adds a `discount_code` column; the next crawler run creates version 7 of `orders`. When a report breaks, the team compares versions 6 and 7.

## Related

- [s3.md](../aws-general-services/s3.md): crawlers scan data that lands in S3 and register it as tables; Glue jobs read raw data from S3 and write curated, partitioned Parquet back to it.
- [athena.md](athena.md): Athena queries S3 data through the table definitions the Glue Data Catalog holds. It needs only the catalog; crawlers and jobs are optional, added when schemas change or data needs cleaning.
- [choosing-delivery-services.md](../../aws-data-engineering/choosing-delivery-services.md): compares Glue with Athena (Glue makes data better, Athena answers questions about it) and gives how much Glue an Athena setup needs.
- [emr.md](emr.md): EMR also reads the Glue Data Catalog, and both run Apache Spark; EMR is the choice when you need cluster control or other frameworks.
- [lake-formation.md](lake-formation.md): Lake Formation applies its fine-grained permissions to Data Catalog resources (databases, tables, columns), so the catalog is the anchor for governance.
- [datazone.md](datazone.md): the Data Catalog holds technical metadata; DataZone holds the full business glossary on top of it.
- [lambda.md](../aws-compute/lambda.md): Lambda handles small, event-driven tasks; a Glue job takes over for big transformations that would time out in Lambda's 15 minutes.
- [step-functions.md](../aws-application-coordination/step-functions.md): Step Functions can start Glue crawlers and jobs as steps of a larger workflow; Glue workflows only chain Glue components.
- [kms.md](../aws-security/kms.md): Glue security configurations use KMS keys to encrypt job output, logs, bookmarks and the Data Catalog.
- [aws-data-pipeline.md](../../aws-data-engineering/aws-data-pipeline/aws-data-pipeline.md): Glue appears in stages 1 (ingest jobs), 3 (crawlers and the Data Catalog) and 4 (ETL), and in five of the six data engineer functions.
- [modern-data-architecture.md](../../../data-engineering/modern-data-architecture.md): Glue jobs perform the types of transformation listed here (type conversion, filtering, aggregation, standardization, normalizing), and the Data Catalog implements the catalog concept.
- [choosing-storage-and-processing-services.md](../../aws-data-engineering/choosing-storage-and-processing-services.md): compares Glue with EMR and EMR Serverless: Glue is serverless, ETL-first and integrated with crawlers, the catalog, a visual editor and data quality; EMR gives control and more frameworks.
- [choosing-orchestration-services.md](../../aws-data-engineering/choosing-orchestration-services.md): compares Glue workflows with Step Functions and MWAA (Glue workflows only chain Glue crawlers and jobs), and a Glue job with Lambda (Glue for heavy, long-running ETL).
- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares the Data Catalog with DataZone (technical vs business metadata), and Glue sensitive data detection with Macie (masking PII during a job vs finding PII at rest in S3).
- [zero-etl-and-serverless-on-aws.md](../../aws-data-engineering/zero-etl-and-serverless-on-aws.md): Glue is the serverless ETL option, replacing ETL on EMR clusters.
- [dms.md](../aws-databases/dms.md): DMS can populate the Glue Data Catalog automatically with the tables it writes to S3.
- [partitioning.md](../../../data-engineering/partitioning.md): a catalog table's partition keys implement partitioning, with one partition per S3 path, and crawlers detect that structure automatically.
- [iam.md](../aws-identity/iam.md): each crawler runs with an IAM role that grants it access to the data it scans, and each job runs as its own scoped role.
- [example-corp-pipeline-on-aws.md](../../aws-data-engineering/aws-data-pipeline/example-corp-pipeline-on-aws.md): its catalog section is a worked example of a Glue database and three crawlers over a raw zone.
