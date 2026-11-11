# Prompt and context engineering

This file covers the two ways of shaping what an LLM sees: prompt engineering, which writes the instructions, and context engineering, which assembles everything else the model reads on each turn and keeps it within the window and the budget.

## Sources

- [How to improve your LLM-powered app (AI Hero)](https://www.aihero.dev/how-to-improve-your-llm-powered-app): AI Hero article on improving an LLM-powered app.
- [Prompting Guide](https://www.promptingguide.ai/): guide to prompt engineering techniques.
- [Prompt engineering overview (Claude docs)](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview): Anthropic's prompt engineering documentation.
- [System prompts (Claude docs)](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/system-prompts): Anthropic's documentation on role-based prompting with system prompts.
- [Prompt library (Claude docs)](https://docs.claude.com/en/resources/prompt-library/library): library of example prompts.
- [Write clear instructions (OpenAI)](https://platform.openai.com/docs/guides/prompt-engineering#strategy-write-clear-instructions): OpenAI's prompt engineering guide, the strategy on writing clear instructions.
- [Prompting good practices (YouTube)](https://www.youtube.com/watch?v=ysPbXH0LpIE): video on prompting good practices and the structure of a great system prompt.
- [The template (AI Hero)](https://www.aihero.dev/workshops/ai-sdk-v5-crash-course/the-template-hmys8): AI SDK v5 crash course lesson on the prompt template.
- [Exemplars (AI Hero)](https://www.aihero.dev/workshops/ai-sdk-v5-crash-course/exemplars-n4ry4/solution): AI SDK v5 crash course lesson on exemplars.
- [Chain of thought (AI Hero)](https://www.aihero.dev/workshops/ai-sdk-v5-crash-course/chain-of-thought-2y3wd/solution): AI SDK v5 crash course lesson on chain-of-thought.
- [How to build production-grade generative AI applications (freeCodeCamp)](https://www.freecodecamp.org/news/how-to-build-production-grade-generative-ai-applications/#heading-qa-for-llm-applications-test-more-than-you-think): its QA section shows potential fixes for common agent malfunctions.
- [Long context isn't the answer (HumanLayer)](https://www.humanlayer.dev/blog/long-context-isnt-the-answer): blog post on why a longer context window doesn't solve the problem.

## Prompt engineering vs context engineering

Both work on the model's **input** instead of changing the model. They differ in what they shape and when:

| | Prompt engineering | Context engineering |
|---|---|---|
| Shapes | The prompt, particularly the system prompt: its instructions, role, constraints and examples | Everything the model sees on a turn: the prompt plus conversation history, retrieved documents and memories |
| When | Written and refined ahead of time, then reused | Rebuilt on every turn of a conversation |
| Main question | How do I phrase this so the model answers reliably? | What goes into the window this turn, and what gets trimmed? |
| Main concerns | Clarity, structure, examples, the order of directives | The context window limit, cost, latency and quality |
| Techniques | Roles, exemplars, few-shot, chain-of-thought | Retrieval (RAG), compaction, memory |

```
 +------------------------ context window -----------------------+
 |  prompt (system prompt + the ask)     <- prompt engineering   |
 |  conversation history                                         |
 |  retrieved documents                                          |
 |  memories                                                     |
 +---------------------------------------------------------------+
   what goes in, and what is trimmed, on each turn
   = context engineering
```

The prompt is one part of the context, so prompt engineering sits inside context engineering. A prompt can be well written and still fail when the history around it grows too long.

## Prompt engineering

### What it is

Prompt engineering improves a foundation model's response quality, consistency and relevance by changing the **input**, not the model. It needs no fine-tuning or extra training, which makes it the cheapest way to get better outputs and the first lever to pull in a PoC.

Its main focus is how to write effective prompts, particularly **system prompts**. Three principles run through everything below:

- **Add the smallest amount of prompt that produces a reliable result.**
- **Order matters.** Put the most important directives at the beginning and at the end of the prompt.
- **Context decides how tailored the answer is.** The more accurate the context, the more tailored the result.

### Prompt structure

An effective prompt has three parts:

| Part | What it gives the model | Example |
|---|---|---|
| Instructions | What to do, stated clearly | "Extract every medical condition from the note." |
| Context | The background it needs | "The note was written by a clinician after a visit." |
| Output requirements | The exact shape of the answer | "Return JSON: a list of `{condition, category, confidence}`." |

Mnemonic frameworks such as COSTAR help remember what a well-structured prompt should contain.

#### Prompt anatomy: goal + context

A second way to break a prompt down: its basic structure is a **goal plus context**, and the context splits into three kinds:

| Context | What it is | Examples |
|---|---|---|
| Role | The "person" who is going to answer the prompt | "You are a senior tax accountant." |
| Constraints | Conditions and boundaries for the answer | Target audience; tone, style, length; output format; keywords; cultural, historical or situational context; emotional state or tone |
| Exemplars | Examples of how the answer should look | A few good sample answers |

With enough good exemplars you may be able to remove some constraints, because the examples already show them clearly. It is a matter of trial and error.

#### System prompt template

LLMs are biased toward the content at the **beginning and end** of a prompt. The middle still matters, but it is less influential. A good template uses that:

```
 START   high-level context          (role, what this is about)
 MIDDLE  background data             (documents, facts, history)
 END     the most critical elements  (the ask, thinking
                                      instructions, output format)
```

#### Role-based prompting

Setting a role in the system prompt shapes how the model answers.

### Zero-, one- and few-shot prompting

The techniques differ in how many examples the prompt includes:

| Technique | Examples in the prompt | Relies on | Good for |
|---|---|---|---|
| Zero-shot | None | The model's pre-trained knowledge alone | Simple, common tasks |
| One-shot | One | One example to set the pattern | Setting an output format |
| Few-shot | Two or more, typically 2 to 5 | Examples that show the format and behavior | Complex or nuanced tasks |

Few-shot prompting improves performance on complex tasks without training the model:

```
 Extract the conditions from the note.

 Note: "Pt reports chest pain, hx of T2 diabetes."   <- example 1
 Conditions: chest pain; type 2 diabetes

 Note: "Follow-up for hypertension, BP controlled."  <- example 2
 Conditions: hypertension

 Note: "<the new note>"                              <- the real input
 Conditions:
```

### Chain-of-thought prompting

For complex reasoning, instruct the model to show its reasoning **step by step** before the answer. It often gives more accurate results, and the visible reasoning makes the model's decision transparent.

Asking for the thought process is especially helpful for math problems. For the arithmetic itself, use a calculator instead of trusting the model.

### Tips for improving a prompt

| Tip | What to do | Example |
|---|---|---|
| Give examples | Show the style or format you want | Asking for a tweet: include sample tweets in the style you want |
| Give a hint to complete | The model is good at completing sequences, so start the answer for it | After a long text: "The key takeaways of this article are:" |
| Ask before answering | Give the goal and context, then ask the model to ask you for any extra information it needs | "Before you answer, ask me what you need to know." |
| Ask for perspectives | Ask for answers from different perspectives, another way to set a role | "Answer as a developer, then as a customer." |
| Split the problem | Break a complex problem into smaller ones and ask for help with each | Design, then data model, then API |
| Self-evaluate | After an answer, ask how it can be improved. Like ask-before-answer, but done on top of an answer | "How could this answer be improved?" |
| Invert roles | Give the model a result and ask what prompt could have produced it | Paste a good text and ask for its prompt |

#### Readability modeling

Telling the model how **simple or complex** its answer should be. It differs from structured output, which controls the format (JSON, lists, tables): readability modeling controls how much effort the answer takes to read and understand. It suits communicating with different audiences, or exploring an unfamiliar topic step by step.

## Context engineering

### What it is

To build agents that can remember, learn and personalize their interactions, you must construct the context for **every single turn** of a conversation. This dynamic assembly and management of information is **context engineering**.

Prompt engineering is about writing the prompt. Context engineering is about deciding, on each turn, what else goes in with it: the conversation history, retrieved documents and memories.

### Why a long context is a problem

Modern LLMs can handle long contexts, but limits remain, especially for latency-sensitive applications:

| Limit | What happens |
|---|---|
| Context window | Every LLM has a maximum amount of text it can process at once. If the history exceeds it, the API call fails. |
| API cost | Providers charge by the tokens sent and received, so shorter histories cost less per turn. |
| Latency | More text takes longer to process, so the user waits longer. Compaction keeps the agent responsive. |
| Quality | As tokens grow, performance can get worse because of extra noise in the context and autoregressive errors. |

### Compaction strategies

Compaction shrinks a long conversation history to fit the context window, cutting cost and latency. It trims the history while trying to keep the most important context. For how it differs from the summarized-memory scope of an agent, see [summarized memory vs compaction](agent-orchestration.md#summarized-memory-vs-compaction).

| Strategy | How it works | Trade-off |
|---|---|---|
| Keep the last N turns | A sliding window: keep the most recent N turns, discard everything older | Simplest, but drops old context entirely |
| Token-based truncation | Count tokens from the most recent message backward, and include as many as fit a token limit (such as 4,000). Cut everything older | Respects the real limit, still drops old context |
| Recursive summarization | Periodically make another LLM call to summarize the oldest messages, then send that summary in front of the recent messages verbatim | Keeps the gist of old context, costs an extra LLM call |

```
 history:   t1  t2  t3  t4  t5  t6

 last N=3:                  [t4  t5  t6]   t1-t3 discarded

 recursive  [summary of t1-t3]  t4  t5  t6   t1-t3 condensed,
 summary:                                    not lost
```

#### When to compact

| Trigger | Compacts when | Notes |
|---|---|---|
| Count-based | The conversation passes a predefined threshold | Often "good enough" for managing context length |
| Time-based | The user has been inactive for a set time, such as 15 or 30 minutes | A background job runs, triggered by inactivity rather than size |
| Event-based | The agent detects that a task, sub-goal or topic has concluded | The agent decides when |

### Four strategies for staying in budget

In development the window rarely fills, because test inputs are small and sessions are short. In production, tool outputs are often three to five times longer than test fixtures and sessions run for more turns, so the window can fill at turn eight rather than turn fifty. The cost of not planning for this is a production outage.

| Strategy | What it does | When to apply | What continuity you lose |
|---|---|---|---|
| **Pruning** | Jumps back to an earlier message and continues from there, removing the conversation that came after | After Claude has gone down an unproductive path or accumulated debugging back-and-forth that won't help the next task | The work done after the rewind point is gone. If Claude learned something useful in that stretch, it has to relearn it |
| **Compaction** (`/compact` in Claude Code; server-side compaction in the API, a beta strategy the platform performs for you, with manual summarization as the client-side alternative) | Summarizes the history into a condensed version that preserves the key information Claude has learned. The summary costs fewer tokens than the original turns. The compaction strategies above are the do-it-yourself forms | When the session is approaching the context ceiling but you want to keep working on the same feature with the knowledge Claude has built up | Details can be lost in the summarization. Anything not captured in the summary isn't available to Claude going forward |
| **Clearing** (`/clear` in Claude Code; a new session in the API) | Starts a new conversation with empty context. Nothing from the previous session carries forward | When the next task is completely different from the current one, and previous context would only introduce bias or confusion | All session context is gone. Anything Claude needs across sessions has to live somewhere persistent, like a CLAUDE.md file |
| **Subagent handoff** | Spawns a subagent in its own isolated context window with only the task description and system prompt it needs. The subagent does the work and returns a summary | When a subtask is self-contained enough to delegate, especially exploration work where the journey clutters the main context but the answer is short | Visibility into how the subagent reached its conclusion. The intermediate steps are discarded with the subagent's context |

```
  What changed since the last useful point?
    went down a dead end   -> pruning   (rewind, drop what followed)
    same task, window full -> compaction (summarize, keep working)
    unrelated next task    -> clearing  (empty context)
    self-contained subtask -> subagent handoff (isolated window,
                                                short answer back)
```

Each strategy trades continuity for room. Pruning drops a stretch of work, compaction drops detail, clearing drops everything, and a subagent handoff drops the path to the answer.

### Prompt caching and token counting

The strategies above manage what enters the context window. Two API features reduce what you pay for what is already there.

| Feature | What it does | Use it for |
|---|---|---|
| **Prompt caching** | Stores the processing work done on a stable prefix of the request. The first request writes the prefix to the cache, and later requests that send identical content up to that point pay a fraction of the original cost | Parts of the request that rarely change across turns: a long system prompt, a large tool definition set, a reference document you query repeatedly |
| **Token counting** | The `count_tokens` endpoint takes the same request body as a messages call and returns the token count **without running inference** | Development: verify your context budget holds against real tool outputs, not just test fixtures. Production: gate requests that would exceed the window before they error |

```
  request 1:  [ stable prefix ][ new turn ]
                   |
                   +--> written to cache (full cost)
  request 2:  [ stable prefix ][ new turn ]
                   |
                   +--> reused from cache (fraction of the cost)
```

### Evaluating a memory-enabled agent

Validating an agent with memory measures three things:

| Measure | Metrics | What it tells you |
|---|---|---|
| Generation quality | Precision and recall | The system captures relevant facts accurately |
| Retrieval performance | Recall@K and strict latency budgets | Memories are found, and in time |
| Task success | Whether retrieved memories improve the agent's final output | Memory actually helps, which drives continuous improvement |

## Related

- [agent-orchestration.md](agent-orchestration.md): orchestrator-workers delegates pieces of a task to workers, the same shape as the subagent handoff above, which keeps the main context small. Its agent memory section sets summarized memory (a summary carried into the next session) against compaction (shrinking history within one conversation).
- [core-concepts.md](../core-concepts.md): prompt engineering is the "prompt / context engineering" customization approach listed there, the one that adapts a foundation model without changing its parameters. RAG is one way context gets filled, by retrieving chunks into the window, and compaction is the way it gets trimmed.
- [genai-poc.md](genai-poc.md): prompts are tuned while testing candidate models in a PoC, so a model is judged with good prompts rather than naive ones.
- [bedrock-poc.md](../../aws/aws-ai-engineering/bedrock-poc.md): the healthcare PoC there used structured prompts and few-shot examples to extract medical conditions more accurately.
- [bedrock.md](../../aws/aws-services/aws-ai/bedrock.md): Bedrock's prompt management saves and versions the prompts written this way.
- [claude-api-foundations.md](claude-api-foundations.md): prompting mode is one of three composable levers there; a more capable model can succeed zero-shot where a cheaper one needs few-shot examples. It also says oversized input errors before generation, the failure that token counting gates against.
- [evaluation-plan.md](evals/evaluation-plan.md): the memory-agent measures above (precision and recall, Recall@K, task success) are capability metrics, which the plan derives from organizational KPIs, alongside rubrics for the subjective parts of a prompt's output.
- [rubrics-and-llm-judge.md](evals/rubrics-and-llm-judge.md): how to write the rubric that grades a prompt's open-ended output, since a prompt change can only be judged against a defined good answer.
