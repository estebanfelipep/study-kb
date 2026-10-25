# aws-data-engineering — index

This folder covers the AWS data engineering track and the AWS Certified Data Engineer – Associate (DEA-C01) exam: how AWS services map to the data pipeline, which service to pick when, and exam traps.

Read [aws-services](../aws-services/aws-services.md) instead for how an individual service works. Read [data-engineering](../../data-engineering/data-engineering.md) for concepts that hold regardless of vendor.

## How to read this folder

- **Before:** [data-engineering](../../data-engineering/data-engineering.md). Each file in the first group maps one of its concept files onto AWS.
- **Order:** first learn which services exist for each stage, then how to choose between them (one pipeline stage at a time, then the cross-cutting concerns), then revise.
- **After:** practice exams. Record mistakes in the matching `choosing-*` file or in `exam-traps.md`.

## Files (in reading order)

**Map the concepts to AWS**

- [aws-data-pipeline.md](aws-data-pipeline.md): the five pipeline stages, the data engineer's functions and the personas mapped to AWS services, plus AWS "lake" services and purpose-built databases. Read when: you need which AWS services belong to which stage or function.
- [zero-etl-and-serverless-on-aws.md](zero-etl-and-serverless-on-aws.md): the AWS zero-ETL integrations and the serverless services, with their roles. Read when: you need which services avoid ETL pipelines, or the serverless option for a workload.
- [security-and-monitoring-on-aws.md](security-and-monitoring-on-aws.md): the five security areas, best practices and monitoring aspects mapped to AWS services, with an example secured and monitored pipeline. Read when: you need which AWS services cover a security or monitoring area.

**Choose between services**

- [choosing-ingestion-services.md](choosing-ingestion-services.md): pick-rules and comparisons for ingestion: DMS, Firehose, MSK, Kinesis, DataSync, Transfer Family, Snow, IoT Core, and loading Redshift (streaming ingestion, auto copy, zero-ETL vs DMS vs Glue). Read when: a question asks how to get data into AWS.
- [choosing-storage-and-processing-services.md](choosing-storage-and-processing-services.md): S3 vs Redshift, RDS vs Redshift, RDS isn't a lake, DynamoDB vs RDS, S3 vs EBS vs EFS, serverless vs provisioned options, and Glue vs EMR vs Flink. Read when: a question asks where data should live or what should transform it.
- [choosing-delivery-services.md](choosing-delivery-services.md): pick-rules for Athena, Redshift, EMR, OpenSearch, QuickSight and SageMaker, plus Athena vs Redshift vs Spectrum. Read when: a question asks how consumers should query or see data.
- [choosing-orchestration-services.md](choosing-orchestration-services.md): pick-rules and comparisons for Step Functions, MWAA, Glue workflows, Lambda, EventBridge, SNS, SQS and API Gateway. Read when: a question asks how to coordinate, trigger or decouple pipeline steps.
- [choosing-security-and-monitoring-services.md](choosing-security-and-monitoring-services.md): which service answers which security or monitoring question, and comparisons across IAM, Lake Formation, KMS, ACM, Config, CloudTrail, Macie, GuardDuty, WAF, Shield, CloudWatch, X-Ray and dashboards. Read when: a question asks which security, compliance or monitoring service fits.

**Revise**

- [exam-traps.md](exam-traps.md): the keyword-to-service table for all stages, older service names in exam material, discontinued services, and course errata. Read when: revising for the exam, or a service name in a question doesn't match the current one.

## Gaps

- No exam facts yet: domains and weights, format, passing score, study progress.
