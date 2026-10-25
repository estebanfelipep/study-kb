# Security and monitoring on AWS

This file maps the five security areas, the security and monitoring best practices, and the monitoring aspects to AWS services, with an example secured and monitored pipeline. The concepts are in [data-security-and-monitoring.md](../../data-engineering/data-security-and-monitoring.md).

## Security areas and services

The course notes that **services can belong to more than one area**, and that the list is partial.

| Area | Course services |
| --- | --- |
| **Access management** | [IAM](../aws-services/aws-identity/iam.md), [ACM](../aws-services/aws-apis/acm.md) |
| **Regulatory compliance** | [Audit Manager](../aws-services/aws-security/audit-manager.md), [AWS Config](../aws-services/aws-monitoring/config.md) |
| **Sensitive data protection** | [Macie](../aws-services/aws-security/macie.md), [KMS](../aws-services/aws-security/kms.md), [Glue](../aws-services/aws-analytics/glue.md) |
| **Data and network security** | [VPC](../aws-services/aws-networking/vpc.md), [Control Tower](../aws-services/aws-security/control-tower.md), [GuardDuty](../aws-services/aws-security/guardduty.md), [WAF](../aws-services/aws-security/waf.md), [Shield](../aws-services/aws-security/shield.md) |
| **Data auditability** | [CloudTrail](../aws-services/aws-monitoring/cloudtrail.md), [Lake Formation](../aws-services/aws-analytics/lake-formation.md), [Glue Data Catalog](../aws-services/aws-analytics/glue.md) |

## Security best practices on AWS

| Practice | AWS implementation | Example _(added)_ |
| --- | --- | --- |
| **Implement robust access control** | **IAM roles and policies** | Each Glue job gets its own role, scoped to its own bucket prefixes |
| **Encrypt data at rest and in transit** | **KMS** for data at rest; **HTTPS/TLS** for data in transit | Default bucket encryption with a customer managed key; a bucket policy that denies non-HTTPS requests |
| **Use data masking** | Masking and anonymization | Hash emails in the curated layer so analysts can count unique customers |
| **Use network isolation** | A **VPC and network ACLs** | Redshift in a private subnet, S3 reached through a VPC endpoint |
| **Understand applicable laws** | Make the architecture conform | EU customer data stays in an EU Region for GDPR |
| **Classify data** | Classes by sensitivity | Public / internal / confidential / restricted, with Lake Formation tags per class |
| **Plan for disaster recovery** | Backups and high availability | S3 cross-Region replication; Redshift snapshots copied to another Region |
| **Define and implement data governance** | Governance policies | Data owners per domain, a catalog with business terms, access requests through DataZone |

Further reading: *Security* in the **Data Analytics Lens** of the AWS Well-Architected Framework.

## Monitoring aspects and services

| Aspect | Services |
| --- | --- |
| **Resources** | [CloudWatch](../aws-services/aws-monitoring/cloudwatch.md), [Systems Manager](../aws-services/aws-monitoring/systems-manager.md) |
| **Analytics jobs** | [CloudWatch](../aws-services/aws-monitoring/cloudwatch.md) |
| **Data pipelines** (Glue, Step Functions, Lambda) | [CloudWatch](../aws-services/aws-monitoring/cloudwatch.md), [X-Ray](../aws-services/aws-monitoring/x-ray.md) |
| **Data access** | [IAM](../aws-services/aws-identity/iam.md), [CloudTrail](../aws-services/aws-monitoring/cloudtrail.md), [GuardDuty](../aws-services/aws-security/guardduty.md) |

For a **single view of overall system health**, the course recommends integrating monitoring with visualization tools: [Managed Grafana](../aws-services/aws-monitoring/managed-grafana.md) and [QuickSight](../aws-services/aws-analytics/quicksight.md).

### Monitoring best practices on AWS _(added: examples)_

- **Test and validate jobs:** run the new Glue job version on a sample in a dev account and compare row counts with the old version.
- **Alert on critical failures:** a Glue job failure event → EventBridge → SNS → the on-call channel.
- **Visualize:** one Managed Grafana dashboard for the full pipeline.

## Example: a secured and monitored pipeline _(added)_

```
Partners ──HTTPS (ACM cert)──▶ API Gateway ◀── WAF + Shield
                                    │
                                    ▼
                                 Lambda
                                    │
                                    ▼
          S3 raw/  (KMS encrypted, private, Macie scans)
                                    │
                                    ▼
          Glue job (IAM role, masks PII)
                                    │
                                    ▼
          S3 curated/ ──▶ Glue Data Catalog
                          (Lake Formation permissions)
                                    │
                                    ▼
          Athena / Redshift (private subnet)
                                    │
                                    ▼
                               QuickSight

Across everything:
  CloudTrail ─── who did what
  Config ─────── is it compliant
  GuardDuty ──── threats
  CloudWatch ─── metrics, logs, alarms ──▶ SNS ──▶ on-call
  X-Ray ──────── request traces (API → Lambda)
  Managed Grafana ── one pipeline dashboard
  Control Tower ──── account setup, guardrails
```

Which service answers which security or monitoring question is in [choosing-security-and-monitoring-services.md](choosing-security-and-monitoring-services.md).
