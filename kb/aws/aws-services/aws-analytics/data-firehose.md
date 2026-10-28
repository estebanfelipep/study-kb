# Amazon Data Firehose

Amazon Data Firehose: fully managed delivery of streaming data into S3, Redshift, OpenSearch and other destinations.

## What it is

Amazon Data Firehose ingests real-time data streams and delivers them to a destination. It doesn't store the stream for apps to process; it packs records and loads them, for example into the S3 data lake. Exam material may use the name **Kinesis Data Firehose**.

## Characteristics

- Can **convert streams to Apache Parquet or ORC**, **decompress** data, and run **custom transformations**.
- Light, in-flight transformation only (format conversion, Lambda transforms). Heavier logic belongs in processing.
- **Near real time:** buffers records for seconds to minutes before delivery.
- **No storage or replay:** data passes through.
- **Fully managed:** no consumer code to write and no servers.
- Destinations include S3, Redshift, OpenSearch, Splunk and more.
- **Delivery to Redshift:** Firehose buffers records, writes them to S3, then runs a `COPY` into Redshift.
- Can read from [Kinesis Data Streams](kinesis-data-streams.md), and can subscribe to [SNS](../aws-application-coordination/sns.md) topics. Step Functions pipelines can process Firehose data through Lambda.
- Parquet/ORC conversion means [Athena](athena.md) and Redshift Spectrum later scan less and cost less.

## Example

- IoT readings flow [IoT Core](../aws-iot/iot-core.md) → Firehose → S3.
- KDS → Firehose → S3: the stream feeds real-time consumers, and Firehose archives the same records to the lake as Parquet files, which Athena and QuickSight use the next day.

## Related

- [kinesis-data-streams.md](kinesis-data-streams.md): Firehose can read from a Kinesis data stream and archive the same records to S3, while real-time consumers read the stream directly (KDS → Firehose → S3).
- [s3.md](../aws-general-services/s3.md): S3 is Firehose's most common destination; Firehose packs streaming records into files (for example Parquet) in the data lake.
- [redshift.md](redshift.md): Firehose delivers to Redshift by buffering records, writing them to S3, then running a `COPY` into Redshift.
- [iot-core.md](../aws-iot/iot-core.md): IoT Core routes device messages to Firehose, which delivers them to S3 (IoT Core → Firehose → S3).
- [athena.md](athena.md): Firehose's Parquet/ORC conversion makes later Athena queries scan less and cost less.
- [choosing-ingestion-services.md](../../aws-data-engineering/choosing-ingestion-services.md): compares Firehose with Kinesis Data Streams, MSK and Redshift streaming ingestion: Firehose delivers a stream to a destination with no code and no replay; KDS and MSK store the stream for your consumers; streaming ingestion lets Redshift read a stream itself with lower latency.
- [batch-and-streaming.md](../../../data-engineering/batch-and-streaming.md): Firehose is the "worker who packs items from the conveyor belt into boxes for the warehouse": it turns data in motion (a stream) into data at rest (files in the lake).
- [ingest-on-aws.md](../../aws-data-engineering/aws-data-pipeline/ingest-on-aws.md): Firehose is a stage 1 (ingest) service for real-time data streams.
- [exam-traps.md](../../aws-data-engineering/exam-traps.md): exam material may call this service Kinesis Data Firehose.
