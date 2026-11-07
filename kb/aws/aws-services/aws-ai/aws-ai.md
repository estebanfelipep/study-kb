# aws-ai — index

Machine learning and AI services.

## How to read this folder

- **Before:** The deliver stage, in [modern-data-architecture.md](../../../data-engineering/modern-data-architecture.md).
- **After:** [choosing-delivery-services.md](../../aws-data-engineering/choosing-delivery-services.md).

## Files

- [sagemaker.md](sagemaker.md): Amazon SageMaker: SageMaker AI (build, train and deploy ML models), the broader platform, and SageMaker Lakehouse. Read when: you need ML at the delivery stage, or the lake house service.
- [bedrock.md](bedrock.md): Amazon Bedrock, the serverless API service for consuming and customizing existing foundation models: model families and Nova 2 tiers, integration options (Inference API, Knowledge Bases, Agents, Model Evaluation), evaluation types, RAG knowledge bases, prompt management, guardrails and encryption. Read when: you need generative AI with foundation models on AWS, which Bedrock model or integration fits, or how Bedrock secures data.
- [ai-factories.md](ai-factories.md): AWS AI Factories, AWS-owned and AWS-operated AI infrastructure, running services such as Bedrock and SageMaker AI, inside the customer's data center. Read when: you need foundation models on premises, for data residency, compliance or low-latency inference.
- [nova-forge.md](nova-forge.md): Amazon Nova Forge, building custom frontier models from Nova checkpoints mixed with your data. Read when: you need a custom model beyond adapting an existing one.
- [textract.md](textract.md): Amazon Textract, text, form and table extraction from documents such as PDFs in S3. Read when: you need text out of documents.
- [polly.md](polly.md): Amazon Polly, text to lifelike speech, saved as an audio file in S3. Read when: you need to turn text into speech.
