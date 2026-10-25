# Amazon Athena

This file covers Amazon Athena: what it is, how it queries S3 in place, how it's priced, and an example.

## What it is

Athena queries large datasets **directly on S3** with **standard SQL**. The data doesn't need to be extracted and loaded anywhere else first, which makes Athena a **zero-ETL** service. In the pipeline it's a **delivery** service, and its typical users are analysts and engineers running ad hoc queries _(added)_.

## Characteristics

- Queries formats such as **CSV, Parquet and ORC**, plus JSON and others _(added)_.
- Reads table definitions from the [Glue Data Catalog](glue.md), so you define a table once and query it from Athena, EMR or Redshift Spectrum _(added)_.
- **Needs only S3 and the catalog.** You can define a table yourself in Athena with `CREATE EXTERNAL TABLE … LOCATION 's3://…'`. Athena has no catalog of its own, so that definition is stored in the Glue Data Catalog, but no crawler or Glue job is involved. This suits data with a known, stable format, such as AWS logs _(added)_.
- **CTAS** (`CREATE TABLE AS SELECT`) writes a query's results to S3 as new files, including as Parquet, and registers them as a table. Athena can do light transformations this way; heavy, scheduled ETL belongs in a Glue job _(added)_.
- Can also use an external Apache Hive metastore instead of the Glue Data Catalog. It's rare, mostly where a company already runs Hive _(added; verify)_.
- **Serverless:** there's nothing to provision, and you pay **per TB of data scanned** by each query _(added)_.
- **Parquet/ORC plus partitioning** reduce the data a query scans, which makes queries cheaper and faster. Converting to Parquet in [Data Firehose](data-firehose.md) pays off here _(added)_.
- **Federated query** connectors can also query RDS, DynamoDB and other sources _(added)_.
- [Step Functions](../aws-application-coordination/step-functions.md) can orchestrate Lambda functions that process and analyze Athena query results in real time. Step Functions can also start an Athena query directly _(added)_.
- [EventBridge](../aws-application-coordination/eventbridge.md) can route events to Athena to run SQL queries.

## Example

_(added)_ A security analyst wants the IP addresses with the most 403 errors from the load balancer last week. The ALB access logs are already in S3. Their format is fixed, so the analyst describes them once in Athena, with no crawler:

```sql
CREATE EXTERNAL TABLE alb_logs (client_ip string, status int, ...)
PARTITIONED BY (day string)
LOCATION 's3://my-logs/alb/';
```

Then they run one query:

```sql
SELECT client_ip, COUNT(*) AS errors
FROM alb_logs
WHERE status = 403 AND day BETWEEN '2026-10-11' AND '2026-10-17'
GROUP BY client_ip ORDER BY errors DESC LIMIT 20;
```

The answer comes back in seconds. No pipeline was built, no database was loaded, and no server is running. In a workflow, Step Functions could run this query every morning and pass the results to a Lambda function that blocks the top offenders.

## Related

- [s3.md](../aws-general-services/s3.md): Athena runs SQL directly on the files stored in S3, so the data is queried where it sits instead of being loaded into a database first.
- [glue.md](glue.md): Athena reads its table definitions from the Glue Data Catalog. Tables can come from Athena's own `CREATE TABLE` or from Glue crawlers, and Glue jobs can clean the data into Parquet first; only the catalog is required.
- [choosing-delivery-services.md](../../aws-data-engineering/choosing-delivery-services.md): also compares Athena with Glue (answering questions vs making data better) and gives how much Glue an Athena setup needs.
- [data-firehose.md](data-firehose.md): Firehose can convert streams to Parquet or ORC before writing to S3, which means Athena later scans less data per query and costs less.
- [step-functions.md](../aws-application-coordination/step-functions.md): Step Functions can start an Athena query as a workflow step (for example a nightly row-count check) and pass the results to Lambda.
- [quicksight.md](quicksight.md): QuickSight dashboards are often built on top of Athena queries over S3 data.
- [choosing-delivery-services.md](../../aws-data-engineering/choosing-delivery-services.md): compares Athena with Redshift and Redshift Spectrum: Athena is serverless and billed per data scanned for ad hoc SQL on S3; Redshift is a warehouse tuned for frequent, complex, concurrent queries; Spectrum is the Redshift feature for joining S3 data with warehouse tables.
- [zero-etl-and-serverless-on-aws.md](../../aws-data-engineering/zero-etl-and-serverless-on-aws.md): Athena is one of the five zero-ETL services: it avoids ETL by querying S3 in place.
- [aws-data-pipeline.md](../../aws-data-engineering/aws-data-pipeline.md): Athena is a stage 5 (deliver) service, used by analysts and engineers for ad hoc queries.
- [data-lakes-and-warehouses.md](../../../data-engineering/data-lakes-and-warehouses.md): Athena is the query engine a data lake needs, because the lake (S3) can't query itself; it applies schema-on-read and benefits from the columnar formats described here.
