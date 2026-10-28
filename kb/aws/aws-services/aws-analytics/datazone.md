# Amazon DataZone

This file covers DataZone: the business data catalog and self-service data sharing across teams.

## What it is

DataZone lets you **catalog, discover, share and govern** data across **AWS, on premises and third-party** sources. It's a data catalog and governance service for sharing data across teams, and one of the services for function 6 of the data engineer (ensure data quality, security and compliance).

## Characteristics

- A governance service, used in the catalog and deliver stages.
- Audience is business users across the organization, not engines.
- Holds business metadata: the **business glossary**, descriptions and owners. Technical metadata (schemas, locations, partitions) stays in the [Glue Data Catalog](glue.md).
- Self-service sharing: users **request and approve** access to data products.
- Supports **data mesh** setups.
- Provides **lineage** (which job produced which table) as part of DataZone / SageMaker Catalog.
- Best practice: **define and implement data governance** with data owners per domain, a catalog with business terms, and access requests through DataZone.

## Example

A marketing analyst searches DataZone for "customer lifetime value", finds the data product the finance team published, and requests access. The finance data owner approves, and the analyst can query it without a ticket to the data team.

## Related

- [glue.md](glue.md): DataZone holds the business metadata (glossary, descriptions, owners) on top of the technical metadata (schemas, locations, partitions) that stays in the Glue Data Catalog.
- [lake-formation.md](lake-formation.md): both govern data access; Lake Formation enforces fine-grained permissions on catalog tables, while DataZone adds self-service request-and-approve sharing of data products for business users. Lineage the course attributes to Lake Formation actually lives in DataZone / SageMaker Catalog.
- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares DataZone with the Glue Data Catalog: the Data Catalog serves engines and engineers with technical metadata in AWS; DataZone serves business users with a business glossary and self-service sharing across AWS, on premises and third-party sources.
- [modern-data-architecture.md](../../../data-engineering/modern-data-architecture.md): DataZone implements the business side of the data catalog concept described here (business glossary, owners, descriptions for people), while the Glue Data Catalog implements the technical side.
- [data-engineer-role.md](../../../data-engineering/data-engineer-role.md): DataZone is one of the AWS services for function 6, ensuring data quality, security and compliance.
