# AWS Systems Manager

This file covers Systems Manager: operations management and automation for EC2 instances.

## What it is

Systems Manager provides **application-level monitoring for EC2 instances** and helps **automate operational tasks**. The course lists it for monitoring **resources**.

## Characteristics

- **Course correction:** the course's description is loose. Systems Manager is mainly an **operations management** toolkit. Most **metrics and alarms** come from [CloudWatch](cloudwatch.md); Systems Manager acts on instances and gathers operational data.
- **Run Command:** run a script on many instances at once, without SSH.
- **Session Manager:** shell access with no open ports or SSH keys, logged in CloudTrail.
- **Patch Manager:** patch instances on a schedule.
- **Parameter Store:** store configuration and secrets for pipelines.
- **OpsCenter and Explorer:** collect operational issues (including from CloudWatch alarms) in one place.
- **Automation runbooks:** fix common problems automatically, for example restart a service when an alarm fires. [Config](config.md) uses them for auto-remediation.
- **Inventory:** what software is installed on each instance.

## Example

A self-managed Kafka cluster on EC2 runs out of disk. A CloudWatch alarm (from the agent's disk metric) opens an OpsCenter item and starts an Automation runbook that deletes old log segments and restarts the broker.

## Related

- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares Systems Manager with CloudWatch: CloudWatch observes (metrics, logs, alarms), Systems Manager acts (runs commands, patches, fixes).
- [security-and-monitoring-on-aws.md](../../aws-data-engineering/security-and-monitoring-on-aws.md): the course lists Systems Manager for monitoring resources, alongside CloudWatch.
- [exam-traps.md](../../aws-data-engineering/exam-traps.md): course correction: the course calls Systems Manager "application-level monitoring for EC2", but it's mainly an operations management toolkit.
- [cloudwatch.md](cloudwatch.md): a CloudWatch alarm opens an OpsCenter item or starts an Automation runbook, so the two are used together.
- [config.md](config.md): Config uses Systems Manager Automation runbooks to auto-remediate non-compliant resources.
- [cloudtrail.md](cloudtrail.md): Session Manager shell sessions are logged in CloudTrail.
