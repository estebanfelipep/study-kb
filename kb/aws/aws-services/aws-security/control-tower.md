# AWS Control Tower

This file covers Control Tower: setting up and governing a multi-account AWS environment.

## What it is

Control Tower sets up and operates a **multi-account AWS environment** with **prescriptive controls**. The course lists it under **data and network security**.

## Characteristics

- **Course correction:** it's really an **account governance** service, not a network security one.
- Builds a **landing zone**: an AWS Organizations structure with a log archive account and an audit account.
- **Controls** are either **preventive** (block an action, for example disabling CloudTrail) or **detective** ([Config](../aws-monitoring/config.md) rules that flag issues). Exam material may call controls **guardrails**.
- **Account Factory** creates new accounts that already follow the rules.
- Sits on top of **AWS Organizations** (accounts, organizational units, service control policies) and sets it up with best practices.

## Example

A company separates its analytics into `data-dev`, `data-prod` and `data-sandbox` accounts. Control Tower creates each with [CloudTrail](../aws-monitoring/cloudtrail.md) on, logs centralized in the log archive account, and a control preventing anyone from making S3 buckets public.

## Related

- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares Control Tower with AWS Organizations: Organizations is the underlying service, and Control Tower sets it up with best practices and keeps it governed.
- [exam-traps.md](../../aws-data-engineering/exam-traps.md): course correction: the course lists Control Tower under data and network security, but it's an account governance service. Exam material may call controls guardrails.
- [security-and-monitoring-on-aws.md](../../aws-data-engineering/security-and-monitoring-on-aws.md): Control Tower is a course service for data and network security, and handles account setup and guardrails in the example secured pipeline.
- [config.md](../aws-monitoring/config.md): Control Tower's detective controls are Config rules that flag issues.
- [cloudtrail.md](../aws-monitoring/cloudtrail.md): accounts created by Control Tower have CloudTrail turned on, with logs centralized in the log archive account, and a preventive control can block disabling CloudTrail.
