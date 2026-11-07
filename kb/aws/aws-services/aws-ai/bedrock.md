In a simplified way, what Amazon Bedrock does is to offer a set of features (it offers an abstraction). We should be able to get the same features with more granular control if we went with just the AI SDK, for example.

Even though Amazon Bedrock and related tools offer a nice UI to set up some of these features, one of the trade-offs is versioning. When you create a knowledge base (for RAG), it's not easy to set up versioning, or if you set up an MCP target with Amazon Bedrock Agent Core, you set up the tool description in there. You're basically creating an MCP tool that's outside of your control when building an agent with code.

## Features

- Managed FM: accessible to developers through a single API
	- Amazon Bedrock is a fully managed service that provides access to high-performing foundation models (FMs) from leading AI companies and Amazon through a unified API.
		- AWS
	- Anthropic
	- Meta
	- Google (Gemini)
	- …
- Evaluations with different FM
- It is serverless
	- Amazon Bedrock is fully managed and serverless, so there is no model to deploy and no endpoint to manage. You call the model on demand through the Bedrock Runtime API.
- Supports fine-tuning (through [sagemaker](sagemaker.md))
- RAG
	- Vector databases through Amazon OpenSearch Serverless
    - Amazon has a frontier model (“Amazon Titan Embeddings”) to embed data
	- We can create a knowledge base on Bedrock. The flow is:
	    1. Data source (S3 bucket) →
	    2. Bedrock chunks the documents →
	    3. Embedding model (Titan Embeddings) converts chunks to vectors →
	    4. OpenSearch Serverless stores the vectors
	    
	    Bedrock orchestrates this: it reads from S3, calls the embedding model, and writes to OpenSearch. The OpenSearch Collection is purely storage for the vectors—it doesn't do the embedding transformation itself.
	    
	    Think of it as: Bedrock KB uses OpenSearch as vector storage, not as the embedding engine.
- Prompt management
	- Prompt management saves, versions, and manages prompts in Amazon Bedrock. Reusable prompts with variables are created and tested with different foundation models, such as Amazon Nova 2 Lite, and then saved as versions that applications call by ID for production use.
- Guardrails
	- Guardrails implement safeguards customized to your application requirements and responsible AI policies.
	- You can set up guardrails for inputs and outputs of models.
	- UI in amazon
		- See how you can set up guardrails based on categories. This is a high-level abstraction of setting up guardrails through aws.
		![](images/Screenshot%202026-09-20%20at%2010.30.48%20AM.png)