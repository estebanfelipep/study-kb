# Batch and streaming

This file covers the three ingest modes (batch, micro-batch, streaming), what a data stream is, and the difference between data in motion and data at rest.

## Ingest modes

| Mode | Examples |
| --- | --- |
| **Streaming** (continuous) | Sensors, social media platforms, media and entertainment services, IoT devices |
| **Micro-batch** (small, frequent batches) | Sensors, website logs, graphics and video rendering |
| **Batch** (large, scheduled loads) | Medical imagery, genomic data, financial records, usage data |

The parenthetical definitions are _(added)_. Sensors appear under both streaming and micro-batch: the same source can be ingested either way.

## What a stream is _(added)_

A **stream** is a **continuous, never-ending, ordered sequence of small records** (events), appended as things happen. It's like a log that only grows at the end: every click, sensor reading or transaction becomes one record.

A stream record usually has:

| Part | What it is |
| --- | --- |
| **Payload** | The data itself, treated by the stream as opaque bytes |
| **Partition key** | Chosen by the producer (for example, `user_id`). Decides which partition (shard) the record goes to, so one key's records stay in order |
| **Sequence number or offset** | The record's position; order is guaranteed **within a partition** |
| **Timestamp** | When the record arrived |

**Structured, semi-structured or unstructured?** Any of them, because the payload is just bytes. In practice stream data is mostly **semi-structured**: small JSON events such as `{"user":"42","action":"click","ts":"..."}`. Large files (video, images) belong in object storage.

Streams are **temporary**: records expire after a retention period, not because someone read them. Consumers read **by position**, each keeping its own position, so several consumers can read the same records and any of them can **replay** older ones.

How AWS implements this is in [kinesis-data-streams.md](../aws/aws-services/aws-analytics/kinesis-data-streams.md) and [msk.md](../aws/aws-services/aws-analytics/msk.md).

## Data in motion vs data at rest _(added)_

|  | **Stream (data in motion)** | **Object storage (data at rest)** |
| --- | --- | --- |
| Model | A flowing sequence of events | A collection of stored objects |
| Unit | Small records (usually KB) | Objects or files (bytes to TB) |
| Writing | **Append** records continuously | **Upload whole objects** |
| Reading | **In order, by position**, as data arrives | **By key**, any object, any time |
| Order | Guaranteed per partition | No order between objects |
| Retention | Temporary | Indefinite, until deleted |
| Purpose | **React now**: real-time processing, alerts, dashboards | **Keep everything**: the data lake, history, later analytics |

**Analogy:** a stream is a **conveyor belt**: items pass in order, several workers can each look at every item, and anything not picked up eventually falls off the end. Object storage is the **warehouse**: items sit on labeled shelves for as long as you want and can be fetched in any order. A delivery service (such as Amazon Data Firehose) is the worker who packs items from the belt into boxes for the warehouse.

## Streams vs queues _(added)_

Both buffer data between producers and consumers.

- **Queue:** each message is a **job** for **one** consumer and is **deleted** once processed. No replay.
- **Stream:** each record is an **event** that **many** consumers can read, in order per partition, and **replay** until it expires.

Queues are covered in [orchestration-and-automation.md](orchestration-and-automation.md).

## Related

- [data-discovery.md](data-discovery.md): in discovery step 3, every data source is classified by data type, data source and **ingest mode**. The ingest modes defined here are that third line, and they decide which ingestion service fits.
- [choosing-ingestion-services.md](../aws/aws-data-engineering/choosing-ingestion-services.md): maps each source and ingest mode to an AWS service. Streaming goes to Firehose, MSK or IoT Core, scheduled batch files to DataSync, and offline batch to Snow Family. It also compares Kinesis (a stream) with S3 (data at rest).
