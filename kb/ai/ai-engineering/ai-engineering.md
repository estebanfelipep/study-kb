- Resources
	- [AWS Generative AI Developer Advanced Learning Plan (includes Labs)](https://skillbuilder.aws/learning-plan/BGTH16YCTU/aws-generative-ai-developer-advanced-learning-plan-includes-labs/ZDN46CX881)
## Generative AI

Generative AI produces original content including text, images, audio, video, and code based on patterns learned from training data. Foundation models serve as the underlying technology, providing general intelligence that you can adapt for specific use cases through techniques like fine-tuning, prompt engineering, and retrieval-augmented generation.

## The role: AI engineer/generative AI engineer 

### Responsibilities

- **Solution architecture and design**
	- As a generative AI developer, you design comprehensive solutions that integrate foundation models with existing systems and data sources. You evaluate different architectural patterns, select appropriate models, and plan deployment strategies that meet business requirements and technical constraints.

- **Integration and implementation**
	- You implement generative AI solutions by using AWS services like Amazon Bedrock, Amazon SageMaker AI, and supporting infrastructure services. This includes configuring APIs, setting up data pipelines, and implementing secure, scalable deployments.

- **Performance optimization**
	- You monitor and optimize generative AI applications for performance, cost, and accuracy. This involves tuning model parameters, implementing caching strategies, and optimizing resource utilization across the solution stack.

- **Security and compliance**
	- You verify that generative AI solutions meet security requirements and regulatory compliance standards. This includes implementing proper access controls, data encryption, and audit logging while maintaining data privacy and governance.

## Files (in reading order)

- [claude-api-foundations.md](claude-api-foundations.md): from Anthropic's Claude course: the four model tiers, model choice vs reasoning mode vs prompting mode, tokens, the context window and sampling, and the sync, streaming, async and Message Batches call patterns. Read when: you need which Claude model or reasoning mode to pick, or how to call the API for a given workload.
- [prompt-and-context-engineering.md](prompt-and-context-engineering.md): how prompt engineering (writing the prompt) differs from context engineering (assembling the context on each turn). Prompt structure and anatomy, system prompts, role prompting, zero-, one- and few-shot, chain-of-thought and prompt tips; the limits of long contexts, compaction strategies and triggers, and evaluating a memory-enabled agent. Read when: you need how to write a prompt that gets better output without changing the model, or how to keep an agent's conversation within the context window.
- [structured-outputs.md](structured-outputs.md): the trade-offs of constraining a Claude response to a schema: first-request latency, extra input tokens, refusal and truncation still returning non-matching output, and no combining with prefilling. Read when: you need what structured outputs cost or when they still fail to parse.
- [extended-thinking.md](extended-thinking.md): extended thinking in the Claude API: the thinking block, what it costs, and the carry-back rule that thinking blocks must return to the API unchanged when tools are used. Read when: you need whether to turn thinking on, or why a tool-using request with thinking was rejected.
- [agent-orchestration.md](agent-orchestration.md): agentic systems: workflows vs agents, the agent loop, and the five workflow patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer), with use cases. Read when: you need whether a task calls for a workflow or an agent, or which workflow pattern fits.
- [genai-poc.md](genai-poc.md): building a generative AI proof of concept: scoping, model selection and evaluation, performance testing, and value calculation. Read when: you need how to scope, evaluate or justify a generative AI PoC.
- [stakeholder-discovery.md](stakeholder-discovery.md): from Anthropic's Claude Certified Architect course: running a discovery call as structured elicitation (listen, translate, write down), turning stated preferences into constraints, the four requirement questions, and the translation table. Read when: you need how to turn a stakeholder's business-language request into requirements, assumptions and design constraints.
- [design-document.md](design-document.md): from Anthropic's Claude course: the design document (success criteria, failure handling, cost and latency budget, trust boundary). Read when: you need what to write down before building an LLM feature.
- [evals/](evals/evals.md): evaluating generative and agentic systems: what an eval is, traces and sessions, the hill-climb lifecycle from organizational KPIs, the evaluation plan, rubrics, the LLM judge (autorater) and synthetic test data. Read when: you need how to measure, grade or monitor an AI system, or how to turn a business KPI into metrics.
