# AWS Lambda

This file covers AWS Lambda: serverless functions for ingestion, automation and event-driven processing, with their limits and an example.

## What it is

Lambda runs code (**Lambda functions**) **without provisioning or managing servers**. It's **the primary serverless AWS service**. Other services or events can invoke a function, and a function can invoke other services. In data engineering, Lambda handles **lightweight ingestion** and **automation** of workflows. It does one task, while Step Functions coordinates many.

## Characteristics

- **Event-invoked:** events from **S3, DynamoDB or Kinesis Data Streams** can invoke a function to process incoming data in real time.
- **Orchestrated:** [Step Functions](../aws-application-coordination/step-functions.md) can orchestrate multiple Lambda functions, with **error handling, retries and visualizations**. Combined with Step Functions, Lambda functions can invoke AWS services and microservices as steps in a workflow.
- **Decoupled:** Lambda works in event-driven architectures with [SNS](../aws-application-coordination/sns.md) and [SQS](../aws-application-coordination/sqs.md), which decouple and coordinate analytics tasks. A message in an SQS queue can invoke a function, which chains functions together asynchronously.
- Can sit behind [API Gateway](../aws-apis/api-gateway.md), where it runs the business logic of a serverless API.
- **Maximum run time: 15 minutes** per invocation _(added)_.
- Memory goes up to **10 GB**, and CPU scales with memory _(added)_.
- You pay per request and per millisecond of run time, and nothing when idle _(added)_.
- Suits small to medium data, such as one file or one batch of records. Bigger transformations that would time out belong in a Glue job _(added)_.

## Example

_(added)_ A partner uploads `orders_2026-10-18.csv` to an S3 bucket, and the upload event invokes a Lambda function. The function:

1. Validates the header and row count.
2. Converts the file to Parquet and writes it to the `clean/` prefix.
3. Moves bad files to a `quarantine/` prefix.

It runs in seconds, once per file, and no server runs between uploads. That's **automation**: one task, triggered by an event.

## Related

- [s3.md](../aws-general-services/s3.md): S3 event notifications (object created, deleted) invoke Lambda functions, which makes S3 the usual starting point of a serverless pipeline, as in the partner-upload example.
- [step-functions.md](../aws-application-coordination/step-functions.md): Step Functions orchestrates multiple Lambda functions as workflow steps, with error handling and retries. Lambda does one task; Step Functions coordinates many.
- [sqs.md](../aws-application-coordination/sqs.md): a message in an SQS queue invokes a Lambda function, which chains functions together asynchronously.
- [sns.md](../aws-application-coordination/sns.md): Lambda functions subscribe to SNS topics and process each message asynchronously.
- [eventbridge.md](../aws-application-coordination/eventbridge.md): EventBridge rules route matching events to Lambda for custom processing.
- [dynamodb.md](../aws-databases/dynamodb.md): DynamoDB Streams invokes Lambda on every table change, and Lambda reads and writes DynamoDB tables directly.
- [kinesis-data-streams.md](../aws-analytics/kinesis-data-streams.md): Kinesis Data Streams records invoke Lambda functions to process incoming data in real time.
- [api-gateway.md](../aws-apis/api-gateway.md): API Gateway invokes Lambda, which runs the business logic of a serverless API.
- [glue.md](../aws-analytics/glue.md): when a transformation is too big for Lambda's 15-minute limit, it belongs in a Glue job instead.
- [choosing-orchestration-services.md](../../aws-data-engineering/choosing-orchestration-services.md): compares Lambda with Step Functions and Glue jobs: Lambda does one small task (up to 15 minutes), Step Functions coordinates many tasks, Glue does heavy distributed ETL.
- [zero-etl-and-serverless-on-aws.md](../../aws-data-engineering/zero-etl-and-serverless-on-aws.md): Lambda is the primary serverless AWS service, the "run code" role in the serverless list.
- [orchestration-and-automation.md](../../../data-engineering/orchestration-and-automation.md): Lambda is the example of automation (one task, triggered by an event) and of serverless (pay only while code runs).
