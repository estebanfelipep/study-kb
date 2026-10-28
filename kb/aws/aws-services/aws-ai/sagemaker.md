# Amazon SageMaker

This file covers Amazon SageMaker: the ML service (SageMaker AI), the broader SageMaker platform, and SageMaker Lakehouse.

## What it is

At the delivery stage, the course lists **machine learning** for building, training and deploying models for **predictive analytics, computer vision, NLP, recommendation systems** and more. The course doesn't name the service. On AWS that's **Amazon SageMaker**. Its typical users are data scientists.

## Characteristics

- **SageMaker AI** is the ML service: build, train and deploy models.
- **SageMaker** is also the name of AWS's broader, unified platform for data, analytics and AI.
- **SageMaker Lakehouse** unifies S3 data lakes and Redshift warehouses under one catalog and one set of permissions. That's the lake house idea.
- Data scientists' models often end up as product features, for example recommendations.

## Example

Watch or purchase history goes through a pipeline into a model. The model's output drives the "Recommended for you" row users see.

## Related

- [s3.md](../aws-general-services/s3.md): SageMaker Lakehouse unifies S3 data lakes with Redshift warehouses under one catalog and one set of permissions.
- [redshift.md](../aws-analytics/redshift.md): Redshift warehouses are the other half that SageMaker Lakehouse unifies with S3.
- [emr.md](../aws-analytics/emr.md): data scientists use both: EMR for big data processing and feature engineering, SageMaker to build, train and deploy models.
- [choosing-delivery-services.md](../../aws-data-engineering/choosing-delivery-services.md): SageMaker is the delivery pick when a question says "train a model", "predictions" or "ML".
- [aws-data-pipeline.md](../../aws-data-engineering/aws-data-pipeline/aws-data-pipeline.md): SageMaker is the stage 5 (deliver) service for machine learning, and SageMaker Lakehouse is one of the services that build a lake on S3.
- [data-lakes-and-warehouses.md](../../../data-engineering/data-lakes-and-warehouses.md): SageMaker Lakehouse is an AWS implementation of the lake house concept described here.
- [data-personas.md](../../../data-engineering/data-personas.md): SageMaker serves the data scientist persona, whose interests include ML pipelines.
- [data-engineer-role.md](../../../data-engineering/data-engineer-role.md): SageMaker models are an example of operational use of data: a recommendation model's output drives what users see in the product.
- [exam-traps.md](../../aws-data-engineering/exam-traps.md): exam material may say Amazon SageMaker for the ML service, which is now SageMaker AI; "SageMaker" alone now means the broader platform.
