# Amazon EMR

Amazon EMR: managed big data clusters for open-source frameworks, including EMR Serverless.

## What it is

Amazon EMR runs big data processing with open-source frameworks such as Spark, Hadoop, Hive, Presto and Flink. It processes ingested data (data engineer function 3, Prepare) and also serves as a delivery engine, running those frameworks on large datasets in S3 and DynamoDB. It's used for log analysis, machine learning, data science, web indexing and scientific simulations.

## Characteristics

- Runs on **customized EC2 clusters, EKS, Outposts or EMR Serverless**.
- Runs **batch jobs**. Petabyte-scale batch.
- **Full control** over the cluster on EC2: instance types, Spot, configuration, SSH, custom software, long-running clusters.
- **Managed scaling** resizes an EMR on EC2 cluster to the workload, within limits you set.
- The **Spark UI** shows a job's processing flow, to find bottlenecks.
- Wider range of frameworks than Glue: Spark, Hive, Presto, HBase, Flink and more.
- **Apache Spark** is the distributed engine EMR runs most often, for data too big for one machine. How it works, with a worked example, is in [apache-spark.md](../../../data-engineering/apache-spark.md).
- Reads table definitions from the [Glue Data Catalog](glue.md).
- Ingests into **Apache Iceberg** tables in batch or streaming, and reads them. A common place to build an **Apache Hudi** lake.
- Usual exam triggers: existing Spark/Hadoop/Hive/Presto jobs, migrating on-premises Hadoop.
- Run clusters in private subnets of a [VPC](../aws-networking/vpc.md).

### EMR Serverless

- You don't have to configure, optimize, secure or operate clusters, and you avoid over- or under-provisioning resources for data processing jobs.
- You create an **application** (Spark or Hive) and submit jobs. Workers are allocated per job and released when it finishes.
- Pay for the vCPU, memory and storage used while jobs run.
- Optional **pre-initialized capacity** keeps workers warm, so jobs start faster.
- Open-source Spark experience, closer to the frameworks than Glue. Best for existing big-data code and data science workloads.

## Example

- A data science team runs a Spark feature-engineering job on 3 TB of clickstream data once a day, plus occasional backfills. On EMR on EC2 they had to size, start, stop and tune a cluster. On EMR Serverless they submit the same Spark code; it scales up for the run, down to zero afterward, and much larger for a backfill with no cluster changes.

## Related

- [glue.md](glue.md): EMR and Glue both run Apache Spark; EMR reads table definitions from the Glue Data Catalog, and Glue is the serverless, more opinionated alternative for ETL.
- [s3.md](../aws-general-services/s3.md): EMR processes and analyzes large datasets stored in S3 (and DynamoDB), usually writing results back to the lake.
- [vpc.md](../aws-networking/vpc.md): EMR clusters run in private subnets of a VPC so they aren't exposed publicly.
- [choosing-storage-and-processing-services.md](../../aws-data-engineering/choosing-storage-and-processing-services.md): compares EMR on EC2, EMR Serverless and Glue: EMR on EC2 gives full cluster control and the widest set of frameworks; EMR Serverless runs existing Spark/Hive code with no clusters; Glue is serverless ETL integrated with the catalog.
- [choosing-delivery-services.md](../../aws-data-engineering/choosing-delivery-services.md): EMR is the delivery pick when a question says "Spark/Hive/Presto" or "full control" for analyzing data, rather than SQL on S3 (Athena) or a warehouse (Redshift).
- [aws-data-pipeline.md](../../aws-data-engineering/aws-data-pipeline/aws-data-pipeline.md): EMR appears in two stages: stage 4 (process, batch) and stage 5 (deliver, for data scientists and engineers).
- [zero-etl-and-serverless-on-aws.md](../../aws-data-engineering/zero-etl-and-serverless-on-aws.md): EMR Serverless is the serverless option for Spark/Hive processing, replacing EMR on EC2 clusters.
- [transactional-data-lake-on-aws.md](../../aws-data-engineering/transactional-data-lake-on-aws.md): EMR ingests into and consumes the Iceberg tables of a transactional data lake.
- [apache-spark.md](../../../data-engineering/apache-spark.md): the engine EMR runs most often: what Spark is for, how it splits a job across executors, and a worked example.
- [troubleshooting-data-lakes-on-aws.md](../../aws-data-engineering/troubleshooting-data-lakes-on-aws.md): rightsizing EMR Serverless workers and EC2 instances, managed scaling, and reading the Spark UI for slow jobs.
