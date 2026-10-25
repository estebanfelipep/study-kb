# Unified customer data on AWS

This file builds the unified customer data example with AWS services, one common way, stage by stage.

All content here is _(added)_: general knowledge from Q&A, not the course notes.

The example itself, with what each step does and why, is in [unified-customer-data.md](../../data-engineering/unified-customer-data.md). This file only names the service for each step.

| Step | AWS service |
| --- | --- |
| CDC from the sales CRM database | [DMS](../aws-services/aws-databases/dms.md), full load + CDC to S3 |
| Batch loads from the SaaS marketing and support tools | [AppFlow](../aws-services/aws-application-coordination/appflow.md), or [Glue](../aws-services/aws-analytics/glue.md) jobs |
| Raw and curated zones | [S3](../aws-services/aws-general-services/s3.md), with `raw/` and `curated/` prefixes. The curated table can be Iceberg on S3 Tables |
| Catalog | [Glue](../aws-services/aws-analytics/glue.md) crawlers and the Glue Data Catalog. [DataZone](../aws-services/aws-analytics/datazone.md) adds business-facing discovery |
| Matching IDs | [Entity Resolution](../aws-services/aws-analytics/entity-resolution.md), or matching logic in a Glue job |
| Standardizing, survivorship, building `customer_360` | [Glue](../aws-services/aws-analytics/glue.md) jobs (Spark) |
| Department views with column and row filters | [Lake Formation](../aws-services/aws-analytics/lake-formation.md) |
| Queries and dashboards | [Athena](../aws-services/aws-analytics/athena.md) or [Redshift](../aws-services/aws-analytics/redshift.md), and [QuickSight](../aws-services/aws-analytics/quicksight.md) |
| Chaining ingest → crawl → merge → refresh | [Step Functions](../aws-services/aws-application-coordination/step-functions.md) or [MWAA](../aws-services/aws-application-coordination/mwaa.md) |

## Related

- [unified-customer-data.md](../../data-engineering/unified-customer-data.md): the vendor-neutral example this file implements. It explains each step, and this file names the AWS service for it.
- [aws-data-pipeline.md](aws-data-pipeline.md): the general stage-to-service map. This file applies it to one project.
- [choosing-ingestion-services.md](choosing-ingestion-services.md): explains why DMS is the pick for the CRM database (CDC) and compares the other ways to get RDS data into S3.
