# aws-security — index

Encryption, sensitive data discovery, threat detection, web and DDoS protection, compliance evidence and account governance.

## How to read this folder

- **Before:** The five security areas, in [data-security-and-monitoring.md](../../../data-engineering/data-security-and-monitoring.md), then [aws-identity](../aws-identity/aws-identity.md) and [aws-networking](../aws-networking/aws-networking.md).
- **Order:** From protecting the data, to protecting the system, to governing accounts.
- **After:** [aws-monitoring](../aws-monitoring/aws-monitoring.md).

## Files (in reading order)

**Protect the data**

- [kms.md](kms.md): KMS key types, envelope encryption, and encrypting pipeline data at rest. Read when: you need how data at rest is encrypted, who controls keys, or why KMS doesn't cover data in transit.
- [macie.md](macie.md): Macie's ML-based discovery and classification of PII and sensitive data in S3. Read when: you need to find PII in S3 or flag risky bucket settings.

**Protect the system**

- [guardduty.md](guardduty.md): GuardDuty threat detection from CloudTrail, VPC Flow Logs and DNS logs, plus its protection plans. Read when: you need to detect attacks, leaked credentials or malicious behavior.
- [waf.md](waf.md): AWS WAF layer 7 rules, rate limiting and managed rule groups. Read when: you need to block SQL injection, XSS or request floods on web apps and APIs.
- [shield.md](shield.md): Shield Standard and Shield Advanced DDoS protection. Read when: you need how AWS absorbs DDoS attacks, or what Shield Advanced adds.

**Govern accounts**

- [control-tower.md](control-tower.md): Control Tower landing zones, preventive and detective controls, and Account Factory. Read when: you need how a multi-account AWS environment is set up and governed.
- [audit-manager.md](audit-manager.md): Audit Manager's compliance frameworks, evidence collection and auditor reports. Read when: you need to prove compliance with GDPR, PCI DSS, HIPAA and similar standards.
