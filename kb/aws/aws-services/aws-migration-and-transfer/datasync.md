# AWS DataSync

AWS DataSync: transferring on-premises file shares, object storage and Hadoop clusters to AWS storage.

## What it is

AWS DataSync transfers data from on-premises file shares, object storage and Hadoop clusters to AWS storage services. It's the ingestion service for on-premises files.

## Characteristics

- Sources: on-premises file shares, object storage and Hadoop clusters.
- Can **sync on a schedule**.
- Ingest mode: batch, scheduled. _(added)_
- For files, not databases. _(added)_
- Usual exam triggers: "on-premises NFS/SMB file shares", "HDFS", "scheduled sync". _(added)_
- AWS points to DataSync (and the AWS Data Transfer Terminal) for transfers where several Snow devices are no longer offered. _(added; verify current status)_

## Example

- _(added)_ A nightly scheduled DataSync task copies new files from an on-premises NFS share into the S3 data lake.

## Related

- [snow-family.md](snow-family.md): both move on-premises data into AWS. DataSync goes over the network; Snow Family ships physical devices when the data is too large or the bandwidth too limited. AWS points to DataSync where Snow devices are no longer offered.
- [transfer-family.md](transfer-family.md): both move files into AWS. DataSync syncs your own on-premises file shares, object storage and HDFS; Transfer Family receives files partners send over SFTP, FTPS or FTP.
- [dms.md](../aws-databases/dms.md): DataSync moves files (NFS/SMB shares, object storage, HDFS), while DMS moves databases, including ongoing changes with CDC. "Replicate a database" points to DMS, not DataSync.
- [s3.md](../aws-general-services/s3.md): DataSync copies on-premises files into AWS storage such as the S3 data lake.
- [choosing-ingestion-services.md](../../aws-data-engineering/choosing-ingestion-services.md): compares DataSync with DMS, Transfer Family and Snow Family: NFS/SMB/HDFS and scheduled sync point to DataSync.
- [aws-data-pipeline.md](../../aws-data-engineering/aws-data-pipeline.md): DataSync is the ingest-stage service for on-premises files.
