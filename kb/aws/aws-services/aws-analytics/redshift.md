# Amazon Redshift

Amazon Redshift: the AWS data warehouse, including Spectrum, streaming ingestion, auto copy, zero-ETL targets and Redshift Serverless.

## What it is

Amazon Redshift is a managed, columnar SQL analytics database (a data warehouse). It analyzes large sets of structured data across many databases and datasets without moving the data. In the pipeline it's a delivery service: the curated, heavily queried data goes here for analysts and BI dashboards. It's built for OLAP; see [data-lakes-and-warehouses.md](../../../data-engineering/data-lakes-and-warehouses.md).

## Characteristics

- **Columnar storage:** `SUM(revenue)` reads only that column, and data compresses well. _(added)_
- **MPP** (massively parallel processing): work is spread across nodes; scales from TB to PB. _(added)_
- **Schema-on-write:** tables are defined before loading; data is cleaned and modeled first. _(added)_
- **Tuned for fast, complex SQL at high concurrency**, with features for BI concurrency. _(added)_
- **PostgreSQL-compatible SQL.** _(added)_
- **Cost:** more expensive than S3 per GB (compute plus storage). _(added)_
- **Export:** can export query results back to S3 in open formats. _(added)_
- **Federated query:** queries RDS and Aurora without loading the data. _(added)_
- **Security:** encryption at rest with [KMS](../aws-security/kms.md); run clusters in private subnets of a [VPC](../aws-networking/vpc.md), listening on port 5439; snapshots can be copied to another Region for disaster recovery. _(added)_

### Redshift Spectrum _(added)_

- Runs SQL directly over files in S3 without loading them, so Redshift acts as a query layer over the lake. This is the lake house idea: S3 holds everything, Redshift serves the curated, high-performance part.
- It's a feature of Redshift: it needs a cluster or workgroup. Use it to join S3 data with tables already in the warehouse.
- Reads table definitions from the [Glue Data Catalog](glue.md).

### Streaming ingestion

- Ingests streaming data in **near real time** at high throughput. Data doesn't need to be staged in S3, so some ETL tasks are no longer needed.
- How it works: you create a **materialized view** over a [Kinesis Data Streams](kinesis-data-streams.md) stream or an [MSK](msk.md) topic. Redshift reads directly from the stream when the view refreshes (manually or automatically), within seconds. _(added)_

### Auto copy from S3

- Continuously ingests new data files from S3 with no manual intervention.
- How it works: a **COPY JOB** watches an S3 prefix, loads new files automatically, and remembers which files it already loaded, so nothing is loaded twice. _(added)_
- For files that arrive over time. Streams use streaming ingestion instead. _(added)_

### Zero-ETL target

- [Aurora](../aws-databases/rds.md) zero-ETL integration replicates data to Redshift in near real time. AWS also offers zero-ETL integrations from more sources, such as RDS for MySQL, DynamoDB and some SaaS applications. _(added; verify the current list)_

### Redshift Serverless

- Automatically provisions and scales resources to meet demand. Analytics run without setting up and managing data warehouse infrastructure.
- Capacity is measured in **RPUs** (Redshift Processing Units). You set a base and a maximum, and Redshift scales between them. _(added)_
- Pay per second of compute while queries run, plus storage. No compute charge when idle. _(added)_
- Same SQL and features (Spectrum, streaming ingestion, zero-ETL targets) as provisioned Redshift. _(added)_

## Example

- _(added)_ Click stream: an e-commerce site streams every click to Kinesis Data Streams. A materialized view in Redshift over that stream feeds a live dashboard ("add-to-cart events per product in the last 10 minutes") and joins with the `products` table. No Firehose, no S3 staging, no scheduled load job.
- _(added)_ Auto copy: a payments vendor drops settlement CSVs into `s3://finance-landing/settlements/` at unpredictable times. One COPY JOB replaces a scheduled Lambda function that listed the prefix, tracked files in DynamoDB and ran `COPY`.
- _(added)_ Serverless: a marketing team runs heavy reports on Monday mornings and a few ad hoc queries the rest of the week. With Redshift Serverless they pay for the Monday burst, and capacity scales up when 20 analysts hit it at 9 a.m.

## Related

- [s3.md](../aws-general-services/s3.md): S3 is the lake and Redshift the warehouse; Redshift reads S3 files in place with Spectrum, loads new S3 files with auto copy, and exports results back to S3 (the lake house).
- [kinesis-data-streams.md](kinesis-data-streams.md): Redshift streaming ingestion creates a materialized view over a Kinesis stream and reads it directly, within seconds and with no S3 staging.
- [msk.md](msk.md): streaming ingestion works the same way over an MSK topic.
- [data-firehose.md](data-firehose.md): the alternative way to stream into Redshift: Firehose buffers records, writes them to S3, then runs a `COPY`.
- [rds.md](../aws-databases/rds.md): Aurora is a zero-ETL source that replicates into Redshift in near real time, and federated query lets Redshift query RDS and Aurora without loading the data.
- [glue.md](glue.md): Redshift Spectrum reads its S3 table definitions from the Glue Data Catalog.
- [quicksight.md](quicksight.md): QuickSight serves BI dashboards on top of the curated data in Redshift.
- [kms.md](../aws-security/kms.md): Redshift data is encrypted at rest with KMS keys.
- [vpc.md](../aws-networking/vpc.md): Redshift runs in a private subnet; its security group allows port 5439 only from approved sources, and it reads S3 through a VPC endpoint.
- [data-lakes-and-warehouses.md](../../../data-engineering/data-lakes-and-warehouses.md): Redshift is the AWS implementation of the data warehouse described here: OLAP, columnar, MPP, schema-on-write, and the warehouse half of a lake house.
- [orchestration-and-automation.md](../../../data-engineering/orchestration-and-automation.md): streaming ingestion, auto copy and the Aurora integration are Redshift's forms of the zero-ETL concept.
- [zero-etl-and-serverless-on-aws.md](../../aws-data-engineering/zero-etl-and-serverless-on-aws.md): Redshift appears in three of the five zero-ETL services (streaming ingestion, auto copy, Aurora zero-ETL target), and Redshift Serverless is the serverless warehouse option.
- [choosing-storage-and-processing-services.md](../../aws-data-engineering/choosing-storage-and-processing-services.md): compares Redshift with S3 (warehouse vs lake) and RDS (OLAP vs OLTP), and Redshift Serverless with provisioned Redshift (variable workloads vs steady 24/7 load).
- [choosing-delivery-services.md](../../aws-data-engineering/choosing-delivery-services.md): compares Redshift with Athena (frequent, complex, concurrent queries vs serverless ad hoc SQL) and Spectrum with Athena (joining S3 with warehouse tables vs standalone queries).
- [choosing-ingestion-services.md](../../aws-data-engineering/choosing-ingestion-services.md): compares the ways to load Redshift: streaming ingestion vs Firehose → Redshift, auto copy vs manual `COPY`, and Aurora zero-ETL vs DMS vs a Glue job.
