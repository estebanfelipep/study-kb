# Functions and personas on AWS

This file maps the data engineer's six functions and the data personas to the AWS services they use.

## Data engineer functions on AWS

The functions are defined in [data-engineer-role.md](../../../data-engineering/data-engineer-role.md).

| # | Function | AWS services named |
| --- | --- | --- |
| 1 | Build and manage data infrastructure and platforms | S3, Glue, Redshift |
| 2 | Ingest data from various sources | Glue jobs, Lambda |
| 3 | Prepare ingested data for analytics | Glue, Apache Spark, EMR |
| 4 | Catalog and document curated datasets | Glue crawlers, Glue Data Catalog |
| 5 | Automate regular workflows and pipelines | Glue workflows, Lambda, Step Functions |
| 6 | Ensure data quality, security and compliance | DataZone, Lake Formation |

**Glue appears in five of the six functions.** Apache Spark is the open-source distributed processing engine that runs under Glue and EMR.

Data discovery step 5 ([data-discovery.md](../../../data-engineering/data-discovery.md)) names **Glue crawlers or custom scripts** to extract data, and **Glue and EMR** to transform it.

## Personas and services

- **Data scientists** → EMR, SageMaker.
- **Analysts** → Athena, Redshift, QuickSight.
- **CDO** → QuickSight dashboards.
- **Data security officer** → PII protection with Macie, fine-grained access and masking with Lake Formation, regulations with Audit Manager.

The personas are defined in [data-personas.md](../../../data-engineering/data-personas.md).

## Related

- [data-engineer-role.md](../../../data-engineering/data-engineer-role.md): defines the six functions this file maps to AWS services.
- [data-personas.md](../../../data-engineering/data-personas.md): defines the personas this file maps to AWS services.
- [glue.md](../../aws-services/aws-analytics/glue.md): Glue is the service behind five of the six functions.
