# Amazon EventBridge

This file covers Amazon EventBridge: serverless event routing and scheduling for event-driven pipelines, with an example.

## What it is

EventBridge is a **serverless** service for building **event-driven applications**. Loosely coupled applications work together by **emitting and responding to events**. In data engineering, it ingests events from various sources and **routes them to targets** for processing or action. For example, it can send events to Athena to run SQL queries or to Lambda for custom processing.

## Characteristics

- Incoming events can **invoke Step Functions workflows**, which coordinate several services in a pipeline.
- **Built-in matching and routing rules** filter and transform events before delivery, so event data can be **pre-processed before analytics**.
- **Event bus:** where events arrive. There's a default bus for AWS service events, custom buses for your own apps, and partner buses for SaaS apps such as Salesforce, Zendesk and Datadog.
- **Rule:** a pattern that matches events by content (for example, `source = aws.s3`, `bucket = raw-data`, and a key starting with `sales/`), plus **up to 5 targets**.
- **Input transformer:** reshapes the event before it goes to the target.
- **EventBridge Scheduler:** runs targets on a schedule (cron or rate). This is the usual way to start a pipeline every night or every hour.
- **Archive and replay:** keep events and replay them later, for example after fixing a bug.
- It's the usual path for alerts: Glue job state changes, Macie findings, GuardDuty findings and Config compliance changes are routed through EventBridge to Lambda or SNS.

## Example

Three rules on one event bus:

- **Rule 1:** an S3 object is created in `raw/sales/` → start the sales **Step Functions** workflow.
- **Rule 2:** a Glue job's state is `FAILED` → run a **Lambda** function that opens a Jira ticket.
- **Rule 3:** EventBridge Scheduler, every day at 02:00 UTC → start the nightly reporting workflow.

## Related

- [step-functions.md](step-functions.md): EventBridge rules start Step Functions workflows. For example, an S3 object created in `raw/sales/` starts the sales workflow, and a nightly schedule starts the reporting workflow.
- [lambda.md](../aws-compute/lambda.md): EventBridge routes matching events to Lambda for custom processing, such as opening a ticket when a Glue job fails.
- [sns.md](sns.md): both push events to several targets, and EventBridge often hands alerts to SNS to notify people. EventBridge adds content-based rules, SaaS events, scheduling and replay; SNS is simpler, higher-throughput fan-out that can email or text people.
- [glue.md](../aws-analytics/glue.md): Glue job state changes (such as `FAILED`) arrive as events that EventBridge rules act on.
- [s3.md](../aws-general-services/s3.md): S3 event notifications can go to EventBridge, whose rules match them by bucket and key prefix.
- [choosing-orchestration-services.md](../../aws-data-engineering/choosing-orchestration-services.md): compares EventBridge with SNS and SQS: EventBridge routes events by rules, SNS pushes one message to many subscribers, SQS stores work for one consumer.
- [orchestration-and-automation.md](../../../data-engineering/orchestration-and-automation.md): EventBridge is the AWS event bus in the pub/sub vs queue vs event bus patterns described there.
