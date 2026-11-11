# Tool use

This file covers how Claude chooses among tools by their descriptions, what to do when descriptions overlap, how a failing tool should report back, and MCP, the standard that supplies ready-made tool definitions from a server: what a server exposes, its transports, how to set one up in Claude Code (transport, scope, config location), how it authenticates, and the context cost of connecting one.

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

## When a tool fails

When your code runs a tool and it fails, return the result to Claude with `is_error` explicitly set to `true`, never as a silent empty result. With the error returned, the model can try a different approach, ask for clarification or stop. A tool that drops its own error and returns nothing produces a confident but wrong answer downstream, because the model reads the empty result as data. The retriable-vs-terminal sorting of errors is in [design-document.md](design-document.md).

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

### What a server exposes

An MCP server is a process that exposes three things to any MCP client. When Claude Code connects, it discovers the tools the server provides and can invoke them during a session. The capability is built once, and every MCP client that connects gets it without re-implementing the integration.

| Exposes | What it is | Who decides it enters the context |
|---|---|---|
| **Tool** | A capability the model can call | The model, by reading the description |
| **Resource** | Read-only data the server exposes for the client to fetch and place into context directly | The client, with no tool call by the model |
| **Prompt** | A pre-written instruction template, so a client can invoke a vetted prompt by name instead of each user writing their own | The user or client, by naming the prompt |

### Context cost of connecting a server

Each connected server adds its tool definitions to the context window whether or not the tools get used. Connect deliberately and control loading cost. When tool selection starts degrading after a fixed number of turns, look at the window first, not the schema: see [prompt-and-context-engineering.md](prompt-and-context-engineering.md#why-a-long-context-is-a-problem).

### Transports

MCP runs over one of two transports. Which one to use depends on where the server lives.

| | stdio | Streamable HTTP |
|---|---|---|
| Server lives | Locally | Remotely |
| How the application connects | It spawns the server as a subprocess | It connects over the network via HTTP |
| How messages move | Standard input and output | POST for client-to-server messages, plus an optional GET-based SSE stream for server-initiated messages |

- **stdio** is right for a local tool, a personal script or a development server on your own machine. It does not work for a server you want to share across a team or host remotely.
- **HTTP** is the recommended transport for any server that doesn't run locally: you register its URL and the client connects over the network. Shared team servers and hosted integrations use it.

An older SSE-only transport exists but has been superseded by Streamable HTTP and is no longer recommended for new servers. Treat SSE in existing configuration or documentation as a legacy option.

### Setting up a server in Claude Code

Transport and scope are independent decisions with dependent consequences. Transport follows where the server runs. Scope follows who should have it: **local** scope keeps a server personal, **project** scope shares it with the repo through `.mcp.json`, and **enterprise** scope deploys it organization-wide through managed settings.

| Context | Transport | Scope | Config location | Secrets handling |
|---|---|---|---|---|
| Personal local tool (runs on your machine only) | stdio | Local | `~/.claude.json` (per-project entry) | Environment variables only. Never in the config file |
| Shared team server (all teammates connect to the same service) | HTTP | Project | `.mcp.json` committed to the repo root | OAuth or environment variables. API keys must never be committed to `.mcp.json` |
| Personal experiment (not ready to share) | stdio or HTTP | Local | Personal Claude settings | Environment variables only |
| Organization-wide deployment (admin-managed) | HTTP | Enterprise | Managed settings (admin-controlled) | Managed by the administrator. Config locked to prevent override |

The combination must match the deployment intent. A shared team server needs HTTP and project or enterprise scope. A stdio server in `.mcp.json` looks shareable but isn't: teammates' machines don't have the local process it spawns.

### Authentication by service type

Pick the pattern from who the credential identifies.

| Service type | Pattern | How it works |
|---|---|---|
| Remote service with user identity | **OAuth** | The server returns a 401 Unauthorized to signal that authentication is required. The client starts a browser-based sign-in flow, and after the user approves access a token is issued and stored. No one copies a secret by hand. Used for cloud services, SaaS tools and any integration where the user's identity is part of authorization. The Linear MCP server uses it. The GitHub server instead authenticates with a personal access token passed as a header |
| Remote service with service identity | **API key in an environment variable** | The key identifies the service account. It is never committed to a configuration file and lives in the environment where the process runs. A CI pipeline using the Agent SDK has the key injected as a secret by the pipeline runner, not baked into the code |
| Local service with file system access | **stdio, no network authentication** | The security boundary is the file-system permission model. A denying rule in the settings files is the governance layer |

Two habits make credential rotation cheaper:

- **Scope each credential to the narrowest access its task needs,** so a leaked key reaches only what that integration required.
- **Keep a record of which services use each credential,** so a rotation doesn't break a consumer you forgot about.

## Related

- [design-document.md](design-document.md): its failure handling sorts errors into retriable and terminal and explains why the `is_error` flag matters; its trust boundary covers tool output as an injection vector and least privilege for the credentials an MCP server holds.
- [agent-orchestration.md](agent-orchestration.md): an agent is an LLM using tools in a loop and picks them from their descriptions, which is why that file says toolsets must be designed clearly. An MCP server is one way to supply the toolset without writing it.
- [claude-api-foundations.md](claude-api-foundations.md): Streamable HTTP's optional SSE stream is the same server-sent events mechanism that its streaming call pattern uses. Its strict tool use, one of the structured-outputs forms, validates the arguments Claude passes to the tools defined here.
- [prompt-and-context-engineering.md](prompt-and-context-engineering.md): connected servers' tool definitions spend context-window budget, which that file's strategies for staying in budget manage.
