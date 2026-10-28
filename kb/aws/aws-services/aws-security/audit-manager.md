# AWS Audit Manager

This file covers Audit Manager: collecting compliance evidence and producing audit reports.

## What it is

Audit Manager **continuously audits** usage to assess **risk and compliance** with regulations and industry standards. It **automatically collects and organizes evidence** from AWS services and turns it into **auditor-friendly reports** for standards such as **GDPR, PCI DSS** and others. It belongs to **regulatory compliance**, one of the five security areas, and applies across all pipeline stages.

## Characteristics

- A governance (compliance) service.
- Comes with **prebuilt frameworks** (GDPR, HIPAA, PCI DSS, SOC 2, CIS) and lets you build custom ones.
- Evidence comes from [Config](../aws-monitoring/config.md), [CloudTrail](../aws-monitoring/cloudtrail.md), Security Hub and manual uploads.
- It **doesn't make you compliant**. It gathers proof of what your controls are doing.
- Answers "Can I prove compliance to an auditor?".

## Example

Before a yearly PCI DSS audit, the compliance team opens an Audit Manager assessment. Instead of spending weeks collecting screenshots, they export a report showing that every bucket holding card data was encrypted and logged for the full year.

## Related

- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares Audit Manager with Config and CloudTrail: Audit Manager proves compliance to an auditor and uses the other two as evidence. Also notes Security Hub, which aggregates findings instead.
- [security-and-monitoring-on-aws.md](../../aws-data-engineering/security-and-monitoring-on-aws.md): Audit Manager is a course service for regulatory compliance.
- [data-security-and-monitoring.md](../../../data-engineering/data-security-and-monitoring.md): Audit Manager implements regulatory compliance, one of the five security areas, by automating auditing and evidence collection.
- [config.md](../aws-monitoring/config.md): Config is an evidence source: its compliance results feed Audit Manager reports.
- [cloudtrail.md](../aws-monitoring/cloudtrail.md): CloudTrail API logs are an evidence source for Audit Manager reports.
- [data-personas.md](../../../data-engineering/data-personas.md): the data security officer uses Audit Manager to handle regulations.
