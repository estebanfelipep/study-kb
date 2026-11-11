# Tool use

This file covers how Claude chooses among tools by their descriptions, what to do when descriptions overlap, and MCP, the standard that supplies ready-made tool definitions from a server, with its two transports and the context cost of connecting a server.

## Description-based routing

Claude selects a tool by reading the tool descriptions, so the description is the routing rule. The same holds whether you wrote the tool schema yourself or received it from an MCP server (below).

### When descriptions overlap

When the failure is overlapping descriptions, the fix is consistent: add one sentence to a description that names **when not to call the tool**. That sentence gives Claude a decision boundary.

Write the exclusion sentence into every description at design time, not after the first wrong call shows up in a log. Two tools that both say "use this to find information" are indistinguishable from Claude's side, even when their input schemas look nothing alike.

If the descriptions can't be cleanly separated even with exclusion conditions, the tools may need to be **merged into one tool with a type parameter**.

| Situation | Fix |
|---|---|
| Two descriptions both fit the same request | Add one sentence to each naming when not to call it |
| Exclusion sentences still don't separate them | Merge them into one tool with a type parameter |

## Model Context Protocol (MCP)

### Who owns the tool definitions

With the tool-schema approach, the application writes a schema and an execution function for every capability it wants Claude to use, and maintains them as the underlying API evolves. An MCP server moves that work to whoever runs the server.

GitHub is the example: it exposes repositories, pull requests, issues, projects and more. Wiring all of that by hand means a schema and an execution function for each piece, kept current as GitHub's API changes. An MCP server for GitHub has already done that work.

| | Hand-written tools | MCP server |
|---|---|---|
| Who writes the schemas and execution code | Your application | The server's author |
| Who maintains them as the API evolves | You | The server's author |
| How the application learns the tools | They're defined in your code | It connects to the server and receives the full list of tools |
| How Claude chooses a tool | By its description | By its description. The mechanism is identical |

```
  application                         MCP server (e.g. GitHub)
  +-----------+   1. connect          +------------------+
  |           | --------------------> |                  |
  |           | <-------------------- |  tool list       |
  |           |   2. full tool list   |  (schemas)       |
  |  Claude   |                       |                  |
  |  picks a  |   3. call chosen tool |  runs it against |
  |  tool by  | --------------------> |  the GitHub API  |
  |  its      | <-------------------- |                  |
  |  descrip- |   4. result           +------------------+
  |  tion     |
  +-----------+
```

Only the ownership changes. Claude's selection still depends on the descriptions, so the overlap fixes above apply to a server's tools as much as to your own.

### Context cost of connecting a server

Each connected server adds its tool definitions to the context window whether or not the tools get used. Connect deliberately and control loading cost. When tool selection starts degrading after a fixed number of turns, look at the window first, not the schema: see [prompt-and-context-engineering.md](prompt-and-context-engineering.md#why-a-long-context-is-a-problem).

### Transports

MCP runs over one of two transports. Which one to use depends on where the server lives.

| | stdio | Streamable HTTP |
|---|---|---|
| Server lives | Locally | Remotely |
| How the application connects | It spawns the server as a subprocess | It connects over the network via HTTP |
| How messages move | Standard input and output | POST for client-to-server messages, plus an optional GET-based SSE stream for server-initiated messages |

An older SSE-only transport exists but is deprecated. New integrations should use Streamable HTTP.

## Related

- [agent-orchestration.md](agent-orchestration.md): an agent is an LLM using tools in a loop and picks them from their descriptions, which is why that file says toolsets must be designed clearly. An MCP server is one way to supply the toolset without writing it.
- [claude-api-foundations.md](claude-api-foundations.md): Streamable HTTP's optional SSE stream is the same server-sent events mechanism that its streaming call pattern uses. Its strict tool use, one of the structured-outputs forms, validates the arguments Claude passes to the tools defined here.
- [prompt-and-context-engineering.md](prompt-and-context-engineering.md): connected servers' tool definitions spend context-window budget, which that file's strategies for staying in budget manage.
