# aws-identity — index

Permission and identity management.

## How to read this folder

- **Before:** Least privilege, in [data-security-and-monitoring.md](../../../data-engineering/data-security-and-monitoring.md).
- **Order:** Read early: every pipeline job runs under an IAM role.
- **After:** [lake-formation.md](../aws-analytics/lake-formation.md), for finer access on top of IAM.

## Files

- [iam.md](iam.md): IAM users, groups, roles and policies, least privilege, and how IAM secures pipeline jobs. Read when: you need how a job or user gets permission to call AWS services.
