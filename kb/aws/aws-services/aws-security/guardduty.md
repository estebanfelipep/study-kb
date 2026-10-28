# Amazon GuardDuty

This file covers GuardDuty: threat detection across accounts and workloads.

## What it is

GuardDuty is a **threat detection** service that identifies potential security issues by monitoring AWS resources such as **networks, applications and user activity**. For monitoring, it detects potential security issues in workloads by watching for **malicious or unauthorized behavior**. The course lists it under **data and network security** and under monitoring **data access**.

## Characteristics

- Analyzes **CloudTrail events, VPC Flow Logs and DNS logs** with ML and threat intelligence. **No agents** to install for these.
- Optional protection plans add **S3 data events, EKS, RDS login activity, Lambda network activity and malware scanning**.
- One click to enable. Findings go to [EventBridge](../aws-application-coordination/eventbridge.md) and Security Hub.
- Looks at **behavior** (API calls, network traffic, logs), not at the content of data. Answers "Is someone attacking me?".

## Example

An access key for the ingestion role leaks on a public code repository. Hours later, GuardDuty flags API calls with that key from an unusual country and a burst of `GetObject` calls on the data lake. An EventBridge rule triggers a [Lambda](../aws-compute/lambda.md) function that deactivates the key.

## Related

- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares GuardDuty with Macie, Inspector and Detective (active threats vs sensitive data vs software vulnerabilities vs root cause), and with Macie and Glue sensitive data detection (behavior vs data content).
- [security-and-monitoring-on-aws.md](../../aws-data-engineering/security-and-monitoring-on-aws.md): GuardDuty is a course service for data and network security and for monitoring data access, and watches for threats in the example secured pipeline.
- [cloudtrail.md](../aws-monitoring/cloudtrail.md): GuardDuty analyzes CloudTrail events to spot suspicious API calls, such as a leaked key used from an unusual country.
- [vpc.md](../aws-networking/vpc.md): GuardDuty analyzes VPC Flow Logs (and DNS logs) to detect malicious network activity, with no agents to install.
- [macie.md](macie.md): GuardDuty looks at behavior (API calls, network traffic), while Macie looks at what's inside S3 objects. Both send findings to EventBridge and Security Hub.
- [eventbridge.md](../aws-application-coordination/eventbridge.md): GuardDuty findings go to EventBridge, where a rule can trigger an automatic response.
- [lambda.md](../aws-compute/lambda.md): in the example, an EventBridge rule on a GuardDuty finding triggers a Lambda function that deactivates the leaked access key.
