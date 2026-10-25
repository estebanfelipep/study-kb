# Choosing delivery services

This file holds the comparisons and exam pick-rules for serving data to consumers: querying, warehousing, search, dashboards and ML.

All content here is _(added)_ general knowledge. Service details are in each service's file in [aws-services](../aws-services/aws-services.md).

## If the question says… pick

| If the question says… | Pick |
| --- | --- |
| "Ad hoc SQL on S3", "serverless", "pay per query", "no infrastructure" | [Athena](../aws-services/aws-analytics/athena.md) |
| "Data warehouse", "complex queries on petabytes", "BI with high concurrency", "join warehouse and lake data" | [Redshift](../aws-services/aws-analytics/redshift.md) |
| "Spark/Hive/Presto", "big data frameworks", "full control" | [EMR](../aws-services/aws-analytics/emr.md) |
| "Full-text search", "log analytics", "near real-time dashboards on logs" | [OpenSearch](../aws-services/aws-databases/opensearch-service.md) |
| "Dashboards", "visualize", "business users", "BI tool" | [QuickSight](../aws-services/aws-analytics/quicksight.md) |
| "Train a model", "predictions", "ML" | [SageMaker](../aws-services/aws-ai/sagemaker.md) |

## Athena vs Redshift

Both use SQL. **Athena** is serverless, has nothing to provision, charges per query by data scanned, and suits ad hoc questions. **Redshift** is a provisioned or serverless warehouse tuned for frequent, complex and concurrent queries.

## Athena vs Redshift Spectrum

Both run SQL on files in S3.

- **Athena** is standalone and serverless. Use it for ad hoc queries.
- **Spectrum** is a feature of Redshift. It needs a Redshift cluster or workgroup, and you use it to **join S3 data with tables already in the warehouse**.

## OpenSearch zero-ETL with S3 vs Athena

Both query logs in S3.

- **OpenSearch direct query:** your team already lives in **OpenSearch Dashboards** and wants hot (indexed) and cold (S3) logs in **one place** for log search and observability.
- **Athena:** general-purpose **SQL analytics** on any S3 data, without needing an OpenSearch domain.

## OpenSearch Serverless vs managed domains

- **Serverless:** no clusters, automatic scaling. Best for variable workloads and teams that don't want to tune OpenSearch.
- **Managed domains:** you choose instance types, counts and storage, with access to more plugins and settings. Best for large, steady workloads that need fine control.

Purpose-built databases by type are listed in [aws-data-pipeline.md](aws-data-pipeline.md).
