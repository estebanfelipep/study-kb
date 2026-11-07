# AI orchestration on AWS

This file covers how AWS services run model chains (the workflow patterns of agent orchestration), example pipelines that chain models, and a real-world predictive maintenance solution built around Bedrock.

## Sources

- [AWS Generative AI Developer Advanced Learning Plan (includes Labs)](https://skillbuilder.aws/learning-plan/BGTH16YCTU/aws-generative-ai-developer-advanced-learning-plan-includes-labs/ZDN46CX881): AWS Skill Builder learning plan, the model chaining and orchestration lesson.

## Services that orchestrate model chains

Complex generative AI applications connect several models or services into multi-step workflows. Three AWS services coordinate them:

| Service | Role in an AI workflow | Pick it when |
| ------- | ---------------------- | ------------ |
| [Step Functions](../aws-services/aws-application-coordination/step-functions.md) | Visual workflow that runs the chain's steps, with built-in error handling, retries, state management and monitoring | Complex multi-step AI workflows that coordinate several services |
| [Lambda](../aws-services/aws-compute/lambda.md) | Event-driven functions that connect AI services, process data between model calls and run custom logic | Intermittent workloads, where paying only while code runs is cheapest |
| [EventBridge](../aws-services/aws-application-coordination/eventbridge.md) | Event-driven architecture that triggers model chains when events arrive | Loosely coupled components and asynchronous processing |

```
 event ─► EventBridge ─► Step Functions state machine
                           │
                           ├─► step 1: model call (Lambda / service)
                           ├─► Lambda: reshape data between calls
                           ├─► step 2: model call
                           └─► store result
```

## Implementation examples

Each example is a model chain where every step uses the model best suited to it.

| Example | Steps | Workflow pattern |
| ------- | ----- | ---------------- |
| Document processing pipeline | OCR text extraction → classification → summarization → storage | Prompt chaining |
| Multi-modal content generation | Text prompt → image generation → image analysis → caption generation, with a different model per modality | Prompt chaining |
| Intelligent customer service | Intent classification → knowledge retrieval → response generation → sentiment analysis, routing adaptively by complexity | Routing |

```
 Document processing pipeline

 PDF ─► [OCR] ─► text ─► [Classify] ─► [Summarize] ─► [Store]
```

## Real-world example: manufacturing predictive maintenance

A manufacturer wants to **predict equipment failures from sensor data** and give technicians a **natural-language troubleshooting assistant**, while **keeping data within company boundaries** for compliance.

```
 DATA SOURCES
  [IoT sensors: pumps, motors]
               │
               ▼
  [AWS IoT Core] ─► [Amazon S3] ─► [AWS Lambda]
                                        │ processes data
 AI ENGINE                              ▼
                                [Amazon Nova Pro]
                                        │ multi-modal analysis
 USER INTERFACE                         ▼
                        ┌──────────────────────────────┐
  Technician ─question─►│ Amazon Bedrock               │
      ▲                 │ (central AI orchestrator)    │
      │                 └───┬──────────▲───────────┬───┘
      │             retrieve│          │context    │ generates
      │                     ▼          │           │
      │                 ┌──────────────┴─────┐     │
      │                 │ Amazon OpenSearch  │     │
      │                 │ RAG knowledge base │     │
      │                 │ (manuals, records, │     │
      │                 │  sensor patterns)  │     │
      │                 └────────────────────┘     ▼
      └──────────────── [AI-generated maintenance guidance]
```

| Layer | Component | Role |
| ----- | --------- | ---- |
| Data sources | [IoT Core](../aws-services/aws-iot/iot-core.md) | Connects the equipment's IoT sensors and routes their readings to S3 |
| Data sources | [S3](../aws-services/aws-general-services/s3.md) | Stores the sensor data |
| Data sources | [Lambda](../aws-services/aws-compute/lambda.md) | Processes the data and orchestrates between services |
| AI engine | [Bedrock](../aws-services/aws-ai/bedrock.md) | The central AI engine: orchestrates the whole AI workflow and answers technicians |
| AI engine | Amazon Nova Pro | Multi-modal analysis of sensor data and equipment images |
| AI engine | Fine-tuned models | Equipment-specific failure pattern recognition |
| AI engine | [OpenSearch Service](../aws-services/aws-databases/opensearch-service.md) | The RAG knowledge base: equipment manuals, historical maintenance records and sensor data patterns |
| User interface | Technician app | Natural-language questions in, AI-generated maintenance guidance out |

**A technician's question, step by step:**

1. The technician asks: *"Why is pump P-101 showing unusual vibration patterns?"*
2. Bedrock retrieves relevant context from the RAG knowledge base in OpenSearch.
3. Bedrock generates a response that combines the sensor analysis with the matching maintenance procedures.
4. The technician gets AI-generated maintenance guidance.

**How the knowledge base finds context.** It combines three retrieval signals:

| Signal | Matches | Example |
| ------ | ------- | ------- |
| Semantic search | Meaning, not exact words | Maintenance procedures relevant to "unusual vibration" |
| Time-series similarity | Sensor readings shaped like past ones | Earlier vibration patterns that preceded a failure |
| Hybrid search | Several relevance signals combined into one ranking | The best mix of procedures, records and patterns |

## Related

- [agent-orchestration.md](../../ai/ai-engineering/agent-orchestration.md): the vendor-neutral patterns these services implement. Model chaining is the workflow side; agentic AI is the agent side.
- [step-functions.md](../aws-services/aws-application-coordination/step-functions.md): Step Functions runs a model chain as a state machine, its Parallel and Choice states covering parallel processing and conditional branching.
- [lambda.md](../aws-services/aws-compute/lambda.md): Lambda runs the custom logic between model calls in a chain.
- [eventbridge.md](../aws-services/aws-application-coordination/eventbridge.md): EventBridge rules start a model chain when a matching event arrives.
- [bedrock.md](../aws-services/aws-ai/bedrock.md): Bedrock serves the foundation models that each step of a chain calls, and in the predictive maintenance example it's the central AI engine that retrieves RAG context and answers technicians.
- [iot-core.md](../aws-services/aws-iot/iot-core.md): IoT Core ingests the equipment sensor readings that feed the predictive maintenance example.
- [opensearch-service.md](../aws-services/aws-databases/opensearch-service.md): OpenSearch stores the RAG knowledge base (manuals, maintenance records, sensor patterns) that Bedrock retrieves context from in the predictive maintenance example.
- [core-concepts.md](../../ai/core-concepts.md): the predictive maintenance example is a RAG system; its semantic and hybrid search are the retrieval methods explained there, and its fine-tuned models are one of the customization approaches.
- [textract.md](../aws-services/aws-ai/textract.md): Textract extracts text from documents, which is the OCR step of the document processing pipeline.
