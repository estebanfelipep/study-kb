# aws-ai-engineering — index

This folder covers the AWS AI engineering track: how AWS services combine to build generative AI systems. It links to the service files rather than repeating them.

Read [aws-ai](../aws-services/aws-ai/aws-ai.md) instead for how an individual AI service works. Read [ai](../../ai/ai.md) for concepts that hold regardless of vendor.

## How to read this folder

- **Before:** [agent-orchestration.md](../../ai/ai-engineering/agent-orchestration.md) and [genai-poc.md](../../ai/ai-engineering/genai-poc.md), the patterns and PoC method that AWS implements here.
- **Order:** how services orchestrate model chains first, then how to run a PoC on Bedrock.

## Files (in reading order)

- [ai-orchestration-on-aws.md](ai-orchestration-on-aws.md): the AWS services that run model chains (Step Functions, Lambda, EventBridge) example pipelines that chain models (document processing, multi-modal content generation, customer service), and a real-world predictive maintenance solution (IoT Core, S3, Lambda, Nova Pro, Bedrock, OpenSearch RAG). Read when: you need which AWS service coordinates a multi-step AI workflow, an example model chain on AWS, or how Bedrock, RAG and IoT data combine in one solution.
- [bedrock-poc.md](bedrock-poc.md): building a PoC on Bedrock: the integration options to start from, security from day one (IAM, encryption, CloudTrail, CloudWatch), and a healthcare medical-condition extraction example. Read when: you need how to run a generative AI PoC on AWS or a worked Bedrock PoC.
