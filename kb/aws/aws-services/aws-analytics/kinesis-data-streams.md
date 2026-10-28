# Amazon Kinesis Data Streams

Amazon Kinesis Data Streams (KDS): real-time streaming storage, its records and shards, and its role as an event source.

## What it is

Kinesis Data Streams is a real-time data streaming service. It captures large volumes of continuous data (clicks, logs, IoT readings, transactions) and keeps it for a while, so multiple applications can read and process it within milliseconds of arrival. The course names it as an **event source** in orchestrated workflows: it triggers Lambda functions, feeds Step Functions streaming pipelines, and is a source for OpenSearch and Redshift streaming ingestion. For what a stream is, see [batch-and-streaming.md](../../../data-engineering/batch-and-streaming.md).

```
Producers ──▶ Kinesis Data Stream ──▶ Consumers
(apps, IoT,    (stores records       (Lambda, Flink, Firehose,
 logs, SDK)     24 h by default,      Redshift streaming
                up to 365 days)       ingestion, apps on EC2/ECS)
```

## Characteristics

### Records

- **Data blob:** the payload, up to **1 MB**. Kinesis treats it as opaque bytes, so any data type fits; in practice records are mostly small JSON events. Large files belong in S3; video uses the separate **Kinesis Video Streams** service.
- **Partition key:** chosen by the producer (for example `user_id`); decides which shard the record goes to.
- **Sequence number:** assigned by Kinesis; the record's position. Order is guaranteed **within a shard**.
- **Timestamp:** when the record arrived.

### Storage

- **Shards:** a stream is split into shards, each an ordered sequence of records. Same partition key → same shard. Each shard handles about **1 MB/s in and 2 MB/s out**.
- **Capacity modes:** **on-demand** scales shards automatically (serverless streaming); **provisioned** lets you set the count.
- **Replicated across three Availability Zones**, so a record is durable once accepted.
- **Retention:** 24 hours by default, up to 365 days. Records expire by time, not because someone read them.
- **Read by position:** a consumer asks for "everything after sequence number X" or "from 2 hours ago". Several consumers each keep their own position and can **replay** older records.
- **Latency:** real time, about 70–200 ms.
- **Cost:** per shard-hour or throughput, plus retention.
- **Consumers:** your code (Lambda, Flink, custom apps); transformation is written in the consumer.
- **Monitoring:** the CloudWatch metric `GetRecords.IteratorAgeMilliseconds` shows how far consumers are behind.

## Example

- **Fraud detection:** each card transaction is written with `card_id` as the partition key, so one card's transactions stay in order. A Lambda consumer scores each one in milliseconds and blocks suspicious ones. [Firehose](data-firehose.md) archives the same stream to S3 for model training and audits.
- **Video playback quality:** every player sends a heartbeat event every few seconds (bitrate, buffering, errors, device, region, CDN). On-demand mode absorbs spikes during a premiere. [Managed Service for Apache Flink](managed-service-for-apache-flink.md) computes buffering rate per region and CDN per 1-minute window. A spike makes a Lambda consumer publish to [SNS](../aws-application-coordination/sns.md), or [EventBridge](../aws-application-coordination/eventbridge.md) starts a [Step Functions](../aws-application-coordination/step-functions.md) workflow that shifts traffic. Firehose writes Parquet to S3 for next-day reports in [Athena](athena.md) and [QuickSight](quicksight.md). Kinesis fits because the alert must fire within seconds, three consumers need the same events, and the team wants to replay hours after fixing a bug.

## Related

- [data-firehose.md](data-firehose.md): Firehose reads from a Kinesis data stream and archives the same records to S3, while real-time consumers read the stream directly (KDS → Firehose → S3).
- [managed-service-for-apache-flink.md](managed-service-for-apache-flink.md): Flink reads the stream and computes real-time results, such as windowed aggregations per minute.
- [lambda.md](../aws-compute/lambda.md): new records in the stream invoke Lambda functions, which process each record in real time (for example scoring a transaction for fraud).
- [redshift.md](redshift.md): Redshift streaming ingestion creates a materialized view over the stream and reads it directly, with no S3 staging.
- [cloudwatch.md](../aws-monitoring/cloudwatch.md): the CloudWatch metric `GetRecords.IteratorAgeMilliseconds` shows how far consumers lag behind the stream, so an alarm can fire before retention runs out.
- [batch-and-streaming.md](../../../data-engineering/batch-and-streaming.md): Kinesis Data Streams is the AWS implementation of a stream as described here: ordered records, partition keys, retention and replay by position (data in motion).
- [choosing-ingestion-services.md](../../aws-data-engineering/choosing-ingestion-services.md): compares KDS with S3 (data in motion vs data at rest), and with Firehose and MSK: KDS stores the stream for your consumers with replay; Firehose delivers it with no code; MSK is the Kafka option.
- [choosing-orchestration-services.md](../../aws-data-engineering/choosing-orchestration-services.md): compares KDS with SQS: an SQS message is a job for one consumer and is deleted once processed; a Kinesis record is an event many consumers can read and replay.
- [choosing-storage-and-processing-services.md](../../aws-data-engineering/choosing-storage-and-processing-services.md): compares KDS on-demand with MSK Serverless and provisioned MSK: all are streaming options; pick KDS when you're not tied to Kafka.
