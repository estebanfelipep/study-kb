# AWS X-Ray

This file covers X-Ray: tracing requests across services to find where they slow down or fail.

## What it is

X-Ray provides **end-to-end monitoring and performance insights** for applications on AWS and their underlying services. The course lists it for monitoring **data pipelines**. It answers "**Which** call in this request is slow?" _(added)_.

## Characteristics

- **Traces** a request as it moves through API Gateway, Lambda, DynamoDB, SQS and other services _(added)_.
- The **service map** shows each component with its latency and error rate _(added)_.
- Built into [Lambda](../aws-compute/lambda.md), [API Gateway](../aws-apis/api-gateway.md) and [Step Functions](../aws-application-coordination/step-functions.md) with a setting _(added)_.
- Works on individual requests (traces), unlike [CloudWatch](cloudwatch.md)'s aggregated metrics _(added)_.
- AWS recommends instrumenting with **OpenTelemetry** (AWS Distro for OpenTelemetry) and viewing traces in **CloudWatch Application Signals**; the X-Ray SDKs are in maintenance _(added; check current docs)_.

## Example

_(added)_ A data ingestion API is slow. The X-Ray service map shows API Gateway at 20 ms, Lambda at 50 ms, and a DynamoDB write at 1.8 seconds because of throttling. The fix is DynamoDB capacity, not the Lambda code.

## Related

- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares X-Ray with CloudWatch: X-Ray traces one request's path across services ("which call is slow?"), CloudWatch aggregates metrics per resource ("is the error rate high?").
- [security-and-monitoring-on-aws.md](../../aws-data-engineering/security-and-monitoring-on-aws.md): the course lists X-Ray for monitoring data pipelines, and it traces API → Lambda requests in the example secured pipeline.
- [cloudwatch.md](cloudwatch.md): AWS recommends OpenTelemetry instrumentation with traces viewed in CloudWatch Application Signals, alongside or instead of the X-Ray SDKs.
- [api-gateway.md](../aws-apis/api-gateway.md): X-Ray tracing is built into API Gateway with a setting, and API Gateway is the first hop in the slow-API example.
- [lambda.md](../aws-compute/lambda.md): X-Ray tracing is built into Lambda with a setting, so each invocation appears in the service map.
- [step-functions.md](../aws-application-coordination/step-functions.md): X-Ray tracing is built into Step Functions with a setting.
- [dynamodb.md](../aws-databases/dynamodb.md): in the example, the X-Ray service map shows a throttled DynamoDB write as the slow call, so the fix is DynamoDB capacity.
