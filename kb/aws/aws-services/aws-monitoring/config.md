# AWS Config

This file covers AWS Config: resource configuration history, compliance rules and remediation.

## What it is

AWS Config provides **configuration management and auditing of AWS resources** to assess security and compliance posture **over time**. It belongs to **regulatory compliance**, one of the five security areas. It answers "**What** does my resource look like, and is it compliant?" _(added)_.

## Characteristics

- Records the **configuration history** of each resource: what it looked like and when it changed _(added)_.
- **Config rules** check resources against desired settings ("S3 buckets must block public access", "Redshift clusters must be encrypted") and flag non-compliant ones _(added)_.
- Can **auto-remediate** through [Systems Manager](systems-manager.md) Automation, for example to re-enable bucket encryption _(added)_.
- **Conformance packs** bundle rules for a standard, such as HIPAA _(added)_.
- Can show which [CloudTrail](cloudtrail.md) event changed a resource, and is an evidence source for [Audit Manager](../aws-security/audit-manager.md) _(added)_.
- [Control Tower](../aws-security/control-tower.md) detective controls are Config rules _(added)_.

## Example

_(added)_ A rule requires encryption on every S3 bucket. An engineer creates an unencrypted bucket for a quick test. Config marks it non-compliant within minutes, an [EventBridge](../aws-application-coordination/eventbridge.md) rule notifies the security team through [SNS](../aws-application-coordination/sns.md), and remediation turns encryption on.

## Related

- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares Config with Audit Manager and CloudTrail: Config shows what a resource looks like and whether it complies, Audit Manager proves compliance to an auditor, and CloudTrail shows who did what.
- [security-and-monitoring-on-aws.md](../../aws-data-engineering/security-and-monitoring-on-aws.md): Config is a course service for regulatory compliance, and checks "is it compliant" in the example secured pipeline.
- [data-security-and-monitoring.md](../../../data-engineering/data-security-and-monitoring.md): Config implements regulatory compliance, one of the five security areas, by checking resources against rules over time.
- [audit-manager.md](../aws-security/audit-manager.md): Audit Manager uses Config results as evidence in its compliance reports.
- [cloudtrail.md](cloudtrail.md): Config can show which CloudTrail event changed a resource.
- [control-tower.md](../aws-security/control-tower.md): Control Tower's detective controls are Config rules, so Config is what flags accounts that break the landing zone's rules.
- [systems-manager.md](systems-manager.md): Config auto-remediates non-compliant resources through Systems Manager Automation, for example to re-enable bucket encryption.
- [eventbridge.md](../aws-application-coordination/eventbridge.md): an EventBridge rule reacts to a Config non-compliance finding and notifies the security team through SNS.
