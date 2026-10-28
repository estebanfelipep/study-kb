# Amazon DynamoDB

Amazon DynamoDB: the serverless NoSQL key-value and document database, and DynamoDB Streams as an event source.

## What it is

Amazon DynamoDB is a fully managed NoSQL database with no servers to provision or manage. Lambda functions can operate on DynamoDB tables directly, with no underlying infrastructure to manage. It's one of AWS's purpose-built databases (key-value), and EMR and OpenSearch can analyze data stored in it.

## Characteristics

- **Key-value and document** model; single-digit-millisecond reads and writes at any scale.
- Access by key. No joins or complex ad hoc SQL.
- **On-demand capacity** (pay per request, scales automatically) or **provisioned capacity** (set reads and writes per second; cheaper for steady load).
- **DynamoDB Streams** emits every change, which can trigger Lambda functions, so DynamoDB is an **event source** as well as a store. Lambda can be invoked by DynamoDB events to process data in real time.
- **TTL** (time to live) deletes expired items automatically.
- Encryption at rest with [KMS](../aws-security/kms.md).
- Writes can be throttled when capacity is too low.

## Example

- A pipeline remembers which files it already processed: each Lambda run writes `{file_key, status, processed_at}` to a table and checks it first, so a file delivered twice isn't loaded twice.
- A `user_sessions` table holds live session data for a streaming app, and DynamoDB Streams sends every change to a Lambda function that updates real-time counters.
- A metrics API: [API Gateway](../aws-apis/api-gateway.md) → [Lambda](../aws-compute/lambda.md) reads a precomputed value from DynamoDB and returns JSON.

## Related

- [lambda.md](../aws-compute/lambda.md): DynamoDB Streams sends every table change to a Lambda function, and Lambda functions read and write tables directly. That makes DynamoDB both an event source and a state store for serverless pipelines.
- [api-gateway.md](../aws-apis/api-gateway.md): in a serverless API, API Gateway invokes Lambda, which reads the precomputed value from DynamoDB and returns it.
- [opensearch-service.md](opensearch-service.md): OpenSearch can analyze data stored in DynamoDB with the OpenSearch APIs.
- [choosing-storage-and-processing-services.md](../../aws-data-engineering/choosing-storage-and-processing-services.md): compares DynamoDB with RDS/Aurora. DynamoDB is NoSQL, accessed by key, fully serverless, with no joins; RDS/Aurora is relational SQL with joins and transactions on instances you size.
- [deliver-on-aws.md](../../aws-data-engineering/aws-data-pipeline/deliver-on-aws.md): DynamoDB is the key-value example among AWS's purpose-built databases at the deliver stage.
- [zero-etl-and-serverless-on-aws.md](../../aws-data-engineering/zero-etl-and-serverless-on-aws.md): DynamoDB is the serverless NoSQL database in the serverless services list, the alternative to provisioned RDS/Aurora.
