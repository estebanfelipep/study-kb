# ai — index

This folder covers AI regardless of vendor: generative AI, foundation models, and retrieval-augmented generation. How AWS implements them lives in [aws-ai](../aws/aws-services/aws-ai/aws-ai.md).

Each subfolder is one way of working with AI: `ai-engineering/` covers building AI-powered systems, and a sibling such as AI orchestration, on leveraging existing AI harnesses instead, gets its own subfolder when its first note arrives. Concepts the subfolders share, such as foundation models and RAG, sit at the top of this folder.

## How to read this folder

- **Order:** start with the core concepts (what generative AI is, what the role involves, then foundation models and RAG), then `ai-engineering/` for building with them.
- **After:** [aws-ai](../aws/aws-services/aws-ai/aws-ai.md), for the AWS services the core concepts name, and [aws-ai-engineering](../aws/aws-ai-engineering/aws-ai-engineering.md), for how AWS services orchestrate model chains.

## Files (in reading order)

- [core-concepts.md](core-concepts.md): what generative AI is, the AI engineer role and its responsibilities, foundation models and their types, ways to integrate and deploy them, customization approaches (fine-tuning, prompt and context engineering, Continued Pre-Training, Nova Forge), and RAG: classical RAG vs agentic search (with progressive disclosure), the pipeline, chunking, BM25 and semantic search, reciprocal rank fusion and reranking. Read when: you need what generative AI is, what an AI engineer does, how foundation models are integrated or adapted, how a RAG system retrieves context, or when an agent should search live instead of using an index.
- [ai-engineering/](ai-engineering/ai-engineering.md): building AI-powered systems with Claude: model tiers and API call patterns, extended thinking and structured outputs, prompt and context engineering (compaction, the four context-budget strategies, prompt caching, token counting), tool use and MCP (servers, transports, scope, authentication), agent orchestration, building a generative AI PoC, stakeholder discovery, the design document, and, in its evals/ subfolder, evaluating a system from KPIs through rubrics, the LLM judge and synthetic data. Read when: you need which Claude model or API pattern to use, how to write prompts or manage an agent's context, how to write tool descriptions, connect an MCP server and choose its transport, scope and authentication, how LLM calls and tools combine into workflows and agents, how to scope, design and evaluate an LLM feature or PoC, or how to hill climb a generative system against organizational KPIs.
