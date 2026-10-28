# Choosing security and monitoring services

This file holds the comparisons and exam pick-rules for access control, encryption, compliance, threat detection, network protection, auditing and monitoring.

Service details are in each service's file in [aws-services](../aws-services/aws-services.md). The area-to-service map is in [security-and-monitoring-on-aws.md](security-and-monitoring-on-aws.md).

## Which service answers which question

| Question | Service |
| --- | --- |
| Who can access this? | [IAM](../aws-services/aws-identity/iam.md), [Lake Formation](../aws-services/aws-analytics/lake-formation.md) |
| Who did this action? | [CloudTrail](../aws-services/aws-monitoring/cloudtrail.md) |
| What did this resource look like, and is it compliant? | [AWS Config](../aws-services/aws-monitoring/config.md) |
| Can I prove compliance to an auditor? | [Audit Manager](../aws-services/aws-security/audit-manager.md) |
| Where is my PII? | [Macie](../aws-services/aws-security/macie.md) |
| Is someone attacking my account? | [GuardDuty](../aws-services/aws-security/guardduty.md) |
| Is the job slow or failing? | [CloudWatch](../aws-services/aws-monitoring/cloudwatch.md) |
| Which part of the request is slow? | [X-Ray](../aws-services/aws-monitoring/x-ray.md) |
| How do I fix or patch many instances? | [Systems Manager](../aws-services/aws-monitoring/systems-manager.md) |
| How do I encrypt data at rest? | [KMS](../aws-services/aws-security/kms.md) |
| How do I serve HTTPS? | [ACM](../aws-services/aws-apis/acm.md) |
| How do I block web attacks? | [WAF](../aws-services/aws-security/waf.md) |
| How do I survive a DDoS attack? | [Shield](../aws-services/aws-security/shield.md) |
| How do I govern many accounts? | [Control Tower](../aws-services/aws-security/control-tower.md) |

## If the question says… pick (governance)

| If the question says… | Pick |
| --- | --- |
| "Column-level or row-level access to the data lake", "share tables across accounts" | **Lake Formation** |
| "Grant a service or user permission to call an API", "least privilege" | **IAM** |
| "Encrypt data at rest", "manage or rotate keys", "customer managed keys" | **KMS** |
| "Find PII in S3", "classify sensitive data" | **Macie** |
| "Business data catalog", "self-service data sharing between teams", "data mesh" | [DataZone](../aws-services/aws-analytics/datazone.md) |
| "Prove compliance", "collect audit evidence", "assess against PCI, HIPAA, GDPR" | **Audit Manager** |

## Access control

### IAM vs Lake Formation

|  | **IAM** | **Lake Formation** |
| --- | --- | --- |
| Grants access to | AWS **services and API actions** (for example, `s3:GetObject` on a bucket) | **Data in the catalog**: databases, tables, **columns, rows and cells** |
| Granularity | Bucket, prefix or object | Column, row, cell |
| Typical question | "Can this role call Athena and read this bucket?" | "Can this analyst see the `salary` column, or only rows for their region?" |

They work **together**: IAM lets a user reach the services, and Lake Formation decides which data they see.

### IAM vs Lake Formation vs resource policies

|  | **IAM** | **Lake Formation permissions** | **Resource policies** (for example, S3 bucket policies) |
| --- | --- | --- | --- |
| Attached to | Identities (users, groups, roles) | Data Catalog objects | The resource itself |
| Granularity | Service actions on resources (bucket, prefix, object) | **Database, table, column, row and cell** | The resource and who can reach it |
| Best for | General AWS access | Fine-grained **data lake** access for analysts | **Cross-account access**, or locking a bucket down regardless of IAM |

### DataZone vs Glue Data Catalog

|  | **Glue Data Catalog** | **DataZone** |
| --- | --- | --- |
| Audience | Engines and engineers | Business users across the organization |
| Holds | Technical metadata: schemas, locations, partitions | Business metadata: **business glossary**, descriptions, owners |
| Sharing | Via Lake Formation permissions | Self-service: **request and approve** access to data products |
| Scope | AWS | AWS, on premises, third-party |

## Encryption and secrets

### ACM vs KMS

|  | **ACM** | **KMS** |
| --- | --- | --- |
| Manages | **Certificates** (public/private key pairs tied to a domain) | **Encryption keys** |
| Protects | Data **in transit** (TLS) | Data **at rest** (S3, Redshift, EBS, Glue, Kinesis) |
| Typical question | "Serve HTTPS on my endpoint" | "Encrypt my bucket with a key I control" |

### KMS vs CloudHSM vs Secrets Manager

|  | **KMS** | **CloudHSM** | **Secrets Manager** |
| --- | --- | --- | --- |
| Stores | Encryption keys (AWS manages the hardware) | Keys on a **dedicated hardware security module** you control | **Secrets**: passwords, API keys, database credentials |
| Use when | Default choice for encrypting AWS data | Regulations require **single-tenant hardware** and full key control | A pipeline needs a database password, with **automatic rotation** |

## Compliance and auditing

### Audit Manager vs Config vs CloudTrail

|  | **Audit Manager** | **AWS Config** | **CloudTrail** |
| --- | --- | --- | --- |
| Question it answers | "Can I prove compliance to an auditor?" | "**What** does my resource look like, and is it compliant?" | "**Who** did what, and when?" |
| Output | Audit reports mapped to a standard | Resource configuration history and compliance status | Log of API calls |
| Relationship | Uses Config and CloudTrail as evidence | Can show which CloudTrail event changed a resource | Feeds both |

**AWS Security Hub** isn't in the course but is often confused with these. It **aggregates security findings** from GuardDuty, Macie, Inspector and Config into one place and scores you against best-practice standards.

### CloudTrail vs CloudWatch vs Config

|  | **CloudTrail** | **CloudWatch** | **AWS Config** |
| --- | --- | --- | --- |
| Records | **API calls**: who, what, when, from where | **Metrics, logs and alarms**: how resources are performing | **Resource configuration** over time |
| Question | "**Who** deleted the table?" | "**Is** the Glue job slow or failing?" | "**What** did the bucket policy look like last Tuesday?" |
| Focus | Audit and security | Performance and operations | Compliance |

## Threat and sensitive-data detection

### Macie vs Glue sensitive data detection vs GuardDuty

|  | **Macie** | **Glue sensitive data detection** | **GuardDuty** |
| --- | --- | --- | --- |
| Looks at | **What's inside** S3 objects | Data **while a Glue job processes it** | **Behavior**: API calls, network traffic, logs |
| Finds | PII and sensitive data at rest | PII in a pipeline, which it can then mask | Threats, compromised credentials, malicious activity |
| Acts | Reports findings | Can **redact or hash** the data in the job | Reports findings |

### GuardDuty vs Macie vs Inspector vs Detective

|  | **GuardDuty** | **Macie** | **Inspector** | **Detective** |
| --- | --- | --- | --- | --- |
| Finds | **Active threats** and suspicious behavior | **Sensitive data** in S3 | **Software vulnerabilities** (CVEs) in EC2, containers and Lambda | **Root cause** of a finding |
| Question | "Is someone attacking me?" | "Where is my PII?" | "What's unpatched?" | "What happened, and how far did it go?" |

## Network protection

### Security groups vs network ACLs

|  | **Security group** | **Network ACL** |
| --- | --- | --- |
| Applies to | An **instance or network interface** | A **subnet** |
| State | **Stateful**: return traffic is allowed automatically | **Stateless**: return traffic needs its own rule |
| Rules | **Allow only** | **Allow and deny** |
| Typical use | "Only the app servers may reach Redshift on port 5439" | "Block this IP range from the whole subnet" |

### WAF vs Shield vs security groups vs Network Firewall

|  | **Security groups / NACLs** | **AWS WAF** | **Shield** | **AWS Network Firewall** |
| --- | --- | --- | --- | --- |
| Layer | 3–4 (IP, port) | **7** (HTTP content) | 3–4 (Standard), plus 7 (Advanced, with WAF) | 3–7, for a **whole VPC** |
| Stops | Unwanted ports and IPs | SQL injection, XSS, bots, request floods | **DDoS** | Traffic in and out of a VPC, with domain filtering and intrusion prevention |
| Cost | Free | Pay per rule and request | Standard free; Advanced paid | Paid |

### Control Tower vs AWS Organizations

Organizations is the **underlying service** (accounts, organizational units, service control policies). Control Tower **sets it up for you with best practices** and keeps it governed. Use Organizations alone if you want to build everything yourself.

## Monitoring

### CloudWatch vs X-Ray

|  | **CloudWatch** | **X-Ray** |
| --- | --- | --- |
| Shows | **Metrics and logs per resource** | **One request's path across services** |
| Question | "Is the Lambda error rate high?" | "**Which** call in this request is slow?" |
| Granularity | Aggregates over time | Individual requests (traces) |

### Systems Manager vs CloudWatch

CloudWatch **observes** (metrics, logs, alarms). Systems Manager **acts** (runs commands, patches, applies fixes). They're commonly used together: an alarm in CloudWatch triggers a runbook in Systems Manager.

### Managed Grafana vs QuickSight vs CloudWatch dashboards

|  | **CloudWatch dashboards** | **Managed Grafana** | **QuickSight** |
| --- | --- | --- | --- |
| Audience | Engineers | Engineers and operations | **Business users** and data owners |
| Data | CloudWatch metrics and logs | **Many sources**, AWS and others | Business data (Athena, Redshift, S3, databases) |
| Best for | Quick views of AWS metrics | **Operational** dashboards across tools | **Business and trend** reporting |
