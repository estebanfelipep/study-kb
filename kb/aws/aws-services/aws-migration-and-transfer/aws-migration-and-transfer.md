# aws-migration-and-transfer — index

Moving files and bulk data into AWS from on premises and partners.

## How to read this folder

- **Before:** Batch ingest, in [batch-and-streaming.md](../../../data-engineering/batch-and-streaming.md).
- **Order:** From the most common case to the most special: your own files over the network, then partner files, then offline devices.
- **After:** [choosing-ingestion-services.md](../../aws-data-engineering/choosing-ingestion-services.md).

## Files (in reading order)

- [datasync.md](datasync.md): AWS DataSync: scheduled transfer of on-premises files, object storage and HDFS. Read when: you need to move on-premises files into AWS.
- [transfer-family.md](transfer-family.md): AWS Transfer Family: SFTP/FTPS/FTP/AS2 transfers into and out of S3. Read when: partners or vendors send files over file transfer protocols.
- [snow-family.md](snow-family.md): AWS Snow Family: physical devices for offline transfer, and their availability. Read when: data is too large or sensitive to send over the network.
