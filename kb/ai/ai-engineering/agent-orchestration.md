# Agent orchestration

This file covers how LLM calls and tools are combined into agentic systems: workflows vs agents, the agent loop, and the five workflow patterns, with when to use each.

## Sources

- [Building effective agents (Anthropic)](https://www.anthropic.com/engineering/building-effective-agents): Anthropic engineering article on the workflow types and agents, with examples and use cases.
- [What is an agent? (AI Hero)](https://www.aihero.dev/what-is-an-agent): AI Hero article on what makes a system an agent.
- [Agents vs workflows (YouTube)](https://www.youtube.com/watch?v=F8NKVhkZZWI): video on agents and workflows.

## Agentic systems: workflows vs agents

An **agentic system** is any system that combines LLMs and tools. There are two architectures, and the difference between them is the **degree of autonomy**:

- **Workflows** orchestrate LLMs and tools through **predefined code paths**. The code is in control, and the LLM runs on rails that a human designed in advance.
- **Agents** let the LLM **dynamically direct its own process and tool usage**. The LLM is in control of how it accomplishes the task.

| Attribute           | Workflow                                     | Agent                                            |
| ------------------- | -------------------------------------------- | ------------------------------------------------ |
| How many LLM calls  | Many                                         | Many                                             |
| Who's in control    | The code describing the workflow             | The LLM                                          |
| Who decides to stop | The predetermined steps                      | The LLM                                          |
| Path to the answer  | Predetermined steps, written in code         | Chosen at run time, tool call by tool call       |
| Autonomy            | Low: runs on predefined rails                | High: plans, picks tools and adapts              |
| Human oversight     | The human designs the path in advance        | Less: the agent acts proactively toward a goal   |
| Good for            | When the path to the solution is known upfront | When the path to the solution is unclear       |
| Example             | Voice-to-text writing assistant (below)      | Code assistant                                   |
| AWS course name     | Model chaining                               | Agentic AI                                       |

The number of LLM calls doesn't tell them apart: both make many. What differs is who decides the next step and when to stop.

## Agent

An agent is an **LLM using tools in a loop, based on feedback from its environment**. Each LLM call takes an action on the environment (a tool call) and gets feedback (the result). From that feedback it decides on its own whether to act again or to stop. A human can talk to the agent along the way, to give the task or answer its questions. It plans, researches, reasons and acts like a self-directing team working toward a goal, and it adapts as conditions and requirements change.

```
                              action (tool call)
 ┌───────┐        ┌──────────┐ ──────────────► ┌─────────────┐
 │ Human │◄╌╌╌╌╌╌►│ LLM call │                 │ Environment │
 └───────┘        └────┬─────┘ ◄────────────── │ (search,    │
                       ╎       feedback        │  code exec) │
                       ╎ LLM decides it's done └─────────────┘
                       ▼
                    [ Stop ]
```

- Because the agent picks tools from their descriptions, **toolsets and their documentation must be designed clearly and thoughtfully**.
- **Use case: code assistant.** The path to the solution is unclear, and it may take several iterations to reach the answer.

## Workflow

A workflow is a **list of predetermined steps, written in code**. The LLM isn't in control; the code is. Each step is an LLM call or a tool, and the code decides what runs next.

```
 ┌─ code (predetermined steps) ──────────────────────┐
 │                                                   │
 │  [LLM call 1] ─► [LLM call 2] ─► [LLM call 3]     │
 │                                       │           │
 │                    last step reached ─┴─► stop    │
 └───────────────────────────────────────────────────┘
```

**Use case: writing text by voice**, a prompt chain of three assistants:

```
 voice ─► [1 Voice-to-text] ─► raw text ─► [2 Clean-up] ─► phrases
                                           (drops slang, "mmm")
 phrases ─► [3 Writer: improves the text] ─► final text
```

### Workflow patterns

| Pattern              | What it does                                                                          | AWS course name       |
| -------------------- | ------------------------------------------------------------------------------------- | --------------------- |
| Prompt chaining      | Splits a task into a sequence of steps; each LLM call processes the previous output   | Sequential chaining   |
| Routing              | Classifies the input and sends it to a specialized follow-up task                     | Conditional branching |
| Parallelization      | Several LLM calls work at once; code aggregates their outputs                         | Parallel processing   |
| Orchestrator-workers | A central LLM breaks the task down, delegates to worker LLMs and synthesizes results  | —                     |
| Evaluator-optimizer  | One LLM generates, another evaluates and gives feedback, in a loop                    | Feedback loops        |

**Prompt chaining**: each LLM call takes the previous call's output as its input, like an assembly line (prompt A → prompt B → output). The voice-writing example above is a prompt chain.

```
 input ─► [LLM 1] ─► [LLM 2] ─► [LLM 3] ─► output
```

**Routing**: a classifier step picks which specialized task handles the input. It separates concerns, so each follow-up prompt can be specialized.

```
                  ┌─► [LLM: refunds] ───┐
 input ─► [Router]┼─► [LLM: tech help] ─┼─► output
                  └─► [LLM: general] ───┘
```

**Parallelization**: LLMs work on the task at the same time, and code aggregates their outputs. It has two variants:

- **Sectioning:** splits the task into independent subtasks that run in parallel.
- **Voting:** runs the same task several times to get diverse outputs.

```
          ┌─► [LLM] ─┐
 input ───┼─► [LLM] ─┼─► [Aggregator: code] ─► output
          └─► [LLM] ─┘
```

**Orchestrator-workers**: a central LLM decides at run time how to split the task, delegates the pieces to worker LLMs, and synthesizes their results. Unlike sectioning, the subtasks aren't fixed in advance; the orchestrator picks them for each input.

```
                        ┌─► [Worker LLM] ─┐
 input ─► [Orchestrator]┼─► [Worker LLM] ─┼─► [Synthesizer] ─► output
           (LLM)        └─► [Worker LLM] ─┘
```

**Evaluator-optimizer**: one LLM generates a response, a second LLM evaluates it and gives feedback, and the loop repeats until the evaluator accepts it. It looks like an agent, but an agent is one LLM calling tools and deciding whether it needs more; here two LLMs work together inside a loop the code defines.

```
 input ─► [Generator LLM] ─response─► [Evaluator LLM] ─ok─► output
                ▲                            │
                └──── feedback (rejected) ───┘
```

## Related

- [core-concepts.md](../core-concepts.md): the LLMs these systems orchestrate are foundation models, and RAG's query rewriter is one step such a system can run before retrieval.
- [ai-orchestration-on-aws.md](../../aws/aws-ai-engineering/ai-orchestration-on-aws.md): how AWS implements these patterns, with Step Functions, Lambda and EventBridge running model chains, and example pipelines.
- [genai-poc.md](genai-poc.md): model-based evaluation in a PoC is the evaluator-optimizer idea applied to choosing a model: one LLM judges another's outputs.
- [stakeholder-discovery.md](stakeholder-discovery.md): discovery decides which work stays in deterministic code (such as routing by a business rule) and which the model does, the same line this file draws between workflows and agents.
- [design-document-and-llm-judge.md](design-document-and-llm-judge.md): an LLM judge is the evaluator-optimizer's evaluator used to grade output, with advice on calibrating its scores.
