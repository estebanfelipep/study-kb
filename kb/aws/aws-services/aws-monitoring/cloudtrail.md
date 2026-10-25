# AWS CloudTrail

This file covers CloudTrail: logging API calls for audit, security monitoring and data access tracking, including CloudTrail Lake.

## What it is

CloudTrail provides **auditing and logging of API calls and management events** in AWS accounts for security monitoring and compliance. For monitoring, it gives **visibility into API calls** in your account, to **monitor user activity** and troubleshoot **access-related issues**. It belongs to **data auditability**, one of the five security areas, and is the monitoring service for **data access**. It answers "**Who** did what, and when?" _(added)_.

## Characteristics

- **Management events** (create bucket, change a policy, start a Glue job) are logged by default for 90 days in **Event history** _(added)_.
- **Data events** (S3 `GetObject`, Lambda invokes) must be turned on and cost extra. They're what tells you **who read which file** _(added)_.
- A **trail** sends events to S3 for long-term storage. An organization trail covers every account _(added)_.
- **CloudTrail Lake** stores CloudTrail audit events in an AWS-managed store (not your S3) that you query with **SQL** _(added)_.
- Every data access through [Lake Formation](../aws-analytics/lake-formation.md) is logged in CloudTrail _(added)_.
- Feeds [Config](config.md) and [Audit Manager](../aws-security/audit-manager.md), and is analyzed by [GuardDuty](../aws-security/guardduty.md) _(added)_.
- Records whether a call was **denied**, so it helps troubleshoot access problems _(added)_.

## Example

_(added)_ A table in the data lake was deleted overnight. CloudTrail shows a `DeleteTable` call in Glue at 02:14, made by the role `etl-cleanup` from a Lambda function. The cause is a cleanup job with the wrong prefix, not an attacker.

## Related

- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares CloudTrail with CloudWatch and Config: CloudTrail answers "who did what, and when?", CloudWatch "is it slow or failing?", and Config "what did the resource look like, and is it compliant?".
- [security-and-monitoring-on-aws.md](../../aws-data-engineering/security-and-monitoring-on-aws.md): CloudTrail is the course service for data auditability and for monitoring data access, and logs "who did what" in the example secured pipeline.
- [data-security-and-monitoring.md](../../../data-engineering/data-security-and-monitoring.md): CloudTrail implements data auditability, one of the five security areas, by recording who called which API on which data.
- [lake-formation.md](../aws-analytics/lake-formation.md): every data access through Lake Formation is logged in CloudTrail, so you can see who queried which table.
- [config.md](config.md): Config can show which CloudTrail event changed a resource, linking a configuration change to the API call that caused it.
- [audit-manager.md](../aws-security/audit-manager.md): Audit Manager uses CloudTrail logs as evidence for its compliance reports.
- [guardduty.md](../aws-security/guardduty.md): GuardDuty analyzes CloudTrail events with ML and threat intelligence to detect suspicious API activity.
- [kms.md](../aws-security/kms.md): every use of a KMS customer managed key is recorded in CloudTrail.
