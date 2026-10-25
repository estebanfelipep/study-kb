# Amazon RDS and Amazon Aurora

Amazon RDS and Aurora: managed relational databases, their role as pipeline sources, and Aurora zero-ETL integration with Redshift.

## What it is

Amazon RDS (Relational Database Service) runs managed relational databases for applications: OLTP workloads. Amazon Aurora is AWS's own engine in the RDS family. In a data pipeline, RDS is usually a **source**: the application writes to it, and data is copied to S3 or Redshift for analytics. It isn't a data lake. For OLTP vs OLAP and why an operational database isn't a lake, see [data-lakes-and-warehouses.md](../../../data-engineering/data-lakes-and-warehouses.md). _(added)_

## Characteristics _(added)_

- **Engines:** MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, plus Aurora.
- **Workload:** many small, fast reads and writes on a few rows ("get order #123"); thousands of small concurrent transactions; ACID transactions across tables, joins, flexible queries.
- **Row-based storage:** one record is fast to fetch, but summing one column reads every full row.
- **Scale:** GB to a few TB per instance, capped at tens of TB. Scale up plus read replicas. You choose instance sizes, except Aurora Serverless.
- **Cost:** a running instance plus provisioned storage, used or not.
- **Schema-on-write:** data must fit tables before it's written. JSON columns exist, but unstructured data only fits as binary blobs, which is an anti-pattern.
- **Not for BI:** large analytical queries compete with application traffic, row storage is wasteful for aggregates, and a single node can't parallelize a scan of billions of rows.
- **Usually one database per application**, a silo by design.
- **Getting data out:** [Glue](../aws-analytics/glue.md), [DMS](dms.md) or zero-ETL integration copies it to S3 and/or [Redshift](../aws-analytics/redshift.md). Redshift federated query and Athena federated query can also read it in place.
- Encryption at rest with [KMS](../aws-security/kms.md); Multi-AZ for availability.

### Aurora zero-ETL integration with Redshift

- Replicates data from some Aurora sources to Redshift in **near real time** for analytics, with no complex ETL pipelines to build and maintain. Check current Aurora documentation for the supported sources.
- How it works: you create an integration between an Aurora cluster and a Redshift warehouse. AWS replicates the initial data and then every insert, update and delete, typically within seconds. No code, no scheduled jobs. _(added)_
- No transformation in flight; you model the data later in Redshift. _(added)_
- AWS also offers zero-ETL integrations from RDS for MySQL and other sources. _(added; verify the current list)_

## Example

- _(added)_ The flow: the app writes to RDS (OLTP); Glue, DMS or zero-ETL copies the data to S3 and/or Redshift; analysts query Redshift (OLAP) without touching the production database.
- _(added)_ An online store runs on Aurora MySQL. A nightly Glue job used to copy tables to Redshift, so dashboards were a day old and the job broke when someone added a column. With zero-ETL integration, new orders appear in Redshift within seconds, the finance dashboard shows today's revenue, and heavy analytical queries don't slow the app.

## Related

- [redshift.md](../aws-analytics/redshift.md): RDS runs the app (OLTP) and Redshift analyzes the data (OLAP). Aurora zero-ETL replicates Aurora data into Redshift within seconds, and Redshift federated query can read RDS in place.
- [dms.md](dms.md): DMS copies RDS data to S3 or Redshift by full load or ongoing CDC.
- [glue.md](../aws-analytics/glue.md): a Glue job can copy RDS tables to S3 or Redshift in batch. The example's nightly Glue job is what zero-ETL replaces.
- [data-lakes-and-warehouses.md](../../../data-engineering/data-lakes-and-warehouses.md): RDS is the OLTP database in the OLTP vs OLAP concept, and the example of why an operational database isn't a data lake.
- [choosing-storage-and-processing-services.md](../../aws-data-engineering/choosing-storage-and-processing-services.md): compares RDS with Redshift (row-based OLTP vs columnar MPP OLAP), checks RDS against each data lake requirement (it fails most), and compares RDS/Aurora with DynamoDB.
- [choosing-ingestion-services.md](../../aws-data-engineering/choosing-ingestion-services.md): compares Aurora zero-ETL with DMS and a Glue job: zero-ETL is no-code and seconds of latency for supported pairs; DMS for migrations; Glue for heavy transformation.
- [zero-etl-and-serverless-on-aws.md](../../aws-data-engineering/zero-etl-and-serverless-on-aws.md): Aurora zero-ETL integration is one of the zero-ETL services, as managed near real-time replication from Aurora to Redshift.
