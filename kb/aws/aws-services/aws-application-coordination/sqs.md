# Amazon SQS (Simple Queue Service)

This file covers Amazon SQS: managed message queues that decouple and buffer work between pipeline steps, with an example.

## What it is

SQS is a managed **message queuing** service that **sends, stores and retrieves** messages of various sizes **asynchronously**. Users or systems submit analytic jobs as messages to a queue, which **decouples the submitters from the jobs being processed**. In serverless workflows, SQS **connects Lambda functions into workflows**.

## Characteristics

- Compute such as **EC2 instances polls the queue** and picks up the messages that contain jobs. Processing **scales independently**, based on the number of messages in the queue.
- Features include **message attributes, dead-letter queues**, and integration with the **AWS CLI and SDKs**.
- One Lambda function can send a message to a queue, and that message invokes a separate Lambda function for further processing.
- **Pull model:** consumers ask the queue for messages, and each message goes to **one** consumer. A message is **deleted** once it's processed, and there's no replay _(added)_.
- **Visibility timeout:** while a consumer works on a message, the message is hidden from other consumers. If the consumer crashes, the message reappears and another consumer retries it _(added)_.
- **Dead-letter queue (DLQ):** a message that fails too many times moves here. One bad message doesn't block the queue, and you can inspect it later _(added)_.
- **Retention:** up to 14 days _(added)_.
- **Queue types** _(added)_:
  - **Standard:** nearly unlimited throughput, at-least-once delivery, best-effort order.
  - **FIFO:** strict order and exactly-once processing, with lower throughput.

## Example

_(added)_ Analysts submit report requests from a web form throughout the day. Sometimes that's 10 an hour, and sometimes it's 5,000 in a minute after a board meeting.

- Each request becomes a message in a queue.
- An Auto Scaling group of EC2 workers (or Lambda functions) pulls messages, runs the query and emails the report.
- The worker count scales with **queue depth**. During a spike, the queue absorbs the burst instead of overloading the database.
- A malformed request that fails 3 times goes to the **DLQ** for someone to inspect.

## Related

- [sns.md](sns.md): in SNS + SQS fan-out, SNS pushes one message to several SQS queues, and each queue buffers work for a consumer running at its own pace.
- [lambda.md](../aws-compute/lambda.md): a message in an SQS queue can invoke a Lambda function, which is how SQS chains Lambda functions into asynchronous workflows. Lambda functions can also be the workers that pull messages.
- [kinesis-data-streams.md](../aws-analytics/kinesis-data-streams.md): both buffer data between producers and consumers. An SQS message is a job for one consumer, deleted once processed; a Kinesis record is an event many consumers read in order and can replay.
- [choosing-orchestration-services.md](../../aws-data-engineering/choosing-orchestration-services.md): compares SQS with SNS, EventBridge and Kinesis Data Streams: SQS stores work for one consumer and smooths load spikes, SNS pushes to many, EventBridge routes by rules, Kinesis lets many consumers replay.
- [orchestration-and-automation.md](../../../data-engineering/orchestration-and-automation.md): SQS is the AWS queue in the pub/sub vs queue vs event bus patterns described there, including dead-letter queues.
- [batch-and-streaming.md](../../../data-engineering/batch-and-streaming.md): explains queues vs streams: a queue message is a job deleted after one consumer processes it, while a stream record can be read by many consumers and replayed.
