# Amazon Managed Service for Apache Flink

This file covers Amazon Managed Service for Apache Flink: real-time stream processing on AWS, with an example.

## What it is

Managed Service for Apache Flink processes streaming data in **real time**. You can **quickly author SQL** that **filters, aggregates, joins and derives** data from a stream. In the pipeline it's a **processing** service, and it's the real-time counterpart to batch processing in Glue and EMR.

Exam material may use the older name **Kinesis Data Analytics**.

## Characteristics

- Works in **real time**, not batch.
- Supports **Java, Scala and Python** as well as SQL _(added)_.
- Typically reads from [Kinesis Data Streams](kinesis-data-streams.md) or [MSK](msk.md), and computes things like **windowed aggregations** (for example, per 1-minute window) _(added)_.
- Fully managed: AWS runs the Flink infrastructure _(added)_.

## Example

_(added)_ A video service needs to monitor playback quality. Every player sends a heartbeat event to Kinesis Data Streams every few seconds. Managed Service for Apache Flink reads the stream and, for each 1-minute window, computes the buffering rate per region and CDN. If one region spikes, a Lambda consumer pages the on-call team through SNS.

## Related

- [kinesis-data-streams.md](kinesis-data-streams.md): Flink's usual source: it reads records from a Kinesis data stream and processes them in real time.
- [msk.md](msk.md): Flink can also read from an MSK (Kafka) topic.
- [glue.md](glue.md): Glue and EMR process data in batch; Flink is the real-time counterpart for streams.
- [choosing-storage-and-processing-services.md](../../aws-data-engineering/choosing-storage-and-processing-services.md): compares Flink with Glue and EMR: pick Flink when the question says "real-time", "windowed aggregations on a stream" or "Apache Flink"; Glue for serverless ETL; EMR for existing Spark/Hadoop and cluster control.
- [aws-data-pipeline.md](../../aws-data-engineering/aws-data-pipeline.md): Flink is the real-time service in stage 4 (process).
- [batch-and-streaming.md](../../../data-engineering/batch-and-streaming.md): Flink processes data in motion as described here, consuming a stream record by record instead of reading stored files.
- [exam-traps.md](../../aws-data-engineering/exam-traps.md): exam material may call this service Kinesis Data Analytics.
