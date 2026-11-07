# ai — index

This folder covers AI regardless of vendor: generative AI, foundation models, and retrieval-augmented generation. How AWS implements them lives in [aws-ai](../aws/aws-services/aws-ai/aws-ai.md).

Each subfolder is one way of working with AI: `ai-engineering/` covers building AI-powered systems, and a sibling such as AI orchestration, on leveraging existing AI harnesses instead, gets its own subfolder when its first note arrives. Concepts the subfolders share, such as foundation models and RAG, sit at the top of this folder.

## How to read this folder

- **Order:** start with what generative AI is and what the role involves, then the core concepts.
- **After:** [aws-ai](../aws/aws-services/aws-ai/aws-ai.md), for the AWS services the core concepts name.

## Files (in reading order)

- [ai-engineering/](ai-engineering/ai-engineering.md): what generative AI is, and the AI engineer role and its responsibilities. Read when: you need what generative AI is or what an AI engineer does.
- [core-concepts.md](core-concepts.md): foundation models and their types, ways to integrate and deploy them, customization approaches (fine-tuning, prompt and context engineering, Continued Pre-Training, Nova Forge), and RAG: the pipeline, chunking, BM25 and semantic search, reciprocal rank fusion and reranking. Read when: you need how foundation models are integrated or adapted, or how a RAG system retrieves context.
