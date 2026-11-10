# Structured outputs

This file covers the trade-offs of turning on structured outputs in the Claude API, where the API constrains the response to a schema: slower first request, more input tokens, no guarantee of success, and no combining with prefilling.

## Trade-offs

| Trade-off | What happens | What to do about it |
|---|---|---|
| First request on a new schema is slower | The API compiles the schema into a grammar before it can constrain output, which adds latency to the first call. Compiled grammars are cached for 24 hours from last use | Keep schemas stable. Steady traffic on one schema pays the cost once. A workload that changes schemas constantly pays it repeatedly |
| Input token count rises | The API adds a system prompt describing the expected format, billed like any other input token | Small per call, but count it when estimating cost at volume |
| A guaranteed schema is not a guaranteed success | A refusal or a truncation still returns output that doesn't match | Check `stop_reason` instead of assuming every response parses |
| It doesn't combine with message prefilling | JSON outputs and prefilling the assistant message are incompatible | Pick the one that fits the task |

### A guaranteed schema is not a guaranteed success

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

### Prefilling vs a schema

Prefilling starts the response for Claude. A schema constrains the **whole** response. A single request can't do both, so choose by task: prefill to steer how an answer begins, structured outputs to guarantee its shape.

## Related

- [claude-api-foundations.md](claude-api-foundations.md): the injected format prompt is billed as input tokens, and tokens are what the API meters. It also covers a different stop reason, `model_context_window_exceeded`, for hitting the context ceiling mid-generation.
- [prompt-and-context-engineering.md](prompt-and-context-engineering.md): its "give a hint to complete" tip, starting the answer for the model, is the prefilling pattern that structured outputs can't be combined with. Its readability modeling is the contrast case: it controls how hard the answer is to read, not its format.
- [extended-thinking.md](extended-thinking.md): the other per-request setting that changes the response. Thinking adds a reasoning block before the answer, while structured outputs constrain the answer itself.
