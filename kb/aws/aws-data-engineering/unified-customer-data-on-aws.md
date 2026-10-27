# Unified customer data on AWS

This file builds the unified customer data example with AWS services, one common way, stage by stage.

All content here is _(added)_: general knowledge from Q&A, not the course notes.

The example itself, with what each step does and why, is in [unified-customer-data.md](../../data-engineering/unified-customer-data.md). This file only names the service for each step.

The **Pipeline stage** column uses the five stages of [modern-data-architecture.md](../../data-engineering/modern-data-architecture.md), so each row can be read against that stage's section there and against the same stage's services in [aws-data-pipeline.md](aws-data-pipeline.md). The **Example step** column is the numbered step in the example's "Following the update, stage by stage", and the rows follow those steps in order. A step with several services takes several rows.

| Pipeline stage                    | Example step | What happens                                          | AWS service                                                                                                                                                               |
| --------------------------------- | ------------ | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source (before the pipeline)      | 1            | Sales writes to the CRM's operational database        | [RDS or Aurora](../aws-services/aws-databases/rds.md), when the CRM's database runs on AWS                                                                                |
| 1. Ingest                         | 2            | CDC from the sales CRM database                       | [DMS](../aws-services/aws-databases/dms.md), full load + CDC to S3                                                                                                        |
| 1. Ingest                         | 2            | Batch loads from the SaaS marketing and support tools | [AppFlow](../aws-services/aws-application-coordination/appflow.md), or [Glue](../aws-services/aws-analytics/glue.md) jobs                                                 |
| 2. Store                          | 3            | Raw zone: every source as it arrived                  | [S3](../aws-services/aws-general-services/s3.md), under a `raw/` prefix                                                                                                   |
| 3. Catalog                        | 4            | Catalog                                               | [Glue](../aws-services/aws-analytics/glue.md) crawlers and the Glue Data Catalog. [DataZone](../aws-services/aws-analytics/datazone.md) adds business-facing discovery    |
| 4. Process                        | 5            | Matching IDs                                          | [Entity Resolution](../aws-services/aws-analytics/entity-resolution.md), or matching logic in a Glue job                                                                  |
| 4. Process                        | 5            | Standardizing, survivorship, building `customer_360`  | [Glue](../aws-services/aws-analytics/glue.md) jobs (Spark)                                                                                                                |
| 2. Store                          | 5            | Curated zone: `customer_360` is written back          | [S3](../aws-services/aws-general-services/s3.md), under a `curated/` prefix. The curated table can be Iceberg on S3 Tables                                                |
| 5. Deliver, with governance       | 6            | Department views with column and row filters          | [Lake Formation](../aws-services/aws-analytics/lake-formation.md)                                                                                                         |
| 5. Deliver                        | 6            | Queries and dashboards                                | [Athena](../aws-services/aws-analytics/athena.md) or [Redshift](../aws-services/aws-analytics/redshift.md), and [QuickSight](../aws-services/aws-analytics/quicksight.md) |
| Across all stages (orchestration) | —            | Chaining ingest → crawl → merge → refresh             | [Step Functions](../aws-services/aws-application-coordination/step-functions.md) or [MWAA](../aws-services/aws-application-coordination/mwaa.md)                          |

## Related

- [unified-customer-data.md](../../data-engineering/unified-customer-data.md): the vendor-neutral example this file implements. It explains each step, and this file names the AWS service for it.
- [aws-data-pipeline.md](aws-data-pipeline.md): the general stage-to-service map. This file applies it to one project, and its Pipeline stage column matches that file's stage sections.
- [modern-data-architecture.md](../../data-engineering/modern-data-architecture.md): defines the five pipeline stages the table's Pipeline stage column is organized by.
- [choosing-ingestion-services.md](choosing-ingestion-services.md): explains why DMS is the pick for the CRM database (CDC) and compares the other ways to get RDS data into S3.
