# Agent orchestration

This file covers how LLM calls and tools are combined into agentic systems: workflows vs agents and how to choose, the agent loop, the five workflow patterns, the three paths for wiring an agent (Messages API, Agent SDK, Managed Agents), human-in-the-loop checkpoints, agent memory scopes, and Skills for carrying instructions across tasks.

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

### Choosing between them

Make this decision **before you write the first line**. The two columns are rules of thumb, read row by row:

| Choose a workflow when…                                   | Choose an agent when…                                                                                     |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| You can enumerate the exact steps in code.                | You can specify the goal and the tools but not the exact path.                                            |
| Error cost is real and step-level guardrails matter.      | The path through the work can't be enumerated in advance.                                                 |
| Observability with standard tooling is required.          | Non-determinism is acceptable and the agent's possible actions are constrained by its registered toolset. |
| The inputs are well-constrained to a known set.           | User inputs vary unpredictably in content and structure.                                                  |
| Every execution of the task follows the same sequence.    | The task requires creative sequencing of the available tools.                                             |

Choosing wrong in either direction only surfaces in production:

- **An agent where a workflow would do** adds context cost and behavior that lives in transcripts.
- **A workflow where an agent is needed** breaks the first time an input falls outside the path.

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

## Wiring paths: who runs the loop

Once you've chosen an agent, there are three ways to wire it, on a spectrum of **how much infrastructure you own**:

| Attribute            | 1. Messages API                                       | 2. Agent SDK                                                        | 3. Claude Managed Agents (public beta)                                  |
| -------------------- | ----------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Who runs the loop    | Your code, every iteration                            | The SDK, inside your own process                                    | Anthropic runs the loop and the sandbox                                 |
| How it runs          | You send the request, read the tool-use blocks, execute the tools and append the results | The SDK iterates and manages context; your code still executes the tools the agent calls | Your app sends user events and streams results back over server-sent events |
| What you own         | The full loop, tool execution, context management, retries and exit conditions | Tool execution and the surrounding application; the SDK provides loop structure, context management and tool registration | The application layer and the agent definition (model, system prompt, tools, MCP servers, skills), defined once and referenced by ID across sessions |
| Choose it when       | You need control over each step, have constraints a library can't accommodate, or are learning how the loop works before adding abstraction | You want the loop, context handling and tool scaffolding that power Claude Code, running in your own environment in Python or TypeScript | You need long-running execution (minutes or hours), a managed sandbox, or no loop, sandbox or tool-execution layer to build |
| Check before committing | The maintenance cost is yours: everything the SDK gives free (context management, parallel tool handling) becomes code you write and test | `settingSources` controls whether filesystem features such as CLAUDE.md and skills load: always set it explicitly | Sessions are stored server-side, so they aren't currently eligible for Zero Data Retention or a HIPAA BAA |

- **Agent SDK `settingSources`:** don't rely on the default. Set it to the sources you intend: `["user", "project", "local"]` matches the Claude Code CLI, and `[]` runs fully isolated with only what you pass programmatically. Confirm the current default against the Agent SDK reference at build time.
- **Managed Agents is a beta:** every endpoint needs the `managed-agents-2026-04-01` beta header, and behavior may change between releases, so build with a migration plan. It is also available on Claude Platform on AWS with some feature differences; verify capability parity for your deployment surface first.
- **A hard stop:** if the workload carries PHI or falls under a ZDR requirement, Managed Agents is ruled out however well it fits operationally, because its sessions are stateful and stored server-side.

## Human-in-the-loop checkpoints

If a tool can take an **irreversible action in production**, it needs a checkpoint before it runs. Register that constraint during design, when you scope the tool surface, before the loop is wired and not after the first write reaches a customer environment.

| Insertion point                  | What triggers the check                                                          | Risk it addresses                                                                      |
| -------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Before a destructive tool call   | The agent is about to execute a write, delete or send                            | **High:** irreversible actions where a wrong call can't be undone                      |
| After a planning step            | The agent has generated a plan and is about to start executing it                | **Medium:** a wrong plan that produces the wrong outcome even if every step executes   |
| On unexpected output             | A tool result has an error flag, is empty, or is outside expected bounds         | **Variable:** failure modes that retry logic alone won't resolve                       |

## Agent memory

**Memory scope** decides what state survives once the loop ends. Choose it in the **design phase**: it's cheap then and expensive in a production refactor. Moving from in-context to external storage under production pressure takes about an hour, against about twenty minutes to make the same choice deliberately at design time.

Scope follows the shape of the session, not what is easiest to implement. In-context memory is the simplest to write, which is why it fails earliest: production sessions turn out to be shorter and more numerous than the long continuous sessions used in development.

| Scope                         | What persists                                                         | Cost                                                                                  | Use when                                                                                       | What you lose                                                          |
| ----------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| In-context memory             | State lives in the active conversation and survives turns in a session | No retrieval overhead; token cost grows with the conversation                         | Short sessions where all the state fits in the context window and nothing carries across restarts | Everything when the session ends: a clear command or new session wipes it |
| External storage              | State is written to a database and read back at session start or on demand | Retrieval latency on every call, plus the engineering work of read and write logic | State that must survive across sessions, move between users or be shared by several agent instances | Nothing on persistence; the cost is latency and implementation complexity |
| Summarized memory             | A condensed version of prior conversation is injected at the start of the next session | Lower token cost per session than replaying full history                     | Long-running conversational agents whose full history would outgrow the context budget         | Any detail the summarizer didn't keep: the agent sees only what the summarization prompt preserved |
| No persistent memory (stateless) | Nothing; each session is independent                               | No overhead, nothing to store or retrieve                                             | Task agents that finish and close out, or pipelines where every session is independent by design | All prior context: a follow-up that depends on an earlier session can't reach it |

- An agent that helps the same user across several days must carry state between sessions.
- An agent that receives one job, completes it and closes it out has no prior session to recall, so it runs stateless.

### Summarized memory vs compaction

Both use an LLM call to condense history, and both are lossy: the agent sees only what the summary kept. Summarized memory is the same technique as [recursive summarization](prompt-and-context-engineering.md#compaction-strategies), used at a different point:

| | Compaction | Summarized memory |
| --- | --- | --- |
| Problem it solves | The window is filling, so the conversation risks the context ceiling, cost and latency | A long-running agent's full history would outgrow the context budget over its life |
| Where the summary is used | In the same conversation, placed in front of the recent turns | Injected at the start of the next session |
| What triggers it | Size (count-based), inactivity (time-based) or a concluded task (event-based) | A session ending or restarting |
| Techniques it covers | Summarizing, but also keeping the last N turns and token-based truncation, which don't summarize | Always a summary |

Time-based compaction (after 15 or 30 minutes of inactivity) comes closest to blurring the line, because the summary is made at a session boundary.

### Carrying instructions across tasks: Skills

Carrying repeatable instructions across tasks is a separate problem from carrying state. The pattern for it is a **Skill**: a markdown file Claude loads on demand by matching its description to the task, rather than instructions injected into every session.

| | Memory scope | Skill |
| --- | --- | --- |
| What it carries | State: what happened in earlier turns or sessions | Instructions: how to do a repeatable task |
| When it enters the context | By the scope chosen (every turn, at session start, on retrieval) | Only when Claude matches its description to the task |

## Related

- [core-concepts.md](../core-concepts.md): the LLMs these systems orchestrate are foundation models, and RAG's query rewriter is one step such a system can run before retrieval.
- [ai-orchestration-on-aws.md](../../aws/aws-ai-engineering/ai-orchestration-on-aws.md): how AWS implements these patterns, with Step Functions, Lambda and EventBridge running model chains, and example pipelines.
- [genai-poc.md](genai-poc.md): model-based evaluation in a PoC is the evaluator-optimizer idea applied to choosing a model: one LLM judges another's outputs.
- [stakeholder-discovery.md](stakeholder-discovery.md): discovery decides which work stays in deterministic code (such as routing by a business rule) and which the model does, the same line this file draws between workflows and agents.
- [design-document.md](design-document.md): an LLM judge is the evaluator-optimizer's evaluator used to grade output, with advice on calibrating its scores.
- [tool-use.md](tool-use.md): an agent picks tools from their descriptions, so overlapping descriptions send it down the wrong path. Tool use covers the exclusion-sentence fix and MCP servers, which supply an agent's toolset ready-made.
- [prompt-and-context-engineering.md](prompt-and-context-engineering.md): a subagent handoff gives a subtask its own context window and returns a short summary, keeping a long agent run within budget. It also covers compaction and how to evaluate a memory-enabled agent; the difference between compaction and summarized memory is in the agent memory section above.
- [claude-api-foundations.md](claude-api-foundations.md): the Messages API wiring path is the raw call patterns covered there (sync, streaming, batch), with your code running the loop around them.
- [hill-climb-lifecycle.md](evals/hill-climb-lifecycle.md): its refund chatbot example pivots from one prompt to subagents and then to a human-in-the-loop design, the workflows-versus-agents decision made under measurement.
- [rubrics-and-llm-judge.md](evals/rubrics-and-llm-judge.md): the evaluator in evaluator-optimizer scores against a rubric, and this file covers how to write one that an autorater applies consistently.
