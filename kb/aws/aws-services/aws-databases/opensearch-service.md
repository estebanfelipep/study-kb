# Amazon OpenSearch Service

This file covers Amazon OpenSearch Service: managed domains, OpenSearch Serverless, and the zero-ETL integration with S3, with examples.

## What it is

OpenSearch Service lets you deploy, operate and scale **OpenSearch** clusters. You analyze data from **Kinesis Data Streams, S3 and DynamoDB** with the OpenSearch APIs. In the pipeline it's a **delivery** service, used for **full-text search**, **log analytics** and near real-time dashboards on logs. Its typical users are engineers and operations teams _(added)_.

Exam material may use the older name **Amazon Elasticsearch Service**.

## Characteristics

### Managed domains _(added)_

- You choose the instance types, instance counts and storage.
- They give access to more plugins and settings, which suits large, steady workloads that need fine control.

### OpenSearch Serverless

- Streamlines running **petabyte-scale search and analytics** workloads. It **automatically provisions and scales** resources, so you don't manage or scale OpenSearch clusters.
- You create **collections** instead of clusters. Each collection has a type _(added)_:
  - **search:** full-text search.
  - **time series:** logs and metrics.
  - **vector search:** embeddings, for semantic search and AI apps.
- Indexing compute and search compute scale separately, measured in **OCUs** (OpenSearch Compute Units). Pricing isn't purely pay-per-query, so check current pricing _(added)_.

### Zero-ETL integration with S3

- OpenSearch Service can **query data directly in S3** without extracting it into OpenSearch, which improves query performance for **log analysis**.
- OpenSearch registers S3 as a **direct query data source**, using table definitions from the [Glue Data Catalog](../aws-analytics/glue.md). You query it from **OpenSearch Dashboards** _(added)_.
- For data you query often, you can build indexes or materialized views over just the parts you need _(added)_.

## Example

- **Direct query on S3** _(added)_: a company keeps the last 7 days of application logs indexed in OpenSearch for fast search, and 2 years of older logs in S3 because indexing them would be too expensive. During an incident, an engineer needs logs from 4 months ago. They run a direct query against the S3 logs from the same OpenSearch Dashboards and correlate the results with recent logs, without re-ingesting anything.
- **Serverless vector search** _(added)_: a help center stores article embeddings in a vector search collection. When a user types "my video keeps stopping", the app finds articles about buffering even though the words don't match. Traffic spikes after a release are absorbed automatically.

## Related

- [kinesis-data-streams.md](../aws-analytics/kinesis-data-streams.md): Kinesis Data Streams is one of the sources OpenSearch analyzes data from.
- [s3.md](../aws-general-services/s3.md): OpenSearch analyzes data from S3, and with the zero-ETL integration it queries logs directly in S3 without ingesting them.
- [dynamodb.md](dynamodb.md): DynamoDB is one of the sources OpenSearch analyzes data from.
- [glue.md](../aws-analytics/glue.md): OpenSearch's direct query on S3 uses the table definitions in the Glue Data Catalog.
- [choosing-delivery-services.md](../../aws-data-engineering/choosing-delivery-services.md): compares OpenSearch direct query with Athena for logs in S3: OpenSearch when the team lives in OpenSearch Dashboards and wants hot and cold logs in one place; Athena for general SQL on any S3 data. It also compares Serverless with managed domains: Serverless for variable workloads with no tuning, managed domains for large, steady workloads that need fine control.
- [zero-etl-and-serverless-on-aws.md](../../aws-data-engineering/zero-etl-and-serverless-on-aws.md): OpenSearch appears twice there: its S3 integration is a zero-ETL service (query in place), and OpenSearch Serverless is the serverless option for search and log analytics.
- [aws-data-pipeline.md](../../aws-data-engineering/aws-data-pipeline.md): OpenSearch is a deliver-stage service, used by engineers and operations for search and logs.
- [exam-traps.md](../../aws-data-engineering/exam-traps.md): exam material may call it Amazon Elasticsearch Service.
