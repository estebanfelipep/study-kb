# Claude model family and API foundations

This file covers the Claude model tiers, how to choose a model and a reasoning mode, how the API meters tokens and the context window, the four ways to call it (synchronous, streaming including what to do when a stream stops early, async and batch), multimodal input (three ways to send an image and what it costs), and the settings that change the response: extended thinking and structured outputs.

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

- **Reasoning mode:** whether the model reasons before it answers. It earns its cost on hard, multi-step problems and is wasted on lookups and classification. [Extended thinking](#extended-thinking) is how it is turned on per request.
- **Prompting mode:** the levers trade against model choice. A more capable model often succeeds zero-shot on a task where a smaller model needs a few examples to match the structure, so adding examples can let a cheaper model do the job. The modes themselves are in [prompt-and-context-engineering.md](prompt-and-context-engineering.md).

**Rule of thumb:** pick the smallest model, the simplest reasoning and the simplest prompting that meet your eval, and add capability only where the eval says you need it.

There is no globally correct model, only the right one for a task at a quality standard, so make the trade-off measurable instead of reaching for the most capable model by default:

- **Start with Sonnet.**
- **Move up to Opus** only when an eval shows Sonnet missing the quality bar.
- **Move down to Haiku** only when an eval shows the quality drop is acceptable for the task.

## Tokens, the context window and sampling

| Concept | What to know |
|---|---|
| Token | The unit of input, output and cost. Budget in tokens, not words, since that is what the API meters and the context window measures. |
| Context window | A fixed token budget that holds the whole request at once. Managing the history is the application's job. |
| Oversized input | The request errors before generation starts. |
| Ceiling hit mid-generation | The output is truncated and the stop reason is `model_context_window_exceeded`. |
| Sampling | Generation is non-deterministic: the same prompt can return different wording on each run. |

Because of sampling, testing on exact text is unreliable. That is the problem evals are built for: see [design-document.md](design-document.md) for the feature-level eval and [evaluation-plan.md](evals/evaluation-plan.md) for building evals from organizational KPIs.

## Calling Claude: sync, streaming, async, batch

A developer reaches Claude over a REST API, usually through an SDK. Choose the call pattern by whether a user is waiting and whether the workload is real-time or bulk offline.

### Synchronous

You send the request and wait for the complete response to come back in one piece, then act on it.

- **Use it when:** responses are short, or it's a backend job where no one is waiting.

### Streaming

The response is sent in pieces as the model generates it, and your code reassembles the pieces into the final message. Claude exposes streaming over the same HTTP connection using server-sent events.

- **Use it when:** the response is long or a user is watching. Output appears immediately instead of after a blank-screen wait.
- **Perceived latency:** streaming returns the first token as soon as it is ready, so a reply that starts in 300 ms feels faster than the same content delivered as one block after two seconds, even with identical total generation time.
- **Streaming with tool use needs extra handling:** a non-streaming response arrives as one object with `tool_use` blocks directly accessible, but a stream is a sequence of server-sent events and a `tool_use` block accumulates across several delta events before it is complete. Consuming the stream without accounting for that gives partial tool inputs and silent downstream failures.

#### When the stream stops early

Your code holds a half-built message until the last piece arrives, so three rules keep that state from corrupting the conversation.

| Rule | What to do |
|---|---|
| Track completion on purpose | A turn is usable only once `message_stop` has arrived. Until then, treat what you've accumulated as provisional |
| On an interrupted stream, discard the partial turn | Don't save it to history. Retry the request. Committing a half-built turn is exactly what breaks the following request |
| Check `stop_reason` from `message_delta` before continuing a loop | `tool_use` means your assembled tool calls are ready to run. Any other value means you're on a different path, not the tool path |

```
  stream arrives
        |
        v
  message_stop received?
    no  -> interrupted: discard the partial turn, retry the request
    yes -> read stop_reason (from message_delta)
             tool_use -> run the assembled tool calls, continue the loop
             other    -> not the tool path
```

For short responses, or backend jobs where no one is waiting on the output, a non-streamed call is simpler and removes the partial-state risk entirely.

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

Calling the synchronous API in a loop over a bulk job is not batching: it pays the synchronous price and gets none of the batch discount. Batch latency is also non-deterministic, so only offline work with no one waiting fits it.

## Multimodal input

Images (and PDFs) go into a message as content blocks. Work out how each input is sent and what it costs before writing the ingestion code.

### Three ways to send an image

| Method | How it works | Overhead | Use it when |
|---|---|---|---|
| Base64 | Encode the image bytes as a base64 string and put it directly in the message block | The full payload travels with every request, inflating request size and latency on large images. Sending the same image repeatedly multiplies the cost | A one-off image, where an upload step would add complexity for no payoff |
| URL reference | Pass a publicly reachable URL in the source block, and Claude fetches the image at request time | No payload in the request, but the URL must be stable, public and reachable at the moment Claude fetches it | The image is already hosted at a stable public URL you control. Not for anything behind auth, signed with a short expiry, or not guaranteed reachable when the request runs |
| Files API | Upload the file once in a separate call, get a `file_id`, and reference that ID in later messages | A one-time upload, then near-zero payload per request. In beta, and not available on Bedrock or Vertex AI, so check your platform | The same image or PDF appears in several requests, or is large enough that re-sending it would dominate request size. Also when asset management should live apart from inference calls, and for images that stay in a multi-turn conversation, since the `file_id` adds no payload weight as the history grows |

### What an image costs

Each image costs `⌈width / 28⌉ × ⌈height / 28⌉` visual tokens, and the per-image ceiling differs by model tier.

| Image | Calculation | Visual tokens |
|---|---|---|
| 280 × 280 thumbnail | 10 × 10 | 100 |
| 1000 × 800 photo | 36 × 29 | 1,044 |
| 4000 × 3000 original | 143 × 108 | 15,444, before the model's per-image ceiling applies |

A high-resolution original on the newest models can cost many times what a thumbnail costs in a test set. Run the formula against the **largest input you expect in production**, not the inputs you have on hand. Compare with [token counting](prompt-and-context-engineering.md#prompt-caching-and-token-counting) for checking a whole request.

### Prompting for images

A visual-analysis prompt should name how Claude handles each kind of ambiguity, which a text-only prompt never needs. For example: "If objects overlap, describe each separately and note the overlap."

## Settings that change the response

Two per-request settings change what comes back, on different axes: thinking adds a reasoning block ahead of the answer, while structured outputs constrain the answer itself.

### Extended thinking

This is the Claude setting that makes the model write out its reasoning before it answers.

Prompting techniques shape what Claude produces. Extended thinking shapes **how much work Claude does before it answers**. With it on, the model "thinks out loud": it writes its step-by-step reasoning first, then gives the final answer. Your job is to decide when that extra work is worth the cost, and to handle the reasoning the API sends back.

It is the API-level form of the reasoning-mode lever above.

#### What comes back: a thinking block

The reasoning returns as its own **thinking block** in the response, positioned just ahead of the block that holds the actual answer.

```
  response content
 +------------------------------------------------------+
 | 1. thinking block   step-by-step reasoning + signature|
 +------------------------------------------------------+
 | 2. text block       the final answer                  |
 +------------------------------------------------------+
```

#### Cost

Thinking tokens cost the same as output tokens. Running a simple task at high effort therefore pays for accuracy the task doesn't need.

| Task | Thinking worth it? | Why |
|---|---|---|
| Hard, multi-step problem | Yes | The extra reasoning is what improves the answer |
| Lookup or classification | No | The tokens are billed as output but add no accuracy |

#### The carry-back rule: thinking blocks must return unchanged

When extended thinking is on **and** the conversation uses tools, every thinking block received must go back to the API **exactly as it arrived** on the next turn.

Each block carries a **signature** that confirms the reasoning wasn't tampered with. If you edit, summarize or drop the block, the signature no longer matches and the API rejects the request.

```
  turn N (response)              turn N+1 (your request)
 +------------------+           +----------------------------+
 | thinking + sig   |  ------>  | thinking + sig  (unchanged)|
 | tool_use         |           | tool_use                   |
 +------------------+           | tool_result                |
                                +----------------------------+

  edited / summarized / dropped thinking block
     -> signature mismatch -> request rejected
```

| What you do with the block | Result |
|---|---|
| Send it back exactly as received | Accepted |
| Edit it | Rejected: signature stops matching |
| Summarize it | Rejected: signature stops matching |
| Drop it | Rejected |

### Structured outputs

With structured outputs on, the API constrains the response to a schema. It costs a slower first request, more input tokens, no guarantee of success, and no combining with prefilling. The injected format prompt is billed as input tokens, which the token metering above counts.

#### Two forms

| Form | What it constrains |
|---|---|
| JSON outputs | The final response, checked against a schema |
| Strict tool use | The arguments Claude passes to your tools, validated against the tool's schema |

Use them when prompt-level instructions aren't enough because untested inputs still break your parser. Both carry the trade-offs below.

#### Trade-offs

| Trade-off | What happens | What to do about it |
|---|---|---|
| First request on a new schema is slower | The API compiles the schema into a grammar before it can constrain output, which adds latency to the first call. Compiled grammars are cached for 24 hours from last use | Keep schemas stable. Steady traffic on one schema pays the cost once. A workload that changes schemas constantly pays it repeatedly |
| Input token count rises | The API adds a system prompt describing the expected format, billed like any other input token | Small per call, but count it when estimating cost at volume |
| A guaranteed schema is not a guaranteed success | A refusal or a truncation still returns output that doesn't match | Check `stop_reason` instead of assuming every response parses |
| It doesn't combine with message prefilling | JSON outputs and prefilling the assistant message are incompatible | Pick the one that fits the task |

#### A guaranteed schema is not a guaranteed success

Two cases still return output that doesn't match the schema:

| Case | What happened | `stop_reason` |
|---|---|---|
| Refusal | The model declined for safety reasons | `refusal` |
| Truncation | The response hit the `max_tokens` limit and stopped mid-structure | `max_tokens` |

```
  response arrives
        |
        v
  stop_reason?
    refusal     -> handle the refusal, nothing to parse
    max_tokens  -> output is cut mid-structure, don't parse
    otherwise   -> parse against the schema
```

#### Prefilling vs a schema

Prefilling starts the response for Claude. A schema constrains the **whole** response. A single request can't do both, so choose by task: prefill to steer how an answer begins, structured outputs to guarantee its shape.

## Related

- [tool-use.md](tool-use.md): strict tool use validates the arguments of the tools whose schemas and descriptions that file covers writing.
- [prompt-and-context-engineering.md](prompt-and-context-engineering.md): defines zero-, one- and few-shot prompting, the prompting-mode lever here, and covers keeping a conversation within the context window: compaction, the four strategies for staying in budget, prompt caching and token counting. Its "give a hint to complete" tip, starting the answer for the model, is the prefilling pattern that structured outputs can't be combined with. Its readability modeling is the contrast case: it controls how hard the answer is to read, not its format.
- [design-document.md](design-document.md): the eval and cost-and-latency-budget practice that tells you which model and reasoning mode are enough, with the levers (model, context size, tool calls, streaming, caching) that budget is tuned with.
- [genai-poc.md](genai-poc.md): the PoC's model selection and evaluation step is where the cost, latency and capability trade-off between tiers gets decided.
- [core-concepts.md](../core-concepts.md): the vendor-neutral view of integrating and adapting foundation models, of which calling Claude over its API is one case.
- [hill-climb-lifecycle.md](evals/hill-climb-lifecycle.md): the "smallest model that meets your eval" rule is applied there as thresholds that must be met before launch, then hill climbed.
