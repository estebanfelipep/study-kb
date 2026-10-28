# AWS Identity and Access Management (IAM)

This file covers IAM: identities, policies, least privilege, and its role in securing a data pipeline.

## What it is

IAM manages **fine-grained access and permissions** for human users, software users, other services and microservices. It is the main service for **access management**, one of the five security areas, and applies **granular permissions per user or group using policies**. In a data pipeline, every job, function and analyst reaches AWS services through IAM.

## Characteristics

- Used in **every stage** of the pipeline; a security service rather than a governance one.
- Building blocks: **users** (long-term credentials, best avoided for people), **groups**, **roles** (temporary credentials, assumed by services, apps or federated users) and **policies** (JSON documents that allow or deny actions on resources).
- Grants access to AWS **services and API actions**, such as `s3:GetObject` on a bucket. Granularity is bucket, prefix or object. Column, row and cell access to data is [Lake Formation](../aws-analytics/lake-formation.md)'s job; the two work together.
- **Least privilege:** grant only what's needed. A Glue job role should read one bucket prefix and write another, not `s3:*`.
- **Explicit deny always wins** over any allow.
- People should sign in through **IAM Identity Center** (SSO) rather than as IAM users.
- Also used for **data access** monitoring, through permissions and access logs, alongside [CloudTrail](../aws-monitoring/cloudtrail.md) and [GuardDuty](../aws-security/guardduty.md).
- Best practice: **implement robust access control** by creating IAM roles and policies that control who can access which resources.

## Example

A Glue ETL job runs as the role `glue-sales-etl`. Its policy allows `s3:GetObject` on `s3://raw/sales/*`, `s3:PutObject` on `s3://cleaned/sales/*`, and `kms:Decrypt` on the raw bucket's key. Nothing else. If the job is compromised, it can't touch HR data.

## Related

- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares IAM with Lake Formation (service actions on buckets vs columns, rows and cells of data) and with resource policies (attached to identities vs to the resource, for cross-account access).
- [security-and-monitoring-on-aws.md](../../aws-data-engineering/security-and-monitoring-on-aws.md): IAM is the course service for access management and for monitoring data access, and implements the "robust access control" best practice.
- [data-security-and-monitoring.md](../../../data-engineering/data-security-and-monitoring.md): IAM implements access management, one of the five security areas, with granular permissions per user or group using policies.
- [lake-formation.md](../aws-analytics/lake-formation.md): IAM lets a user reach the services, and Lake Formation decides which data (columns, rows, cells) they see. They work together.
- [kms.md](../aws-security/kms.md): a Glue job role's IAM policy includes `kms:Decrypt` on the raw bucket's key so it can read encrypted data.
- [cloudtrail.md](../aws-monitoring/cloudtrail.md): for data access monitoring, IAM sets the permissions and CloudTrail logs how they're used, including denied calls.
- [glue.md](../aws-analytics/glue.md): each Glue job runs as its own IAM role, scoped to the bucket prefixes it reads and writes (least privilege).
