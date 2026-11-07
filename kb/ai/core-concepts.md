# Core concepts

- Graphic representation of the relationship between some of these concepts
	![](images/Screenshot%202026-11-07%20at%2011.49.28%20AM.png)

## Foundation models
 
 Foundation models are **large deep learning neural networks** trained on massive datasets that have changed how you approach machine learning. Rather than develop AI from scratch, you use foundation models as starting points to develop ML models that power new applications more quickly and cost-effectively.
 
They are specialized, so there are foundation models for translations, image generation, video generation, etc.

A unique feature of foundation models is their **adaptability**. These models can perform a wide range of disparate tasks with high accuracy based on input prompts, including 

- natural language processing
- question answering
- image classification
- code generation
- visual comprehension
- and speech-to-text conversion

Foundation model can then be tuned and adjusted to solve specific needs

### Model types

Foundation models fall into two primary categories based on their design and intended use

-  **general-purpose models** 
	- trained on diverse, broad datasets spanning multiple domains and languages, making them versatile for various applications.
-  **specialized models** 
	- Trained on domain-specific datasets focused on particular industries, tasks, or use cases. Their training data is curated from specialized sources like medical journals, legal documents, or scientific papers. They excel in their target domain by incorporating specialized knowledge and terminology that general models may lack. Examples include BioGPT for biomedical text generation, AlphaFold for protein structure prediction, LEGAL-BERT for legal document analysis, and CodeT5 for software development tasks.

### Integration and deployment approaches 

There are different ways to integrate a foundation model in a system, depending on the needs:

> *In the following list even though AWS service-related services or approaches are mentioned, these may apply to other hyper-scaler vendors such as Google or Microsoft*

- **Amazon Bedrock integration (unified API):**
	- [bedrock](../aws/aws-services/aws-ai/bedrock.md) provides a unified API to access multiple foundation models without managing infrastructure.
	- This might be the easiest way to integrate a foundation model using AWS 
- **AWS AI Factories integration (on-premises):**
	- "On-premises" describes where the hardware sits, not who owns and runs it. AWS ships, installs and operates its own AI infrastructure inside the customer's data center.
	- Suitable for cases when the company data has 
		- residency requirements
		- regulated industries with strict compliance needs
		- scenarios requiring low-latency inference close to data sources
		- and enterprises wanting cloud-like AI capabilities within their own security perimeter.
	- Split of responsibilities:
		- **The customer provides** the building, floor space, power, cooling, physical security and the network uplink. Their data, models and apps stay inside their own security perimeter.
		- **AWS provides and operates** the hardware (GPUs, Trainium chips, servers, storage, networking). It patches, monitors and replaces failed parts, and runs AI services such as Bedrock and SageMaker AI on top.
	- The site stays connected to an AWS Region, but that link mostly carries management traffic (health checks, software updates, telemetry, billing). Inference and training run locally, next to the data.
	- How the pieces connect:
		```
		  CUSTOMER DATA CENTER                      AWS REGION
		 +-----------------------------------+     +-------------------+
		 |  AWS-owned AI racks               |     |                   |
		 |  +-----------------------------+  |     |  control plane:   |
		 |  | Bedrock / SageMaker AI      |  |<--->|  monitoring,      |
		 |  | GPUs / Trainium, storage    |  | mgmt|  updates, health, |
		 |  +-----------------------------+  | link|  billing          |
		 |        ^                          |     |                   |
		 |        | local, low-latency       |     +-------------------+
		 |  customer apps + data             |
		 |  (data stays here)                |
		 +-----------------------------------+
		```
	- This is the reverse of a typical hybrid setup. There, on-premises servers send data or workloads up to the cloud. Here, the cloud's hardware comes down to the customer.
	- That's why it fits data residency, regulated industries and low-latency inference: the data never leaves the building, and the customer still doesn't build or run their own GPU cluster.
- **Amazon SageMaker AI integration (self-host):**
	- This might be suitable for cases where we need to fine-tune foundation models 
	- This offers a lower level of abstraction when it comes to managing the integration, and the deployment of a FM
- **Direct provider API integration (direct API):**
	- Consuming the API from model providers directly, such as Claude, OpenAI, or Gemini, offers the main benefit of potentially early access to new features
	- Depending on how these are consumed, the team may also fall into a bottleneck situation. Say, for example, if they only use Gemini with the specific Gemini API, this is where tools like the Vercel AI SDK come in very handy 

### Model customization approaches 

- **Fine-tuning** adjusts model parameters using your specific training data to improve performance for domain-specific tasks. Requires training and validation datasets, and typically needs Provisioned Throughput for deployment.
- **Prompt / Context engineering** optimizes input prompts to achieve better outputs without modifying the model itself. This cost-effective approach uses iterative refinement of prompts, examples, and instructions.
- **Continued Pre-Training (CPT)** extends foundation models by training on domain-specific data before fine-tuning, helping models grasp specialized terminology and concepts. 
	- Requires either the model's weights (open-weight models such as Llama, Mistral or Qwen, trained on SageMaker or your own GPUs) or a provider that runs it for you (Nova on SageMaker or Bedrock). Closed models such as Claude can't be continually pre-trained; customize them with prompt/context engineering or RAG instead.
	- Trains on **unlabeled** domain text (manuals, tickets, code) with the same objective as the original pre-training: predict the next token. Fine-tuning is the step that needs labeled pairs.
	- Process: 
		- collect text → 
		- clean and dedupe → 
		- mix in some general text → 
		- train at a small learning rate → 
		- evaluate on domain and general tasks → 
		- fine-tune to restore instruction following → 
		- deploy.
	- Main risk is **catastrophic forgetting**: the model loses general skills. Mixing in general text and evaluating on general tasks guard against it.
- **Nova Forge (aws specific)** enables building custom frontier models with Amazon's Nova technology, providing infrastructure and tools **to create large language models from scratch**. Supporting models up to 1 trillion parameters with flexible deployment, it serves organizations needing highly specialized AI capabilities beyond adapting existing models.

#### CPT vs Nova Forge

CPT is a technique, and Nova Forge is an AWS service. The difference is where each one enters the model's training:

```
  AMAZON'S TRAINING OF A NOVA MODEL
  [pre-training] -> [mid-training] -> [post-training] -> finished model
       ^                 ^                  ^                 |
       |                 |                  |                 v
       +---- Nova Forge: start from any checkpoint     CPT: start here,
             and mix your data with Amazon's data      add your domain
                                                       text on top
```

| | Continued Pre-Training (CPT) | Nova Forge |
|---|---|---|
| What it is | A vendor-neutral technique | An AWS service built on Nova |
| Needs the model's weights | Yes: open-weight models, or a provider running it for you | No: AWS holds the Nova checkpoints |
| Starting point | A finished model | Early, middle or late Nova checkpoints |
| Training data | Only your unlabeled domain text | Your data mixed with Amazon's curated data |
| Main risk | Catastrophic forgetting | Cost and effort |
| Cost and effort | Moderate | High, aimed at large organizations |

Mixing your data in at an earlier stage is why Nova Forge forgets less: the domain becomes part of the model's foundation instead of a layer on top.

## Retrieval-augmented generation (RAG)

**Problem:** Foundation models have knowledge cutoffs and lack access to your specific or proprietary information, leading to outdated responses or hallucinations.

***Solution:*** RAG connects foundation models with external knowledge sources, retrieving relevant information to ground responses in factual sources.

**Components:*** RAG systems rely on five essential components that work together to transform raw information into contextually relevant responses.

- Document processing: Chunks knowledge while maintaining context
- Embedding models: Converts text to mathematical vectors
- Vector storage: Efficiently stores and searches vectors
- Query processing: Matches user questions to relevant content
- Response generation: Combines retrieved context with queries