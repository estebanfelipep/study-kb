# Study KB — index

Start here. This file is the map of the KB's **topics**: the subjects people ask about, each of which may span several folders. To answer a question, read only as deep as you need to:

1. Find the topic, or topics, the question is about.
2. Open the files that topic lists. They may sit in different folders.
3. For more context, read the index of the folder a file sits in (`<folder>/<folder>.md`). It lists that file's neighbors.

## How to study

The topics below are in study order: the role, how a project starts, the pipeline, then one stage per topic, then what cuts across stages.

- **From scratch:** read the topics top to bottom. Inside a topic, the files are listed concept first, then the AWS track file, then services. Stop at the service files once you have what you need.
- **Revising for DEA-C01:** go straight to "DEA-C01 exam prep".
- **Side path:** "Serverless web apps and APIs" isn't part of the data pipeline.

## Topics

- **The data engineer role**: what a data engineer does, the six functions, and the people they work with. Read when: a question is about the job itself, its responsibilities or its stakeholders.
  - [data-engineer-role.md](data-engineering/data-engineer-role.md)
  - [data-personas.md](data-engineering/data-personas.md)
  - [aws-data-pipeline.md](aws/aws-data-engineering/aws-data-pipeline.md)
- **Data discovery**: how a data project starts, its five steps, and how data is classified by type, source and ingest mode. Read when: scoping a data project, or classifying data.
  - [data-discovery.md](data-engineering/data-discovery.md)
  - [batch-and-streaming.md](data-engineering/batch-and-streaming.md)
- **Data pipeline architecture**: data silos, the modern data architecture, and the five stages (ingest, store, catalog, process, deliver) on any vendor and on AWS. Read when: you need the overall flow of data, or which services belong to which stage.
  - [modern-data-architecture.md](data-engineering/modern-data-architecture.md)
  - [aws-data-pipeline.md](aws/aws-data-engineering/aws-data-pipeline.md)
- **Data ingestion and streaming**: ingest modes, streams, and the AWS services that bring data in. Read when: a question is about getting data into the lake, or real-time streams.
  - [batch-and-streaming.md](data-engineering/batch-and-streaming.md)
  - [choosing-ingestion-services.md](aws/aws-data-engineering/choosing-ingestion-services.md)
  - [kinesis-data-streams.md](aws/aws-services/aws-analytics/kinesis-data-streams.md)
  - [data-firehose.md](aws/aws-services/aws-analytics/data-firehose.md)
  - [msk.md](aws/aws-services/aws-analytics/msk.md)
  - [dms.md](aws/aws-services/aws-databases/dms.md)
  - [datasync.md](aws/aws-services/aws-migration-and-transfer/datasync.md)
  - [transfer-family.md](aws/aws-services/aws-migration-and-transfer/transfer-family.md)
  - [snow-family.md](aws/aws-services/aws-migration-and-transfer/snow-family.md)
  - [iot-core.md](aws/aws-services/aws-iot/iot-core.md)
- **Data storage**: data lakes, warehouses, OLTP vs OLAP, columnar formats, and the AWS stores. Read when: deciding where data lives, or how a lake differs from a warehouse or a database.
  - [data-lakes-and-warehouses.md](data-engineering/data-lakes-and-warehouses.md)
  - [choosing-storage-and-processing-services.md](aws/aws-data-engineering/choosing-storage-and-processing-services.md)
  - [s3.md](aws/aws-services/aws-general-services/s3.md)
  - [redshift.md](aws/aws-services/aws-analytics/redshift.md)
  - [rds.md](aws/aws-services/aws-databases/rds.md)
  - [dynamodb.md](aws/aws-services/aws-databases/dynamodb.md)
- **Data catalogs**: what a catalog holds, technical vs business metadata, and the Glue Data Catalog, crawlers and DataZone. Read when: making lake data findable, or tracking schemas.
  - [modern-data-architecture.md](data-engineering/modern-data-architecture.md)
  - [glue.md](aws/aws-services/aws-analytics/glue.md)
  - [datazone.md](aws/aws-services/aws-analytics/datazone.md)
  - [lake-formation.md](aws/aws-services/aws-analytics/lake-formation.md)
- **Data processing and transformation**: types of transformation, and the AWS ETL and big data engines. Read when: a question is about the T in ETL, Spark, or real-time stream processing.
  - [modern-data-architecture.md](data-engineering/modern-data-architecture.md)
  - [choosing-storage-and-processing-services.md](aws/aws-data-engineering/choosing-storage-and-processing-services.md)
  - [glue.md](aws/aws-services/aws-analytics/glue.md)
  - [emr.md](aws/aws-services/aws-analytics/emr.md)
  - [managed-service-for-apache-flink.md](aws/aws-services/aws-analytics/managed-service-for-apache-flink.md)
- **Analytics and data delivery**: serving data to consumers through SQL, warehouses, search, dashboards and ML. Read when: a question is about how analysts, scientists or apps query or see data.
  - [choosing-delivery-services.md](aws/aws-data-engineering/choosing-delivery-services.md)
  - [athena.md](aws/aws-services/aws-analytics/athena.md)
  - [redshift.md](aws/aws-services/aws-analytics/redshift.md)
  - [opensearch-service.md](aws/aws-services/aws-databases/opensearch-service.md)
  - [quicksight.md](aws/aws-services/aws-analytics/quicksight.md)
  - [sagemaker.md](aws/aws-services/aws-ai/sagemaker.md)
- **Orchestration and event-driven pipelines**: automation vs orchestration, messaging patterns, and the AWS workflow, event and messaging services. Read when: coordinating, triggering, scheduling or decoupling pipeline steps.
  - [orchestration-and-automation.md](data-engineering/orchestration-and-automation.md)
  - [choosing-orchestration-services.md](aws/aws-data-engineering/choosing-orchestration-services.md)
  - [step-functions.md](aws/aws-services/aws-application-coordination/step-functions.md)
  - [mwaa.md](aws/aws-services/aws-application-coordination/mwaa.md)
  - [eventbridge.md](aws/aws-services/aws-application-coordination/eventbridge.md)
  - [lambda.md](aws/aws-services/aws-compute/lambda.md)
  - [sns.md](aws/aws-services/aws-application-coordination/sns.md)
  - [sqs.md](aws/aws-services/aws-application-coordination/sqs.md)
- **Zero-ETL and serverless**: avoiding ETL pipelines and infrastructure, and the AWS services that do it. Read when: a question asks for the least operational overhead or near real-time data without pipelines.
  - [orchestration-and-automation.md](data-engineering/orchestration-and-automation.md)
  - [zero-etl-and-serverless-on-aws.md](aws/aws-data-engineering/zero-etl-and-serverless-on-aws.md)
- **Data security and governance**: security vs governance, the CIA triad, the five security areas, best practices, and the AWS services for each. Read when: a question is about access, encryption, PII, compliance, network protection or auditing.
  - [data-security-and-monitoring.md](data-engineering/data-security-and-monitoring.md)
  - [security-and-monitoring-on-aws.md](aws/aws-data-engineering/security-and-monitoring-on-aws.md)
  - [choosing-security-and-monitoring-services.md](aws/aws-data-engineering/choosing-security-and-monitoring-services.md)
  - [iam.md](aws/aws-services/aws-identity/iam.md)
  - [lake-formation.md](aws/aws-services/aws-analytics/lake-formation.md)
  - [datazone.md](aws/aws-services/aws-analytics/datazone.md)
  - [kms.md](aws/aws-services/aws-security/kms.md)
  - [acm.md](aws/aws-services/aws-apis/acm.md)
  - [macie.md](aws/aws-services/aws-security/macie.md)
  - [audit-manager.md](aws/aws-services/aws-security/audit-manager.md)
  - [config.md](aws/aws-services/aws-monitoring/config.md)
  - [control-tower.md](aws/aws-services/aws-security/control-tower.md)
  - [cloudtrail.md](aws/aws-services/aws-monitoring/cloudtrail.md)
  - [vpc.md](aws/aws-services/aws-networking/vpc.md)
  - [guardduty.md](aws/aws-services/aws-security/guardduty.md)
  - [waf.md](aws/aws-services/aws-security/waf.md)
  - [shield.md](aws/aws-services/aws-security/shield.md)
- **Monitoring**: what to monitor in a data system, best practices, and the AWS monitoring and dashboard services. Read when: a job, pipeline or resource needs metrics, alarms, traces or dashboards.
  - [data-security-and-monitoring.md](data-engineering/data-security-and-monitoring.md)
  - [security-and-monitoring-on-aws.md](aws/aws-data-engineering/security-and-monitoring-on-aws.md)
  - [choosing-security-and-monitoring-services.md](aws/aws-data-engineering/choosing-security-and-monitoring-services.md)
  - [cloudwatch.md](aws/aws-services/aws-monitoring/cloudwatch.md)
  - [x-ray.md](aws/aws-services/aws-monitoring/x-ray.md)
  - [systems-manager.md](aws/aws-services/aws-monitoring/systems-manager.md)
  - [managed-grafana.md](aws/aws-services/aws-monitoring/managed-grafana.md)
  - [cloudtrail.md](aws/aws-services/aws-monitoring/cloudtrail.md)
- **Serverless web apps and APIs**: static websites on S3 and APIs in front of Lambda. Read when: building a front end or an API without servers.
  - [s3.md](aws/aws-services/aws-general-services/s3.md)
  - [api-gateway.md](aws/aws-services/aws-apis/api-gateway.md)
  - [lambda.md](aws/aws-services/aws-compute/lambda.md)
  - [dynamodb.md](aws/aws-services/aws-databases/dynamodb.md)
- **DEA-C01 exam prep**: exam keywords, pick-rules per stage, older service names, and course errata. Read when: revising for the AWS Certified Data Engineer – Associate exam.
  - [choosing-ingestion-services.md](aws/aws-data-engineering/choosing-ingestion-services.md)
  - [choosing-storage-and-processing-services.md](aws/aws-data-engineering/choosing-storage-and-processing-services.md)
  - [choosing-delivery-services.md](aws/aws-data-engineering/choosing-delivery-services.md)
  - [choosing-orchestration-services.md](aws/aws-data-engineering/choosing-orchestration-services.md)
  - [choosing-security-and-monitoring-services.md](aws/aws-data-engineering/choosing-security-and-monitoring-services.md)
  - [exam-traps.md](aws/aws-data-engineering/exam-traps.md)

## Subjects

- [aws](aws/aws.md): Amazon Web Services, one file per service, and the AWS certification tracks being studied.
- [data-engineering](data-engineering/data-engineering.md): vendor-neutral data engineering concepts.

## Reference

- [context.md](context.md): the glossary of terms and abbreviations. Read when: a term, acronym, or service nickname is unfamiliar, or two names might mean the same thing.
- [links.md](links.md): every external link in the KB, grouped by kind (official docs, courses, practice exams, videos). Read when: you need a URL, or want to know where a resource lives.
- [AGENTS.md](../AGENTS.md): how this KB is organized and run.
