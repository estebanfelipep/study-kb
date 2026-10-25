# AWS Glue

AWS Glue: serverless data integration, covering jobs, crawlers, the Data Catalog, workflows, Glue Studio, Data Quality and sensitive data detection.

## What it is

AWS Glue is a serverless data integration service and a fully managed ETL service. It prepares and cleanses data from various sources, classifies data, extracts schema and populates data catalogs. It appears in five of the six data engineer functions (infrastructure, ingest, prepare, catalog, automate) and across the whole flow: jobs for ingestion, crawlers and the Data Catalog for cataloging, ETL for processing, and workflows for automation. It's the central service of the training.

## Characteristics

- **Serverless:** jobs scale automatically; you don't manage infrastructure and pay only per use.
- Part of the **security and auditability** story: KMS encryption, data masking, and the Data Catalog's table history.

### Jobs

- Ingest and transform data. Run on **Apache Spark**, or **Python shell** for small tasks (also Ray). _(added)_
- Capacity is measured in **DPUs** (data processing units), billed per second while a job runs. _(added)_
- Mostly batch; also **streaming ETL**. _(added)_
- **Job bookmarks** remember what was already processed, so each run handles only new data. _(added)_
- Connectors to many sources. _(added)_
- Run for hours on GB to TB of data (distributed Spark), so they suit transformations that would time out in [Lambda](../aws-compute/lambda.md). _(added)_

### Crawlers

- Scan data, determine the format and schema, group data into tables, and write the metadata to the Data Catalog.
- Flow: data lands in S3 → crawlers catalog it → it becomes discoverable and queryable.
- Update schemas and partitions automatically as new data arrives. _(added)_
- Used in discovery step 5 to extract relevant data (or custom scripts).

### Data Catalog

- Central metadata store: table definitions, schemas, tags. Creates a catalog of metadata about your stored assets.
- Lets you search and find relevant data sources by attributes such as name, owner, business terms and others.
- Stores the **table definition and physical location** of a dataset, and lets you add business-relevant attributes.
- **Tracks how data has changed over time**, including metadata changes as data moves between stores such as S3 and Redshift. This helps trace the flow of data.
- Keeps **table versions**: each schema change creates a new version you can compare or roll back to. _(added)_
- **Stores metadata, not the data.** The data stays in S3; the catalog holds table definitions that point to it. _(added)_
- **One catalog, many engines:** [Athena](athena.md), [EMR](emr.md), Redshift Spectrum and Glue jobs all read table definitions from it. Compatible with the **Apache Hive metastore**. _(added)_
- [Lake Formation](lake-formation.md) permissions are applied to Data Catalog resources (databases, tables, columns), so the catalog is the anchor for governance. _(added)_
- Supports owners, descriptions and custom table properties; the full business glossary lives in [DataZone](datazone.md). _(added)_
- The catalog and connection passwords can be encrypted with KMS. _(added)_
- For the catalog concept (single source of truth, data swamp), see [modern-data-architecture.md](../../../data-engineering/modern-data-architecture.md).

### Workflows

- Orchestrate a chain of Glue crawlers, jobs and triggers. Only Glue; serverless. _(added: defined in the Glue console or API)_

### Glue Studio _(added)_

- The visual editor for building ETL jobs. It answers discovery step 5's "Do you have a visual editor?"

### Data Quality _(added)_

- Rules that check data in a job, for example failing the job when too many rows break a rule.

### Sensitive data protection

- Protects sensitive data with **encryption with KMS** and **data masking**.
- **Security configurations** encrypt job output in S3, CloudWatch logs and job bookmarks with KMS. _(added)_
- **Sensitive data detection** finds PII in a job's data while the job processes it, and can **redact, hash or partially mask** it. _(added)_

## Example

- _(added)_ Nightly ETL: a Glue job reads only new JSON order files from S3 (job bookmarks), joins them with the customer table from the Data Catalog, drops test orders, standardizes country codes, and writes partitioned Parquet back to S3. A data-quality rule fails the job if more than 1% of orders have no customer ID. Nothing is billed between nights.
- _(added)_ Masking: a job copies customer records from `raw/` to `curated/`, replaces emails with a hash and keeps only the last four digits of phone numbers. Analysts can count unique customers but can't see contact details.
- _(added)_ Table versions: a source adds a `discount_code` column; the next crawler run creates version 7 of `orders`. When a report breaks, the team compares versions 6 and 7.

## Related

- [s3.md](../aws-general-services/s3.md): crawlers scan data that lands in S3 and register it as tables; Glue jobs read raw data from S3 and write curated, partitioned Parquet back to it.
- [athena.md](athena.md): Athena queries S3 data through the table definitions the Glue Data Catalog holds.
- [emr.md](emr.md): EMR also reads the Glue Data Catalog, and both run Apache Spark; EMR is the choice when you need cluster control or other frameworks.
- [lake-formation.md](lake-formation.md): Lake Formation applies its fine-grained permissions to Data Catalog resources (databases, tables, columns), so the catalog is the anchor for governance.
- [datazone.md](datazone.md): the Data Catalog holds technical metadata; DataZone holds the full business glossary on top of it.
- [lambda.md](../aws-compute/lambda.md): Lambda handles small, event-driven tasks; a Glue job takes over for big transformations that would time out in Lambda's 15 minutes.
- [step-functions.md](../aws-application-coordination/step-functions.md): Step Functions can start Glue crawlers and jobs as steps of a larger workflow; Glue workflows only chain Glue components.
- [kms.md](../aws-security/kms.md): Glue security configurations use KMS keys to encrypt job output, logs, bookmarks and the Data Catalog.
- [aws-data-pipeline.md](../../aws-data-engineering/aws-data-pipeline.md): Glue appears in stages 1 (ingest jobs), 3 (crawlers and the Data Catalog) and 4 (ETL), and in five of the six data engineer functions.
- [modern-data-architecture.md](../../../data-engineering/modern-data-architecture.md): Glue jobs perform the types of transformation listed here (type conversion, filtering, aggregation, standardization, normalizing), and the Data Catalog implements the catalog concept.
- [choosing-storage-and-processing-services.md](../../aws-data-engineering/choosing-storage-and-processing-services.md): compares Glue with EMR and EMR Serverless: Glue is serverless, ETL-first and integrated with crawlers, the catalog, a visual editor and data quality; EMR gives control and more frameworks.
- [choosing-orchestration-services.md](../../aws-data-engineering/choosing-orchestration-services.md): compares Glue workflows with Step Functions and MWAA (Glue workflows only chain Glue crawlers and jobs), and a Glue job with Lambda (Glue for heavy, long-running ETL).
- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares the Data Catalog with DataZone (technical vs business metadata), and Glue sensitive data detection with Macie (masking PII during a job vs finding PII at rest in S3).
- [zero-etl-and-serverless-on-aws.md](../../aws-data-engineering/zero-etl-and-serverless-on-aws.md): Glue is the serverless ETL option, replacing ETL on EMR clusters.
