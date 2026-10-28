# Amazon VPC, security groups and network ACLs

This file covers network isolation for data pipelines: VPCs, subnets, security groups, network ACLs and VPC endpoints.

## What it is

A **VPC** is your private network in AWS. **Security groups, network ACLs and firewalls** restrict network access and secure compute and storage. Best practice is to use a **VPC and network ACLs** so resources aren't exposed publicly. These belong to **data and network security**, one of the five security areas.

## Characteristics

- Put Redshift, EMR and RDS in **private subnets** with no public IP.
- **VPC endpoints** let resources reach S3, Glue or KMS **without going over the internet**.
- **Security group:** applies to an **instance or network interface**; **stateful** (return traffic is allowed automatically); **allow rules only**.
- **Network ACL:** applies to a **subnet**; **stateless** (return traffic needs its own rule); **allow and deny** rules.
- Both work at layers 3–4 (IP, port) and are free.
- **Encryption at rest** adds protection on top of network controls.
- Best practice: **use network isolation**, keeping resources off the public internet.

## Example

A Redshift cluster sits in a private subnet. Its security group accepts port 5439 only from the security group of the QuickSight VPC connection. An S3 gateway endpoint lets `COPY` read from S3 without internet access.

A network ACL blocks a known bad IP range from the whole subnet.

## Related

- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares security groups with network ACLs (stateful, allow-only, per instance vs stateless, allow and deny, per subnet), and both with WAF, Shield and Network Firewall.
- [security-and-monitoring-on-aws.md](../../aws-data-engineering/security-and-monitoring-on-aws.md): a VPC with network ACLs implements the "use network isolation" best practice, and Athena/Redshift sit in a private subnet in the example secured pipeline.
- [data-security-and-monitoring.md](../../../data-engineering/data-security-and-monitoring.md): VPCs, security groups and network ACLs implement data and network security, one of the five security areas.
- [redshift.md](../aws-analytics/redshift.md): Redshift is placed in a private subnet: its security group accepts port 5439 only from QuickSight's VPC connection, and an S3 gateway endpoint lets `COPY` read S3 without internet access.
- [s3.md](../aws-general-services/s3.md): S3 sits outside your VPC; resources in private subnets reach it through a gateway VPC endpoint instead of the internet.
- [guardduty.md](../aws-security/guardduty.md): GuardDuty analyzes VPC Flow Logs to detect malicious network traffic.
- [waf.md](../aws-security/waf.md): security groups and NACLs filter IPs and ports at layers 3–4, while WAF inspects HTTP requests at layer 7.
