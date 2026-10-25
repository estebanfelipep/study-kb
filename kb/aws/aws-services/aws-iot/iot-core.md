# AWS IoT Core

AWS IoT Core: ingesting data from IoT devices and routing it to AWS services.

## What it is

AWS IoT Core connects IoT devices to AWS and routes their messages to other AWS services. It's the ingestion service for the "IoT devices" data source (sensor data, device metadata, time-series data).

## Characteristics

- Connects **billions of devices** and routes **trillions of messages** to AWS services.
- Ingest mode: streaming. _(added)_
- Usual exam triggers: "millions of devices", "MQTT". _(added)_

## Example

- _(added)_ Sensor readings flow IoT Core → [Data Firehose](../aws-analytics/data-firehose.md) → S3, where they land in the data lake.

## Related

- [data-firehose.md](../aws-analytics/data-firehose.md): IoT Core often routes device messages to Firehose, which delivers them to S3.
- [data-discovery.md](../../../data-engineering/data-discovery.md): IoT Core is the ingestion service for the "IoT devices" data source defined there (sensor data, device metadata, time-series data).
- [batch-and-streaming.md](../../../data-engineering/batch-and-streaming.md): IoT devices are a streaming source, one of the ingest modes defined there.
- [choosing-ingestion-services.md](../../aws-data-engineering/choosing-ingestion-services.md): explains when to pick IoT Core rather than sending to Firehose directly: millions of devices and MQTT point to IoT Core.
- [aws-data-pipeline.md](../../aws-data-engineering/aws-data-pipeline.md): IoT Core is the ingest-stage service for IoT devices.
