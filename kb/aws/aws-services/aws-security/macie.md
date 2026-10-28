# Amazon Macie

This file covers Macie: discovering and classifying sensitive data such as PII in S3.

## What it is

Macie **automatically discovers, classifies and protects sensitive data** such as **PII**, using **machine learning and pattern matching**. It belongs to **sensitive data protection**, one of the five security areas, and works on the storage stage of the pipeline. It's the service the data security officer uses to protect PII.

## Characteristics

- A security service that also feeds governance.
- Works on **S3 only**.
- Finds names, addresses, credit card numbers, passport numbers, credentials, and custom patterns you define.
- Also flags risky **bucket settings**: public, unencrypted or shared outside the account.
- Looks at **what's inside** S3 objects (data at rest), not behavior.
- Findings go to [EventBridge](../aws-application-coordination/eventbridge.md) and Security Hub.

## Example

A partner drops customer exports into the `landing/` bucket every day, before anything moves to `raw/`. Macie scans it and finds a file with unmasked credit card numbers. An EventBridge rule triggers a [Lambda](../aws-compute/lambda.md) function that moves the file to a quarantine bucket and alerts the data security officer.

## Related

- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares Macie with Glue sensitive data detection and GuardDuty: Macie finds PII at rest in S3, Glue finds and masks PII while a job runs, GuardDuty detects threatening behavior.
- [security-and-monitoring-on-aws.md](../../aws-data-engineering/security-and-monitoring-on-aws.md): Macie is a course service for sensitive data protection, and scans the raw S3 bucket in the example secured pipeline.
- [data-personas.md](../../../data-engineering/data-personas.md): the data security officer uses Macie to protect PII.
- [s3.md](../aws-general-services/s3.md): Macie works on S3 only: it scans objects for sensitive data and flags risky bucket settings (public, unencrypted, shared).
- [glue.md](../aws-analytics/glue.md): Glue sensitive data detection complements Macie by finding and masking PII inside a pipeline, while Macie scans data at rest.
- [guardduty.md](guardduty.md): Macie looks at what's inside data, while GuardDuty looks at behavior.
- [eventbridge.md](../aws-application-coordination/eventbridge.md): Macie findings go to EventBridge, where a rule can trigger a Lambda function that quarantines the file.
