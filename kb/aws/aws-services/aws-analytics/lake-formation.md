# AWS Lake Formation

This file covers Lake Formation: building and governing a data lake on S3 with fine-grained permissions.

## What it is

Lake Formation **centrally manages and scales fine-grained data access permissions** on the data lake, and lets you share data with confidence **within and outside** your organization. It builds and governs a lake on S3; the data stays in your S3 buckets. It is the main service for function 6 of the data engineer (ensure data quality, security and compliance), and the service the data security officer uses for fine-grained access and masking.

## Characteristics

- Both a security and a governance service, used in the store, catalog and deliver stages.
- Grants access to **data in the catalog**: databases, tables, **columns, rows and cells**, plus **tag-based access control**.
- **Lake Formation permissions are applied to [Glue Data Catalog](glue.md) resources**, so the catalog is also the anchor for governance.
- Works **together with [IAM](../aws-identity/iam.md)**: IAM lets a user reach the services, and Lake Formation decides which data they see.
- Shares tables **across accounts**.
- Every data access through Lake Formation is **logged in [CloudTrail](../aws-monitoring/cloudtrail.md)**, so you know who queried which table.
- Course (auditability): **automatically catalogs the source and destination** of data in the Glue Data Catalog, giving metadata about the **origin, landing location and transformations** of the data.
- **Course correction:** the course overstates "automatically catalogs… transformations". Lake Formation records **where tables live** and controls access. Full **lineage** (which job produced which table) is a feature of [Amazon DataZone](datazone.md) / SageMaker Catalog.
- Best practice: **classify data** by sensitivity, with Lake Formation tags per class.

## Example

Analysts in marketing can query the `customers` table in Athena but only see the `country` and `segment` columns, and only rows where `region = 'EU'`. CloudTrail logs every query they run against it.

## Related

- [glue.md](glue.md): Lake Formation permissions are applied to Glue Data Catalog resources (databases, tables, columns), so it governs the tables the catalog defines.
- [s3.md](../aws-general-services/s3.md): Lake Formation builds and governs a data lake on S3; the data stays in your S3 buckets.
- [iam.md](../aws-identity/iam.md): IAM lets a user reach the services (for example call Athena), and Lake Formation then decides which databases, tables, columns and rows that user sees.
- [cloudtrail.md](../aws-monitoring/cloudtrail.md): every data access through Lake Formation is logged in CloudTrail, which shows who queried which table.
- [datazone.md](datazone.md): DataZone adds self-service sharing and the business glossary, and provides the full lineage the course attributes to Lake Formation.
- [athena.md](athena.md): when analysts query through Athena, Lake Formation filters the columns and rows they're allowed to see (as in this file's example).
- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares Lake Formation with IAM and resource policies: IAM grants access to services and API actions, resource policies lock down a resource or allow cross-account access, and Lake Formation grants database, table, column, row and cell access to lake data.
- [store-on-aws.md](../../aws-data-engineering/aws-data-pipeline/store-on-aws.md): Lake Formation is one of the services that build and govern a lake on S3, and a security and governance service in the store, catalog and deliver stages.
- [modern-data-architecture.md](../../../data-engineering/modern-data-architecture.md): Lake Formation provides the end-to-end governance that a modern data architecture adds on top of the lake and its catalog.
- [data-personas.md](../../../data-engineering/data-personas.md): Lake Formation is the data security officer's tool for fine-grained access control and masking.
