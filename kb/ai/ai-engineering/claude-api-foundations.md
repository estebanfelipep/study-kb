# Claude model family and API foundations

This file covers the Claude model tiers, how to choose a model and a reasoning mode, how the API meters tokens and the context window, and the four ways to call it: synchronous, streaming, async and batch.

## Sources

- [Claude Certified Developer: Foundations (Anthropic Skilljar)](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations): Anthropic's learning path. This file comes from its Module 1 (foundations).

## The Claude model family

Claude is a family of models in four tiers. Each tier trades cost, latency and capability differently.

| Tier | Built for | Pick it when |
|---|---|---|
| Haiku | Speed and cost efficiency | The task fits its capability envelope (lookups, classification) |
| Sonnet | The balanced default | Most production workloads |
| Opus | Demanding work above the Sonnet envelope | Sonnet's output isn't good enough on your eval |
| Fable | The most capable tier: the hardest reasoning, coding and agentic work | Maximum intelligence is the priority |

## Three separate levers

Model choice, reasoning mode and prompting mode are separate decisions that compose. Model choice picks the family member. The other two are set per request.

Pick one option per row. The rows don't constrain each other.

| Lever | Options | Decided |
|---|---|---|
| Model choice | Haiku, Sonnet, Opus, Fable | Which model runs |
| Reasoning mode | Off, on (reason before answering) | Per request |
| Prompting mode | Zero-shot, one-shot, multi-shot | Per request |

- **Reasoning mode:** whether the model reasons before it answers. It earns its cost on hard, multi-step problems and is wasted on lookups and classification.
- **Prompting mode:** the levers trade against model choice. A more capable model often succeeds zero-shot on a task where a smaller model needs a few examples to match the structure, so adding examples can let a cheaper model do the job. The modes themselves are in [prompt-and-context-engineering.md](prompt-and-context-engineering.md).

**Rule of thumb:** pick the smallest model, the simplest reasoning and the simplest prompting that meet your eval, and add capability only where the eval says you need it.

## Tokens, the context window and sampling

| Concept | What to know |
|---|---|
| Token | The unit of input, output and cost. Budget in tokens, not words, since that is what the API meters and the context window measures. |
| Context window | A fixed token budget that holds the whole request at once. Managing the history is the application's job. |
| Oversized input | The request errors before generation starts. |
| Ceiling hit mid-generation | The output is truncated and the stop reason is `model_context_window_exceeded`. |
| Sampling | Generation is non-deterministic: the same prompt can return different wording on each run. |

Because of sampling, testing on exact text is unreliable. That is the problem evals are built for, see [design-document-and-llm-judge.md](design-document-and-llm-judge.md).

## Calling Claude: sync, streaming, async, batch

A developer reaches Claude over a REST API, usually through an SDK. Choose the call pattern by whether a user is waiting and whether the workload is real-time or bulk offline.

### Synchronous

You send the request and wait for the complete response to come back in one piece, then act on it.

- **Use it when:** responses are short, or it's a backend job where no one is waiting.

### Streaming

The response is sent in pieces as the model generates it, and your code reassembles the pieces into the final message. Claude exposes streaming over the same HTTP connection using server-sent events.

- **Use it when:** the response is long or a user is watching. Output appears immediately instead of after a blank-screen wait.

### Async

Non-blocking async/await calls that don't tie up the application thread. The request still returns in real time, but the application can handle other work while it waits.

- **Use it when:** you need concurrency without blocking.
- **Python:** a separate async client, `AsyncAnthropic`.
- **TypeScript:** the standard `Anthropic` client is already Promise-based, so you `await` calls directly. There is no separate async client class.

### Message Batches API

A separate pattern for bulk offline workloads. You submit a large set of requests in one call, receive an identifier, and poll for completion. A batch can take up to 24 hours, and it costs less per token than synchronous requests in exchange for that latency.

- **Use it when:** latency doesn't matter and the work is bulk and offline.

Worked examples of picking between synchronous and batch:

| Use case | Right API pattern | Why |
|---|---|---|
| A user uploads a photo and expects an immediate classification | Synchronous API | Real-time response is required. Batch latency is unacceptable for interactive use. |
| A nightly pipeline classifies 5,000 customer records | Message Batches API | Latency is not a constraint. Batch cost reduction and asynchronous processing are both valuable. |
| An evaluation run tests a new prompt against 2,000 examples | Message Batches API | Offline task with no real-time requirement. Batch is the correct pattern. |
| A chatbot generates a reply to a user's message | Synchronous API | The user is waiting, and batch would add unacceptable delay. |

### Choosing a pattern

```
  user waiting?
    yes -> long response?  yes -> streaming
                           no  -> synchronous (or async for concurrency)
    no  -> bulk, can wait up to 24h?  yes -> Message Batches API
                                      no  -> synchronous / async
```

## Related

- [prompt-and-context-engineering.md](prompt-and-context-engineering.md): defines zero-, one- and few-shot prompting, the prompting-mode lever here, and covers keeping a conversation within the context window.
- [design-document-and-llm-judge.md](design-document-and-llm-judge.md): the eval and cost-and-latency-budget practice that tells you which model and reasoning mode are enough.
- [genai-poc.md](genai-poc.md): the PoC's model selection and evaluation step is where the cost, latency and capability trade-off between tiers gets decided.
- [core-concepts.md](../core-concepts.md): the vendor-neutral view of integrating and adapting foundation models, of which calling Claude over its API is one case.
