# ai — index

This folder covers AI regardless of vendor: generative AI, foundation models, and retrieval-augmented generation. How AWS implements them lives in [aws-ai](../aws/aws-services/aws-ai/aws-ai.md).

Each subfolder is one way of working with AI: `ai-engineering/` covers building AI-powered systems, and a sibling such as AI orchestration, on leveraging existing AI harnesses instead, gets its own subfolder when its first note arrives. Concepts the subfolders share, such as foundation models and RAG, sit at the top of this folder.

## How to read this folder

- **Order:** start with what generative AI is and what the role involves, then the core concepts.
- **After:** [aws-ai](../aws/aws-services/aws-ai/aws-ai.md), for the AWS services the core concepts name, and [aws-ai-engineering](../aws/aws-ai-engineering/aws-ai-engineering.md), for how AWS services orchestrate model chains.

## Files (in reading order)

- [ai-engineering/](ai-engineering/ai-engineering.md): what generative AI is, the AI engineer role and its responsibilities, the Claude model tiers and API call patterns, prompt engineering, context engineering, agent orchestration (workflows vs agents and the workflow patterns), and building a generative AI PoC, and stakeholder discovery. Read when: you need what generative AI is, what an AI engineer does, which Claude model or API pattern to use, how to write prompts, how to manage an agent's context, how LLM calls and tools combine into workflows and agents, how to scope and evaluate a PoC, how to run a stakeholder discovery call, or how to design and judge an LLM feature.
- [core-concepts.md](core-concepts.md): foundation models and their types, ways to integrate and deploy them, customization approaches (fine-tuning, prompt and context engineering, Continued Pre-Training, Nova Forge), and RAG: the pipeline, chunking, BM25 and semantic search, reciprocal rank fusion and reranking. Read when: you need how foundation models are integrated or adapted, or how a RAG system retrieves context.
