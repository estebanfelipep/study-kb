# AWS Snow Family

AWS Snow Family: physical devices for moving huge or sensitive datasets into AWS offline.

## What it is

The AWS Snow Family is a set of **physical devices** for moving huge or sensitive data into AWS when network transfer isn't feasible because of volume or sensitivity.

## Characteristics

- For huge or sensitive data; offline batch ingest.
- Usual exam triggers: "petabytes", "limited bandwidth", "would take weeks over the network". _(added)_
- AWS no longer offers several Snow devices to new customers; it points to [DataSync](datasync.md) and the AWS Data Transfer Terminal instead. Exam questions may still feature Snowball. _(added; verify current status)_

## Example

- _(added)_ A company with petabytes of archives and poor connectivity ships the data on Snowball devices instead of transferring it over the network for weeks.

## Related

- [datasync.md](datasync.md): DataSync is the network alternative and the service AWS points to where Snow devices are no longer offered. Snow wins when the transfer would take weeks over the network.
- [choosing-ingestion-services.md](../../aws-data-engineering/choosing-ingestion-services.md): compares Snow Family with DataSync: petabytes, limited bandwidth or weeks over the network point to Snow.
- [exam-traps.md](../../aws-data-engineering/exam-traps.md): the trap is availability. AWS no longer offers several Snow devices to new customers, but exam questions may still feature Snowball.
