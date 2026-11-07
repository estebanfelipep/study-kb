# Amazon SageMaker

This file covers Amazon SageMaker: the ML service (SageMaker AI), the broader SageMaker platform, and SageMaker Lakehouse.

## What it is

It is a fully managed cloud service from [Amazon Web Services (AWS)](https://aws.amazon.com/es/sagemaker/) that enables developers and data scientists to build, train, and deploy machine learning and AI models at scale without manually managing underlying infrastructure

The primary difference between Amazon SageMaker and Amazon Bedrock ([bedrock](bedrock.md)) is that SageMaker is an end-to-end platform for building custom machine learning models from scratch, whereas Bedrock is a serverless API service designed for consuming and customizing existing foundation models.

Think of SageMaker as a fully equipped professional workshop where you build, tune, and maintain your own machinery, and Bedrock as a vending machine for world-class, pre-built engines that you can instantly plug into your app.

## Characteristics

- **SageMaker AI** is the ML service: build, train and deploy models.
- **SageMaker** is also the name of AWS's broader, unified platform for data, analytics and AI.
- **SageMaker Lakehouse** unifies S3 data lakes and Redshift warehouses under one catalog and one set of permissions. That's the lake house idea.
- Data scientists' models often end up as product features, for example recommendations.


## Related

- [s3.md](../aws-general-services/s3.md): SageMaker Lakehouse unifies S3 data lakes with Redshift warehouses under one catalog and one set of permissions.
- [redshift.md](../aws-analytics/redshift.md): Redshift warehouses are the other half that SageMaker Lakehouse unifies with S3.
- [emr.md](../aws-analytics/emr.md): data scientists use both: EMR for big data processing and feature engineering, SageMaker to build, train and deploy models.
- [choosing-delivery-services.md](../../aws-data-engineering/choosing-delivery-services.md): SageMaker is the delivery pick when a question says "train a model", "predictions" or "ML".
- [aws-data-pipeline.md](../../aws-data-engineering/aws-data-pipeline/aws-data-pipeline.md): SageMaker is the stage 5 (deliver) service for machine learning, and SageMaker Lakehouse is one of the services that build a lake on S3.
- [data-lakes-and-warehouses.md](../../../data-engineering/data-lakes-and-warehouses.md): SageMaker Lakehouse is an AWS implementation of the lake house concept described here.
- [data-personas.md](../../../data-engineering/data-personas.md): SageMaker serves the data scientist persona, whose interests include ML pipelines.
- [data-engineer-role.md](../../../data-engineering/data-engineer-role.md): SageMaker models are an example of operational use of data: a recommendation model's output drives what users see in the product.
- [transactional-data-lake-on-aws.md](../../aws-data-engineering/transactional-data-lake-on-aws.md): SageMaker consumes the Iceberg dataset of a transactional data lake.
- [ai-factories.md](ai-factories.md): AI Factories runs SageMaker AI on AWS-owned hardware inside the customer's data center.
- [core-concepts.md](../../../ai/core-concepts.md): SageMaker AI is the self-host way to integrate a foundation model, a lower level of abstraction than Bedrock, suited to fine-tuning.
