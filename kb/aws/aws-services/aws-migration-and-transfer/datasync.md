# AWS DataSync

AWS DataSync: transferring on-premises file shares, object storage and Hadoop clusters to AWS storage.

## Sources

- [AWS DataSync User Guide](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html): the official guide.
- [AWS DataSync FAQs](https://aws.amazon.com/datasync/faqs/): frequently asked questions.

## What it is

AWS DataSync transfers data from on-premises file shares, object storage and Hadoop clusters to AWS storage services. It's the ingestion service for on-premises files.

It's optimized for moving **large volumes of file-based and object data** to, from and between AWS storage services, on-premises storage and edge locations.

## Characteristics

- Sources: on-premises file shares, object storage and Hadoop clusters.
- Can **sync on a schedule**.
- Ingest mode: batch, scheduled.
- For files, not databases.
- Also copies between AWS storage services, such as S3, EFS and FSx.
- **Kinds of file data it's built for:** content repositories (home directories, project files, digital archives), media libraries (video, audio, images), research, engineering and simulation files, and log files or file-based backups from enterprise applications.
- **A DataSync agent** is deployed on premises, next to the storage, and registered with the DataSync service. The agent reads the files and copies them to AWS securely.
- **A task** pairs a **source location** (such as a folder on an on-premises NAS) with a **destination location** (such as an S3 bucket and prefix), and can run on a schedule.
- **Incremental loads:** a scheduled task copies only what's new or changed since the last run.
- DataSync **scales automatically** and handles **scheduling, monitoring, encryption and verification** of transfers.
- **Pricing:** pay per amount of data copied, with no minimum commitments or upfront fees.
- Usual exam triggers: "on-premises NFS/SMB file shares", "HDFS", "scheduled sync".
- AWS points to DataSync (and the AWS Data Transfer Terminal) for transfers where several Snow devices are no longer offered.

## Example

- A nightly scheduled DataSync task copies new files from an on-premises NFS share into the S3 data lake.
- Example Corp's agent copies the `website_clicks` folder from an on-premises NAS to the S3 raw bucket under the `website_clicks` prefix, incrementally, every hour:

  ```
  on premises                              AWS
  NAS: /website_clicks ──► DataSync ══VPN══► S3 raw bucket
                           agent              website_clicks/
                           (hourly, only new or changed files)
  ```

  The whole scenario is in [example-corp-ingest-on-aws.md](../../aws-data-engineering/aws-data-pipeline/example-corp-ingest-on-aws.md).

## Related

- [snow-family.md](snow-family.md): both move on-premises data into AWS. DataSync goes over the network; Snow Family ships physical devices when the data is too large or the bandwidth too limited. AWS points to DataSync where Snow devices are no longer offered.
- [transfer-family.md](transfer-family.md): both move files into AWS. DataSync syncs your own on-premises file shares, object storage and HDFS; Transfer Family receives files partners send over SFTP, FTPS or FTP.
- [dms.md](../aws-databases/dms.md): DataSync moves files (NFS/SMB shares, object storage, HDFS), while DMS moves databases, including ongoing changes with CDC. "Replicate a database" points to DMS, not DataSync.
- [s3.md](../aws-general-services/s3.md): DataSync copies on-premises files into AWS storage such as the S3 data lake.
- [choosing-ingestion-services.md](../../aws-data-engineering/choosing-ingestion-services.md): compares DataSync with DMS, Transfer Family and Snow Family: NFS/SMB/HDFS and scheduled sync point to DataSync.
- [ingest-on-aws.md](../../aws-data-engineering/aws-data-pipeline/ingest-on-aws.md): DataSync is the ingest-stage service for on-premises files.
- [example-corp-ingest-on-aws.md](../../aws-data-engineering/aws-data-pipeline/example-corp-ingest-on-aws.md): DataSync copies Example Corp's website clicks from an on-premises NAS into the raw zone every hour.
- [site-to-site-vpn.md](../aws-networking/site-to-site-vpn.md): a Site-to-Site VPN encrypts the path the DataSync agent copies files over, from the data center to AWS.
