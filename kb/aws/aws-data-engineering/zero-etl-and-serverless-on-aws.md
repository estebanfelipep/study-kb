# Zero-ETL and serverless on AWS

This file lists the AWS services the course names for zero-ETL and for serverless architectures, and what role each plays. The concepts are in [orchestration-and-automation.md](../../data-engineering/orchestration-and-automation.md).

Zero-ETL and serverless are the two technologies that make orchestration and automation more effective in data analytics workflows.

## Zero-ETL services

| Service | How it avoids ETL | Source → target |
| --- | --- | --- |
| [Athena](../aws-services/aws-analytics/athena.md) | Queries data where it sits | S3 (query in place) |
| [Redshift streaming ingestion](../aws-services/aws-analytics/redshift.md) | Reads streams directly; no S3 staging | Kinesis Data Streams / MSK → Redshift |
| [Aurora zero-ETL integration](../aws-services/aws-databases/rds.md) | Managed near real-time replication | Aurora → Redshift |
| [Redshift auto copy](../aws-services/aws-analytics/redshift.md) | Loads new files automatically | S3 → Redshift |
| [OpenSearch zero-ETL with S3](../aws-services/aws-databases/opensearch-service.md) | Queries data where it sits | S3 (query from OpenSearch) |

AWS has extended zero-ETL integrations to more sources, such as RDS for MySQL, DynamoDB and some SaaS applications into Redshift. Verify the current list. On the exam, "near real-time analytics on transactional data without building pipelines" points to **zero-ETL**.

## Serverless services

**Lambda is the primary serverless AWS service.** Many AWS services have serverless options or can be used in serverless workflows.

| Service | Serverless role | Closest non-serverless alternative |
| --- | --- | --- |
| [Lambda](../aws-services/aws-compute/lambda.md) | Run code | EC2, containers |
| [API Gateway](../aws-services/aws-apis/api-gateway.md) | Expose APIs | ALB + EC2 |
| [DynamoDB](../aws-services/aws-databases/dynamodb.md) | NoSQL database | RDS/Aurora (provisioned) |
| [S3](../aws-services/aws-general-services/s3.md) | File storage, static sites | EBS, EFS, web servers |
| [SNS](../aws-services/aws-application-coordination/sns.md) | Pub/sub notifications | Self-managed message broker |
| [SQS](../aws-services/aws-application-coordination/sqs.md) | Queues between steps | Self-managed queue (RabbitMQ) |
| [Redshift Serverless](../aws-services/aws-analytics/redshift.md) | Data warehouse | Provisioned Redshift |
| [EMR Serverless](../aws-services/aws-analytics/emr.md) | Spark/Hive processing | EMR on EC2 |
| [Glue](../aws-services/aws-analytics/glue.md) | Serverless ETL | EMR on EC2 |
| [MSK Serverless](../aws-services/aws-analytics/msk.md) | Kafka streaming | Provisioned MSK |
| [OpenSearch Serverless](../aws-services/aws-databases/opensearch-service.md) | Search and log analytics | OpenSearch managed domains |

How serverless and provisioned options compare is in [choosing-storage-and-processing-services.md](choosing-storage-and-processing-services.md) and [choosing-orchestration-services.md](choosing-orchestration-services.md).
