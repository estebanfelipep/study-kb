# Extended thinking

This file covers extended thinking, the Claude setting that makes the model write out its reasoning before it answers: what comes back, what it costs, and the rule for handing thinking blocks back to the API when tools are involved.

## What it is

Prompting techniques shape what Claude produces. Extended thinking shapes **how much work Claude does before it answers**. With it on, the model "thinks out loud": it writes its step-by-step reasoning first, then gives the final answer. Your job is to decide when that extra work is worth the cost, and to handle the reasoning the API sends back.

It is the API-level form of the reasoning-mode lever in [claude-api-foundations.md](claude-api-foundations.md).

## What comes back: a thinking block

The reasoning returns as its own **thinking block** in the response, positioned just ahead of the block that holds the actual answer.

```
  response content
 +------------------------------------------------------+
 | 1. thinking block   step-by-step reasoning + signature|
 +------------------------------------------------------+
 | 2. text block       the final answer                  |
 +------------------------------------------------------+
```

## Cost

Thinking tokens cost the same as output tokens. Running a simple task at high effort therefore pays for accuracy the task doesn't need.

| Task | Thinking worth it? | Why |
|---|---|---|
| Hard, multi-step problem | Yes | The extra reasoning is what improves the answer |
| Lookup or classification | No | The tokens are billed as output but add no accuracy |

## The carry-back rule: thinking blocks must return unchanged

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

## Related

- [claude-api-foundations.md](claude-api-foundations.md): extended thinking is how the reasoning-mode lever there is switched on per request, and it is separate from choosing the model tier. The reasoning mode earns its cost on hard multi-step problems and is wasted on lookups.
- [structured-outputs.md](structured-outputs.md): both are per-request settings that change the response, but they sit on different axes: thinking adds a reasoning block ahead of the answer, structured outputs constrain the answer's format.
