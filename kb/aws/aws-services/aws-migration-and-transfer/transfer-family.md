# AWS Transfer Family

AWS Transfer Family: managed SFTP, FTPS, FTP and AS2 file transfers into and out of S3.

## What it is

AWS Transfer Family automates file transfers into and out of S3 over file transfer protocols. It's the ingestion service when partners and vendors send files.

## Characteristics

- Protocols: **SFTP, FTPS, FTP and AS2**. (the course text lists "SFTP, FTPS, and SFTP")
- Transfers **into and out of S3**.
- Ingest mode: batch.
- Usual exam triggers: "partners upload via SFTP", "keep existing FTP workflows".

## Example

- A partner uploads `orders_2026-10-18.csv` over SFTP. Transfer Family writes it to an S3 bucket, and the upload event invokes a [Lambda](../aws-compute/lambda.md) function that validates and converts it.

## Related

- [s3.md](../aws-general-services/s3.md): Transfer Family writes partner files into S3 and serves files out of S3.
- [lambda.md](../aws-compute/lambda.md): once Transfer Family writes a file to S3, the upload event can invoke a Lambda function that validates and converts it.
- [datasync.md](datasync.md): both move files. Transfer Family receives files partners send over file transfer protocols; DataSync syncs your own on-premises shares.
- [choosing-ingestion-services.md](../../aws-data-engineering/choosing-ingestion-services.md): compares Transfer Family with DataSync: partners uploading over SFTP, or keeping existing FTP workflows, point to Transfer Family.
- [exam-traps.md](../../aws-data-engineering/exam-traps.md): the course text lists the protocols as "SFTP, FTPS, and SFTP"; the actual list is SFTP, FTPS, FTP and AS2.
