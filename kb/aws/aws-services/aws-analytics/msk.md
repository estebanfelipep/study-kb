# Amazon MSK (Managed Streaming for Apache Kafka)

Amazon MSK: fully managed Apache Kafka clusters for streaming, including MSK Serverless.

## What it is

Amazon MSK provides fully managed **Apache Kafka** clusters for real-time streaming pipelines and applications. Like a Kinesis stream, it stores the stream so Kafka consumers can process it. It's the ingestion choice when a workload needs Kafka.

## Characteristics

- Real-time streaming; storage and replay with configurable retention.
- You manage Kafka topics and consumers; transformation is written in the consumers.
- A source for [Redshift streaming ingestion](redshift.md): a materialized view over an MSK topic.
- Usual exam triggers: "Apache Kafka", "existing Kafka applications".
- Provisioned MSK gives full control over broker types, configuration and very high, steady throughput.

### MSK Serverless

- Runs Apache Kafka clusters **without managing and scaling infrastructure**, with **pay-per-use pricing, automatic scaling and high availability**.
- Standard **Kafka APIs**, so existing producers and consumers work unchanged.
- No brokers to size, no storage to provision, no partition rebalancing.
- Fewer configuration options than provisioned MSK, and throughput limits per cluster.

## Example

- A startup's microservices use Kafka locally for order events. In production they have no one to manage brokers, and traffic swings between almost none overnight and heavy during sales. MSK Serverless runs their Kafka code unchanged and scales with the traffic.

## Related

- [redshift.md](redshift.md): Redshift streaming ingestion can create a materialized view over an MSK topic and read it directly.
- [managed-service-for-apache-flink.md](managed-service-for-apache-flink.md): Flink can read an MSK topic and process it in real time.
- [kinesis-data-streams.md](kinesis-data-streams.md): both store a stream for consumers to process and replay; MSK is the Kafka-based option, KDS the AWS-native one.
- [batch-and-streaming.md](../../../data-engineering/batch-and-streaming.md): MSK implements a stream as described here, with Kafka topics and partitions instead of Kinesis shards.
- [choosing-ingestion-services.md](../../aws-data-engineering/choosing-ingestion-services.md): compares MSK with Kinesis Data Streams and Firehose: pick MSK when the question says "Apache Kafka" or "existing Kafka applications"; Firehose when you want delivery with no servers; KDS for AWS-native streaming.
- [choosing-storage-and-processing-services.md](../../aws-data-engineering/choosing-storage-and-processing-services.md): compares MSK Serverless, provisioned MSK and KDS on-demand: MSK Serverless is Kafka without operations; provisioned MSK gives full control and very high steady throughput; KDS on-demand is serverless but not Kafka.
- [zero-etl-and-serverless-on-aws.md](../../aws-data-engineering/zero-etl-and-serverless-on-aws.md): MSK Serverless is the serverless option for Kafka streaming, replacing provisioned MSK.
- [ingest-on-aws.md](../../aws-data-engineering/aws-data-pipeline/ingest-on-aws.md): MSK is a stage 1 (ingest) service for real-time streaming on Apache Kafka.
