# Choosing ingestion services

This file holds the comparisons and exam pick-rules for getting data into AWS: databases, files, streams and devices, plus zero-ETL loading into Redshift.

Service details are in each service's file in [aws-services](../aws-services/aws-services.md).

## Matching services to sources and ingest modes

Data discovery step 3 ([data-discovery.md](../../data-engineering/data-discovery.md)) classifies sources by **data source** and **ingest mode** ([batch-and-streaming.md](../../data-engineering/batch-and-streaming.md)):

| Data source | Ingest mode | Service |
| --- | --- | --- |
| Databases (CRM, ERP, CMS) | Batch (full load) or ongoing (change data capture) | [DMS](../aws-services/aws-databases/dms.md) |
| Logs, clickstreams, app events | Streaming / near real time | [Data Firehose](../aws-services/aws-analytics/data-firehose.md) |
| Logs, events, high-throughput streams needing Kafka | Streaming | [MSK](../aws-services/aws-analytics/msk.md) |
| IoT devices | Streaming | [IoT Core](../aws-services/aws-iot/iot-core.md) (often → Firehose → S3) |
| On-premises files, object storage, Hadoop | Batch, scheduled | [DataSync](../aws-services/aws-migration-and-transfer/datasync.md) |
| Partners and vendors sending files | Batch | [Transfer Family](../aws-services/aws-migration-and-transfer/transfer-family.md) |
| Petabytes, poor connectivity, or sensitive data | Offline batch | [Snow Family](../aws-services/aws-migration-and-transfer/snow-family.md) |

## If the question says… pick

| If the question says… | Pick | Not |
| --- | --- | --- |
| "Migrate or replicate a **database**", "change data capture" | **DMS** | DataSync (files, not databases) |
| "Deliver streaming data to S3/Redshift, **no servers to manage**", "convert to Parquet" | **Data Firehose** | MSK (you manage Kafka topics and consumers) |
| "**Apache Kafka**", "existing Kafka applications" | **MSK** | Firehose |
| "On-premises **NFS/SMB** file shares", "**HDFS**", "scheduled sync" | **DataSync** | Transfer Family |
| "Partners upload via **SFTP**", "keep existing FTP workflows" | **Transfer Family** | DataSync |
| "**Petabytes**", "limited bandwidth", "would take weeks over the network" | **Snow Family** | DataSync |
| "Millions of **devices**", "MQTT" | **IoT Core** | Firehose directly |

## Kinesis Data Streams vs Data Firehose vs MSK

|  | **Kinesis Data Streams** | **Data Firehose** | **Amazon MSK** |
| --- | --- | --- | --- |
| Job | **Stores** the stream so apps can **process** it | **Delivers** the stream to a destination | **Stores** the stream (Apache Kafka) |
| Consumers | Your code: Lambda, Flink, custom apps | None to write; loads into S3, Redshift, OpenSearch, Splunk and more | Kafka consumers |
| Latency | **Real time** (~70–200 ms) | **Near real time** (buffers seconds to minutes) | Real time |
| Storage and replay | **Yes**, 24 h to 365 days | **No**, data passes through | **Yes**, configurable |
| Transformation | You write it in the consumer | Built in: Parquet/ORC conversion, Lambda transforms | You write it |
| Management | On-demand or provisioned shards | Fully managed | Managed Kafka clusters (or MSK Serverless) |

**Often combined:** KDS → Firehose → S3. The stream feeds real-time consumers, and Firehose archives the same records to the lake.

## Kinesis Data Streams vs S3

|  | **Kinesis Data Streams** | **S3 bucket** |
| --- | --- | --- |
| Model | **Data in motion** | **Data at rest** |
| Unit | **Small records** (≤ 1 MB, usually KB) | **Objects** (bytes up to 5 TB) |
| Writing | **Append** records continuously, thousands per second | **Upload whole objects**; no appending |
| Reading | **In order, by position** (ms latency) | **By key**, any object, any time |
| Order | Guaranteed **per shard** | No order between objects |
| Retention | **Temporary**: 24 h to 365 days | **Indefinite**, until deleted or moved by a lifecycle rule |
| Cost model | Per shard-hour or throughput, plus retention | Per GB stored plus requests |
| Purpose | **React now** | **Keep everything** |

The vendor-neutral version is in [batch-and-streaming.md](../../data-engineering/batch-and-streaming.md).

## Loading Redshift

### Streaming ingestion vs Firehose → Redshift

- **Firehose → Redshift:** Firehose buffers records, writes them to S3, then runs a `COPY` into Redshift. More latency (minutes) and more moving parts, but you also get a copy in S3.
- **Streaming ingestion:** Redshift reads the stream itself. Lower latency (seconds), fewer components, nothing staged in S3.

### Auto copy vs other options

- **Manual or scheduled `COPY`:** you decide when to load and track which files are done yourself.
- **Auto copy:** Redshift watches S3 and tracks files for you. Use it for **files** that arrive over time.
- **Streaming ingestion:** for **streams** (Kinesis, MSK), not files.

### Aurora zero-ETL vs DMS vs a Glue ETL job

|  | **Zero-ETL integration** | **AWS DMS** | **Glue ETL job** |
| --- | --- | --- | --- |
| Effort | Configure once, no code | Configure tasks and replication instances | Write and schedule jobs |
| Latency | Seconds | Seconds to minutes (CDC) | Batch (hours) |
| Transformation | None in flight (model later in Redshift) | Light (mappings, filters) | Full (any Spark logic) |
| Sources and targets | Specific supported pairs (Aurora/RDS/DynamoDB → Redshift and others) | Many databases → many targets | Anything Glue can connect to |
| Pick it when | Supported source, near real-time analytics, least effort | Migrations or unsupported source/target pairs | Data needs heavy cleaning or joining first |

## DMS vs DataSync

**DMS moves a database's data. DataSync moves files.** DMS understands tables, rows and transactions; DataSync sees only files and folders.

|  | **DMS** | **DataSync** |
| --- | --- | --- |
| What it moves | Rows from database tables | Files and objects, as they are |
| Typical sources | RDS, Aurora, on-premises Oracle, SQL Server, MySQL, MongoDB | On-premises NFS/SMB shares, object storage, HDFS |
| How it reads | Queries the tables (full load), then reads the change log (CDC) | Walks the file system and copies new or changed files |
| Keeping current | Continuously, seconds to minutes | On a schedule (batch) |
| What lands in S3 | New files built from rows: `LOAD` files plus `Op`-column change files | The same files that were on the share |

Analogy: DataSync is a mover copying the documents in a filing cabinet without reading them. DMS is a clerk who copies the accounts ledger once, then writes down every new entry as it's made.

## DMS vs an RDS read replica

Both keep a copy of an RDS database current, but for different reasons.

- **RDS read replica:** a second, live database kept in sync. Apps can connect to it, to spread read traffic or to fail over. Nothing lands in the lake.
- **DMS to S3:** files in the lake (a snapshot plus a log of changes). No app can connect to it; it exists for analytics, next to every other source.

"Offload reads" or "failover" points to a read replica. "Get the database into the data lake" points to DMS.

## Getting RDS data into S3

The concept, including why the CDC files need a merge step, is in [replicating-databases-to-the-lake.md](../../data-engineering/replicating-databases-to-the-lake.md). Loading Redshift directly with zero-ETL is covered in the section above.

| Way | AWS service | Pick it when |
| --- | --- | --- |
| Full load + CDC | [DMS](../aws-services/aws-databases/dms.md) | The lake must stay close to current |
| Scheduled snapshot over JDBC | [Glue](../aws-services/aws-analytics/glue.md) job | Daily snapshots are enough, or data needs heavy transformation on the way |
| Snapshot export | [RDS](../aws-services/aws-databases/rds.md) snapshot export to S3 (Parquet) | Occasional bulk copies, with no load on the live database |
| No copy | [Athena](../aws-services/aws-analytics/athena.md) federated query | Occasional queries only; it loads production |

