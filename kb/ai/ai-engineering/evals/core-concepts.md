# Evals core concepts

This file covers the building blocks the other evals files rest on: what an eval is, and the records an agent leaves behind, the span, the trace and the session.

## What an eval is

An **eval** is a check of a generative system's output against defined criteria. Sampling makes the same prompt return different wording each run, so testing on exact text is unreliable ([claude-api-foundations.md](../claude-api-foundations.md)), and evals replace it. The criteria come from the feature's success criteria ([design-document.md](../design-document.md)) or, at organizational scale, from KPIs ([evaluation-plan.md](evaluation-plan.md)).

[genai-poc.md](../genai-poc.md) names three types by who or what judges the output: human, model-based and metrics-based.

## What an agent leaves behind: span, trace, session

| Term | What it is |
|---|---|
| Span | A single timed step, such as a model call or a tool call |
| Trace | A factual, immutable record of **one agent invocation**, a single turn. It captures the model inputs, the responses and the tool calls, in order. A trace is built from spans |
| Session | The **entire multi-turn conversation** between a user and the agent. It can contain several traces |

```
  session (the whole conversation)
  +----------------------------------------------------------+
  |  trace 1 (turn 1)        trace 2 (turn 2)     trace 3 ...|
  |  +-------------------+   +----------------+              |
  |  | span: model call  |   | span: model    |              |
  |  | span: tool call   |   | span: tool     |              |
  |  | span: model call  |   | span: model    |              |
  |  +-------------------+   +----------------+              |
  +----------------------------------------------------------+
```

## Related

- [evaluation-plan.md](evaluation-plan.md): step 7 of its roadmap evaluates trajectories and intermediate steps such as tool calls, which are the spans inside a trace.
- [hill-climb-lifecycle.md](hill-climb-lifecycle.md): the chat logs it analyzes and the sampled production chats it monitors are sessions, each made of traces.
- [synthetic-data-for-agent-evaluation.md](synthetic-data-for-agent-evaluation.md): user simulation produces whole sessions, one trace per simulated turn.
- [llm-judge.md](llm-judge.md): the model-based evaluation type, one model grading another's output against a rubric.
