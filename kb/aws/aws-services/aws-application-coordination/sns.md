# Amazon SNS (Simple Notification Service)

This file covers Amazon SNS: publish/subscribe messaging that fans one message out to many endpoints, with an example.

## What it is

SNS is a fully managed **messaging** service. Applications and services send messages through **SNS topics** to **multiple endpoints at the same time**. This is **publish/subscribe**: publishers send to a topic, and every subscriber gets a copy. In serverless workflows, SNS provides **asynchronous communication** between services.

## Characteristics

- SNS topics **receive notifications and events** from data sources and AWS services.
- Those events can **invoke Step Functions workflows**, which coordinate Glue, Redshift and Athena in processing and analytics pipelines.
- **Message durability, encryption and archiving** make analytics workflows more reliable and help them recover from failures.
- An S3 upload can publish a message to a topic. Lambda functions or other services subscribe to the topic and process the object asynchronously.
- Subscriber types are Lambda, SQS queues, HTTP/HTTPS endpoints, Firehose, email, SMS and mobile push.
- SNS **pushes** messages immediately and doesn't store them.
- **Subscription filter policies** let each subscriber receive only the messages it needs.
- **SNS + SQS fan-out:** SNS sends to several SQS queues, and each queue buffers work for a different consumer that runs at its own pace. If one consumer is down, its queue holds the messages until it recovers.
- It's the usual last step of an alert: a CloudWatch alarm or an EventBridge rule notifies the on-call team through SNS.

## Example

A new orders file lands in S3, and S3 publishes one event to the `new-orders` topic. Three subscribers each get a copy at the same time:

- **Lambda A** updates a real-time inventory table in DynamoDB.
- An **SQS queue** feeds a slower billing job.
- An **email** tells the finance team that today's orders file has arrived.

The publisher doesn't know how many subscribers there are. Adding a fourth consumer is just a new subscription.

## Related

- [sqs.md](sqs.md): SNS pushes one message to many subscribers and stores nothing; SQS stores messages until one consumer pulls each. Combined in SNS + SQS fan-out, SNS sends to several queues and each queue buffers work for its own consumer.
- [lambda.md](../aws-compute/lambda.md): Lambda functions subscribe to SNS topics and process each message asynchronously, such as an S3 upload event.
- [s3.md](../aws-general-services/s3.md): an S3 upload can publish a message to an SNS topic, which starts the asynchronous processing of the object.
- [step-functions.md](step-functions.md): SNS messages can start Step Functions workflows, and a workflow can publish to SNS to alert the team when a check fails.
- [eventbridge.md](eventbridge.md): both push to several targets. EventBridge has rich content-based rules, SaaS events, schedules and replay; SNS is simpler fan-out that can notify people directly. EventBridge rules often send alerts on to SNS.
- [cloudwatch.md](../aws-monitoring/cloudwatch.md): CloudWatch alarms notify the on-call team through SNS.
- [choosing-orchestration-services.md](../../aws-data-engineering/choosing-orchestration-services.md): compares SNS with SQS and EventBridge: SNS pushes to many subscribers, SQS stores work for one consumer, EventBridge routes events by rules.
- [orchestration-and-automation.md](../../../data-engineering/orchestration-and-automation.md): SNS is the AWS publish/subscribe service in the pub/sub vs queue vs event bus patterns described there.
