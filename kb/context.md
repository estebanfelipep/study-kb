# Glossary

This file holds the vocabulary shared across the subjects in this KB: terms, abbreviations, and service nicknames. Entries follow `../.claude/skills/kb-intake/references/glossary-format.md`.

## Language

**ACM**: AWS Certificate Manager. Provisions and renews the SSL/TLS certificates behind encryption in transit. See [acm.md](aws/aws-services/aws-apis/acm.md).

**Agent (AI)**: An LLM that uses tools in a loop, deciding from each result whether to call another tool or stop. It directs its own process. See [agent-orchestration.md](ai/ai-engineering/agent-orchestration.md).
_Avoid:_ agentic AI, autonomous agent

**Agentic system**: Any system that combines LLMs and tools: either a workflow or an agent. See [agent-orchestration.md](ai/ai-engineering/agent-orchestration.md).

**Apache Hudi**: One of the three common open table formats. See [open-table-formats.md](data-engineering/open-table-formats.md).

**Apache Iceberg**: The open table format most widely adopted on AWS, developed at Netflix. See [open-table-formats.md](data-engineering/open-table-formats.md).

**Apache Spark**: The open-source distributed engine for processing data too big for one machine, in batch and streaming. Runs under Glue and EMR. See [apache-spark.md](data-engineering/apache-spark.md).

**Automation**: Running a single repetitive task without manual effort. See [orchestration-and-automation.md](data-engineering/orchestration-and-automation.md).

**Autorater**: An automated system, typically a foundation model itself, that evaluates, scores or critiques another generative AI application's outputs against a rubric. The same mechanism as an LLM judge. See [rubrics-and-llm-judge.md](ai/ai-engineering/evals/rubrics-and-llm-judge.md).

**BM25**: A keyword search algorithm: the ranking function search engines use to estimate how relevant documents are to a search query. See [core-concepts.md](ai/core-concepts.md).

**Break-even analysis**: Finding the usage volume that justifies a PoC's one-time development and ongoing operational costs. See [genai-poc.md](ai/ai-engineering/genai-poc.md).

**Cached changes**: Changes made to a source database while a DMS full load runs. DMS stores them and applies them once the full load finishes, before ongoing replication starts. See [dms.md](aws/aws-services/aws-databases/dms.md).

**Carry-back rule**: With extended thinking on and tools in use, every thinking block must go back to the API exactly as it arrived on the next turn. An edited, summarized or dropped block fails its signature check and the request is rejected. See [claude-api-foundations.md](ai/ai-engineering/claude-api-foundations.md).

**Catastrophic forgetting**: The main risk of Continued Pre-Training: the model loses general skills. Mixing in general text and evaluating on general tasks guard against it. See [core-concepts.md](ai/core-concepts.md).

**CDC**: Change data capture. Replicating a database's ongoing inserts, updates and deletes rather than reloading it. See [replicating-databases-to-the-lake.md](data-engineering/replicating-databases-to-the-lake.md).

**CDO**: Chief data officer. The executive who builds a data-driven culture and owns data and AI strategy. See [data-personas.md](data-engineering/data-personas.md).

**Chain-of-thought prompting**: Instructing a model to show its reasoning step by step before answering, for more accurate and transparent results on complex reasoning. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).
_Avoid:_ CoT

**Chunking**: Splitting large content into smaller pieces, so it is easier to search and doesn't fill the context window. Fixed-size or structural. See [core-concepts.md](ai/core-concepts.md).

**CIA triad**: Confidentiality, integrity and availability, the three goals of data security. See [data-security-and-monitoring.md](data-engineering/data-security-and-monitoring.md).

**Classifier**: The part of a Glue crawler that infers a data store's format and schema, built in (JSON, CSV, Avro, …) or custom. The first classifier in the list that recognizes the data wins. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**Claude Agent SDK**: Anthropic's library (Python, TypeScript) that runs the agent loop inside your own process and handles context management and tool registration, while your code executes the tools. Always set `settingSources` explicitly. See [agent-orchestration.md](ai/ai-engineering/agent-orchestration.md).

**Claude Managed Agents**: The public-beta Anthropic service where Anthropic runs the agent loop and the sandbox, and your app streams events in and results back. Sessions are stored server-side, so they aren't eligible for Zero Data Retention or a HIPAA BAA. See [agent-orchestration.md](ai/ai-engineering/agent-orchestration.md).

**Cleaned zone**: The data lake zone that holds each source after filtering anomalies, standardizing formats and correcting invalid values, still not combined with other sources. See [data-lake-zones.md](data-engineering/data-lake-zones.md).

**Column statistics**: Per-column minimum, maximum, null count and distinct-value count computed for a Data Catalog table, to optimize queries. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**Columnar format**: A file or storage layout that stores each column together, so queries read only the columns they need. Parquet and ORC are columnar file formats. See [data-lakes-and-warehouses.md](data-engineering/data-lakes-and-warehouses.md).

**Compaction (context)**: Shrinking a long conversation history to fit the context window, by keeping the last N turns, truncating by tokens or recursively summarizing older messages. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).

**Compaction (table)**: Merging many small data files into fewer, larger ones so queries open fewer files, a feature of open table formats. See [open-table-formats.md](data-engineering/open-table-formats.md).

**Connector (Glue)**: Code that lets Glue communicate with a data store, as a source or a target. Built in, from AWS Marketplace, or custom. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**Context engineering**: Assembling and managing the information an LLM sees on every turn: history, retrieved documents and memories. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).

**Context window**: The maximum amount of text an LLM can process at once. A history that exceeds it makes the API call fail. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).

**CPT**: Continued Pre-Training. Training a foundation model further on unlabeled domain text, with the same next-token objective as the original pre-training, before fine-tuning. See [core-concepts.md](ai/core-concepts.md).

**Crawler**: A Glue component that scans data, infers format and schema, and writes tables to the Data Catalog. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**CTAS**: `CREATE TABLE AS SELECT`. An Athena statement that writes a query's results to S3 as new files and registers them as a table. See [athena.md](aws/aws-services/aws-analytics/athena.md).

**Curated zone**: The data lake zone that holds data merged, joined or aggregated with other datasets, quality-assured and consumption-ready for analytics and ML. See [data-lake-zones.md](data-engineering/data-lake-zones.md).

**Customer gateway**: The on-premises end of an AWS Site-to-Site VPN. See [site-to-site-vpn.md](aws/aws-services/aws-networking/site-to-site-vpn.md).

**DAG**: Directed acyclic graph. A workflow of tasks and their dependencies, as defined in Apache Airflow. See [orchestration-and-automation.md](data-engineering/orchestration-and-automation.md).

**Data catalog**: The metadata store that makes a data lake's contents findable: what data exists, where, its quality and how it's used. It stores metadata, not the data. See [modern-data-architecture.md](data-engineering/modern-data-architecture.md).

**Data discovery**: Finding and understanding an organization's relevant data sources and how they relate; the first step of a data project. See [data-discovery.md](data-engineering/data-discovery.md).

**Data lake**: A centralized repository for structured, semi-structured and unstructured data at scale, stored without extensive preprocessing. On AWS, built on S3. See [data-lakes-and-warehouses.md](data-engineering/data-lakes-and-warehouses.md).

**Data quality at rest**: Checking the quality of data already stored and cataloged. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**Data quality in transit**: Checking data inside an ETL job, so bad data is filtered out before it's loaded. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**Data silo**: An isolated, incompatible data store optimized for one department or use case. See [modern-data-architecture.md](data-engineering/modern-data-architecture.md).

**Data swamp**: A data lake without a catalog: files nobody can find or trust. See [modern-data-architecture.md](data-engineering/modern-data-architecture.md).

**Data warehouse**: A columnar SQL analytics database for curated, modeled data, with schema-on-write. On AWS, Redshift. See [data-lakes-and-warehouses.md](data-engineering/data-lakes-and-warehouses.md).

**Database (Data Catalog)**: A container of tables in the Glue Data Catalog, such as `db_raw`. The convention is one database per data lake zone. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**DataSync agent**: The software DataSync runs on premises, next to the storage, to read files and copy them to AWS. See [datasync.md](aws/aws-services/aws-migration-and-transfer/datasync.md).

**DDL**: Data definition language. SQL statements that define tables, such as `CREATE EXTERNAL TABLE`, one way to populate the Data Catalog. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**Delta Lake**: One of the three common open table formats. See [open-table-formats.md](data-engineering/open-table-formats.md).

**Design document**: A written record, made before production code, of an LLM feature's success criteria, failure handling, cost and latency budget and trust boundary. See [design-document.md](ai/ai-engineering/design-document.md).

**Detect PII**: The Glue transform that detects sensitive data in a job and masks or removes it. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**Directory bucket**: The S3 bucket type that S3 Express One Zone stores data in. It lives in one AZ and supports hundreds of thousands of requests per second. See [s3.md](aws/aws-services/aws-general-services/s3.md).

**Discovery call (AI)**: A structured elicitation with a stakeholder: listen to the business goal, translate it into requirements, assumptions and constraints, and write them down before the design starts. See [stakeholder-discovery.md](ai/ai-engineering/stakeholder-discovery.md).

**DLQ**: Dead-letter queue. Holds messages that failed processing too many times, so they don't block the queue. See [sqs.md](aws/aws-services/aws-application-coordination/sqs.md).

**DPU**: Data processing unit. The capacity and billing unit of Glue jobs. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**DQDL**: Data Quality Definition Language. The language Glue Data Quality rules are written in. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**Driver (Spark)**: The process that turns a Spark job's code into a plan and hands the work out to executors. See [apache-spark.md](data-engineering/apache-spark.md).

**Dynamic allocation**: A Spark setting that adds executors when tasks queue up and releases idle ones. See [apache-spark.md](data-engineering/apache-spark.md).

**DynamicFrame**: The Glue ETL library's data structure for messy data, where the same field can be inconsistent across a dataset. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**Embedding**: Text converted to a mathematical vector by an embedding model. Semantic search compares a query's embedding to every chunk's embedding. See [core-concepts.md](ai/core-concepts.md).

**EMR managed scaling**: Resizing an EMR on EC2 cluster to its workload, within limits you set. See [emr.md](aws/aws-services/aws-analytics/emr.md).

**Entity resolution**: Matching records that refer to the same real-world entity, such as one customer under different IDs in different systems. See [unified-customer-data.md](data-engineering/unified-customer-data.md).
_Avoid:_ record linkage, identity resolution

**Envelope encryption**: KMS encrypts a small data key, and the data key encrypts the data. See [kms.md](aws/aws-services/aws-security/kms.md).

**ETL**: Extract, transform, load. Get data from sources, make it useful, and serve it to stakeholders. See [data-engineer-role.md](data-engineering/data-engineer-role.md).

**Eval**: A check of a generative system's output against defined criteria. Needed because sampling makes the same prompt return different wording, so exact-text tests are unreliable. Built from the design document's success criteria. See [hill-climb-lifecycle.md](ai/ai-engineering/evals/hill-climb-lifecycle.md), [design-document.md](ai/ai-engineering/design-document.md) and [evaluation-plan.md](ai/ai-engineering/evals/evaluation-plan.md).

**Evaluation plan**: A structured document that translates organizational KPIs into system goals, target metrics and evaluation tasks, and serves as the interface between stakeholders and engineers. See [evaluation-plan.md](ai/ai-engineering/evals/evaluation-plan.md).

**Evaluator-optimizer**: A workflow pattern where one LLM generates a response and another evaluates it and gives feedback, in a loop. See [agent-orchestration.md](ai/ai-engineering/agent-orchestration.md).
_Avoid:_ feedback loop

**Executor (Spark)**: A worker process that runs a Spark job's work on its partitions of the data. See [apache-spark.md](data-engineering/apache-spark.md).

**Exemplar**: An example of how the answer should look, included in a prompt. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).

**Extended thinking**: The Claude setting that makes the model write out its step-by-step reasoning before the answer, returned as a thinking block. Thinking tokens cost the same as output tokens. See [claude-api-foundations.md](ai/ai-engineering/claude-api-foundations.md).

**Fan-out**: Delivering one message to many consumers, often SNS to several SQS queues. See [orchestration-and-automation.md](data-engineering/orchestration-and-automation.md).

**Federated query**: Querying an external database in place from Athena or Redshift, without loading it. See [athena.md](aws/aws-services/aws-analytics/athena.md).

**Few-shot prompting**: Including several examples, typically two to five, in a prompt to show the desired format and behavior. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).

**Fine-tuning**: Adjusting a model's parameters with your own training data to improve performance for domain-specific tasks. See [core-concepts.md](ai/core-concepts.md).

**FM**: Foundation model. A large deep learning neural network trained on massive datasets, used as the starting point for new applications and adapted to specific needs. See [core-concepts.md](ai/core-concepts.md).

**Full CDC**: CDC that captures updates and deletes as well as inserts. See [replicating-databases-to-the-lake.md](data-engineering/replicating-databases-to-the-lake.md).

**Full load**: Copying every row of a database's tables once, usually before CDC takes over. See [replicating-databases-to-the-lake.md](data-engineering/replicating-databases-to-the-lake.md).

**Glue auto scaling**: Adding and removing a Glue job's workers during a run, up to a maximum you set. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**Golden data (evaluation)**: Historical examples, such as refunds and returns handled by human support agents, used to find edge cases and to build a data simulator. Not the same as a golden record. See [hill-climb-lifecycle.md](ai/ai-engineering/evals/hill-climb-lifecycle.md).

**Golden record**: The single trusted, merged record for one entity, built by matching and survivorship rules. See [unified-customer-data.md](data-engineering/unified-customer-data.md).
_Avoid:_ customer 360, single customer view

**GTM**: Go-to-market. The plan for taking a solution to its users: launch, adoption and rollout. It is the third part of the Claude Certified Architect course section "Stakeholder Engagement, Lifecycle & GTM", whose discovery lesson is in [stakeholder-discovery.md](ai/ai-engineering/stakeholder-discovery.md).

**Hill climbing**: Improving a generative system step by step against measurable metrics: change the system, re-run the evaluation suite and keep the changes that raise the scores. See [hill-climb-lifecycle.md](ai/ai-engineering/evals/hill-climb-lifecycle.md).

**Human-in-the-loop (HITL)**: A design where a human confirms or intervenes before the system's output takes effect, such as a support rep confirming a chatbot's refund before it is issued. For agents, a checkpoint goes before a destructive tool call, after a planning step, or on unexpected tool output: see [agent-orchestration.md](ai/ai-engineering/agent-orchestration.md), [hill-climb-lifecycle.md](ai/ai-engineering/evals/hill-climb-lifecycle.md) and [stakeholder-discovery.md](ai/ai-engineering/stakeholder-discovery.md).

**Hybrid search**: Retrieval that combines several relevance signals, such as keyword (BM25) and semantic search, into one ranking. See [core-concepts.md](ai/core-concepts.md).

**Incremental crawl**: A crawler run that scans only new subfolders and adds only the new partitions. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**Insert-only CDC**: CDC for append-only data, such as logs, where rows are only added. See [replicating-databases-to-the-lake.md](data-engineering/replicating-databases-to-the-lake.md).

**Interactive session (Glue)**: On-demand interactive access to a remote Spark runtime, from a notebook or IDE. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**Job bookmark**: Glue's record of data a job already processed, so each run handles only new data. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**KPI**: Key performance indicator. An organizational goal measure, such as auto-resolving 30% of return requests within 2 hours, as opposed to a model metric. See [evaluation-plan.md](ai/ai-engineering/evals/evaluation-plan.md).

**Lake house**: A lake and a warehouse used together: the lake holds everything, and the warehouse serves the curated, high-performance part and can query the lake in place. See [data-lakes-and-warehouses.md](data-engineering/data-lakes-and-warehouses.md).

**Landing zone (data lake)**: An optional first zone for sensitive data such as PII, where it is masked before moving into the raw zone. Not the same as a Control Tower landing zone. See [data-lake-zones.md](data-engineering/data-lake-zones.md).

**Lazy evaluation**: Spark transformations only build a plan; nothing runs until an action, such as writing output. See [apache-spark.md](data-engineering/apache-spark.md).

**Least privilege**: Granting only the permissions a role needs. See [iam.md](aws/aws-services/aws-identity/iam.md).

**LLM judge**: A second model call that grades an output against a rubric, asked for strengths, weaknesses and reasoning alongside the score so scores don't drift toward a safe middle number. Also called an autorater. See [rubrics-and-llm-judge.md](ai/ai-engineering/evals/rubrics-and-llm-judge.md).
_Avoid:_ LLM-as-a-judge

**MCP**: Model Context Protocol. A standard in which a server supplies ready-made tool definitions to an application, so you don't write and maintain each schema and execution function yourself. Runs over stdio (local) or Streamable HTTP (remote). See [tool-use.md](ai/ai-engineering/tool-use.md).

**MDM**: Master data management. The ongoing practice of keeping one trusted version of core entities, such as customers or products, across systems. See [unified-customer-data.md](data-engineering/unified-customer-data.md).

**Memory scope (agent)**: The design choice of what state survives once an agent's loop ends: in-context, external storage, summarized memory or none (stateless). See [agent-orchestration.md](ai/ai-engineering/agent-orchestration.md).

**Message Batches API**: Claude's API for bulk offline work: submit many requests in one call, get an identifier and poll for completion. Takes up to 24 hours, at a lower per-token cost. See [claude-api-foundations.md](ai/ai-engineering/claude-api-foundations.md).

**message_stop**: The streaming event that marks a streamed Claude turn as complete. Until it arrives, the accumulated message is provisional and a partial turn is discarded, not saved. See [claude-api-foundations.md](ai/ai-engineering/claude-api-foundations.md).

**Messages API**: Claude's core API, where your own code runs the agent loop: send the request, read the tool-use blocks, execute the tools and append the results. See [agent-orchestration.md](ai/ai-engineering/agent-orchestration.md).

**Micro-batch**: Ingesting data in small, frequent batches, between batch and streaming. See [batch-and-streaming.md](data-engineering/batch-and-streaming.md).

**Model chaining**: The AWS course's name for workflows: connecting models or services in fixed, predetermined steps. See [ai-orchestration-on-aws.md](aws/aws-ai-engineering/ai-orchestration-on-aws.md).

**Model-based evaluation**: Using an AI model to evaluate another model's outputs. See [genai-poc.md](ai/ai-engineering/genai-poc.md). A calibrated LLM judge is one way to do it.

**MPP**: Massively parallel processing. Spreading a query's work across many nodes, as Redshift does. See [data-lakes-and-warehouses.md](data-engineering/data-lakes-and-warehouses.md).

**MTTD / MTTR**: Mean time to detection and mean time to recovery. See [data-discovery.md](data-engineering/data-discovery.md).

**OLAP**: Online analytical processing. Large scans and aggregations for analytics, on columnar storage. See [data-lakes-and-warehouses.md](data-engineering/data-lakes-and-warehouses.md).

**OLTP**: Online transaction processing. Many small reads and writes for an application, on row-based storage. See [data-lakes-and-warehouses.md](data-engineering/data-lakes-and-warehouses.md).

**One-shot prompting**: Including a single example in a prompt to set the pattern the model follows. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).

**Ongoing replication**: The DMS phase that applies changes from the source's transaction log to the target in near real time. See [dms.md](aws/aws-services/aws-databases/dms.md).

**Open table format**: An open-source library, such as Apache Iceberg, Apache Hudi or Delta Lake, that organizes a data lake's files into tables with database-like functionality: record updates and deletes, consistent concurrent reads and writes, safe failed writes, and schema evolution. See [open-table-formats.md](data-engineering/open-table-formats.md).

**Orchestration**: Coordinating multiple services and their dependencies through a series of steps. See [orchestration-and-automation.md](data-engineering/orchestration-and-automation.md).

**Orchestrator-workers**: A workflow pattern where a central LLM breaks a task down at run time, delegates the pieces to worker LLMs and synthesizes their results. See [agent-orchestration.md](ai/ai-engineering/agent-orchestration.md).

**Parallelization**: A workflow pattern where several LLM calls run at once and code aggregates their outputs, by sectioning or voting. See [agent-orchestration.md](ai/ai-engineering/agent-orchestration.md).
_Avoid:_ parallel processing

**Partition (table)**: One combination of partition-key values of a lake table, stored under its own path, such as `year=2024/month=3/day=13/`. See [partitioning.md](data-engineering/partitioning.md).

**Partition key (stream)**: A producer-chosen value that decides which shard or partition a stream record goes to, keeping one key's records in order. See [batch-and-streaming.md](data-engineering/batch-and-streaming.md).

**Partition key (table)**: A column a lake table is partitioned by, such as `year` or `day`. Queries that filter on it skip the other partitions. See [partitioning.md](data-engineering/partitioning.md).

**PII**: Personally identifiable information. See [macie.md](aws/aws-services/aws-security/macie.md).

**PoC**: Proof of concept. A time-boxed build, typically 2 to 8 weeks, that validates technical feasibility, measures performance and demonstrates business value before full-scale deployment. See [genai-poc.md](ai/ai-engineering/genai-poc.md).

**Prompt caching**: A Claude API feature that stores the processing of a stable request prefix (a long system prompt, a large tool set, a reference document), so later requests with identical content up to that point pay a fraction of the cost. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).

**Prompt chaining**: A workflow pattern where each LLM call processes the previous call's output, in a fixed sequence. See [agent-orchestration.md](ai/ai-engineering/agent-orchestration.md).
_Avoid:_ sequential chaining

**Pruning (context)**: Jumping back to an earlier message and continuing from there, removing the conversation that came after. Used after an unproductive path. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).

**Pub/sub**: Publish/subscribe. Publishers send to a topic, and every subscriber gets a copy. See [orchestration-and-automation.md](data-engineering/orchestration-and-automation.md).

**PySpark**: Spark's Python API. See [apache-spark.md](data-engineering/apache-spark.md).

**Query rewriter**: An agent that turns the user query into a semantic query for embedding search and a list of keywords for BM25. See [core-concepts.md](ai/core-concepts.md).

**RAG**: Retrieval-augmented generation. Connecting a foundation model to external knowledge sources and retrieving relevant information to ground its responses. See [core-concepts.md](ai/core-concepts.md).

**Ragged edge**: The way a generative model's capabilities don't scale uniformly: getting better at one task doesn't guarantee it gets better at closely related ones. See [hill-climb-lifecycle.md](ai/ai-engineering/evals/hill-climb-lifecycle.md).

**Raw zone**: The data lake zone that holds data as ingested, in its original format, kept for auditing and reprocessing. See [data-lake-zones.md](data-engineering/data-lake-zones.md).

**Read replica**: A second, live RDS database kept in sync with the primary, for spreading read traffic or failover. Not a copy in the lake. See [choosing-ingestion-services.md](aws/aws-data-engineering/choosing-ingestion-services.md).

**Readability modeling**: Telling a model how simple or complex its answer should be, as opposed to structured output, which controls the format. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).

**Reasoning mode**: A per-request setting for whether Claude reasons before answering. Worth the cost on hard multi-step problems, wasted on lookups and classification. Separate from model choice. Extended thinking turns it on. See [claude-api-foundations.md](ai/ai-engineering/claude-api-foundations.md).

**Replication instance**: The managed server that runs DMS tasks, reading from a source endpoint and writing to a target endpoint. See [dms.md](aws/aws-services/aws-databases/dms.md).

**Reranking**: Passing a larger set of search results, such as 30 chunks, to a reranking model that returns only the truly relevant ones. See [core-concepts.md](ai/core-concepts.md).

**Reverse ETL**: Pushing cleaned data back into operational tools, such as a CRM. See [data-engineer-role.md](data-engineering/data-engineer-role.md).

**Routing**: A workflow pattern where the input is classified and sent to a specialized follow-up task. See [agent-orchestration.md](ai/ai-engineering/agent-orchestration.md).
_Avoid:_ conditional branching

**RPU**: Redshift Processing Unit. The capacity unit of Redshift Serverless. See [redshift.md](aws/aws-services/aws-analytics/redshift.md).

**RRF**: Reciprocal rank fusion. Fusing the rankings of keyword and semantic search by scoring each chunk with the sum of `1 / (k + rank)` over the rankings it appears in. See [core-concepts.md](ai/core-concepts.md).

**Rubric**: A set of guidelines that defines a high-quality output when many valid outputs exist, used to evaluate subjective, open-ended output. Fixed or adaptive. See [rubrics-and-llm-judge.md](ai/ai-engineering/evals/rubrics-and-llm-judge.md).

**S3 Express One Zone**: The single-AZ S3 storage class with the lowest latency, for the most frequently accessed data. See [s3.md](aws/aws-services/aws-general-services/s3.md).

**SCD2**: Slowly changing dimension, type 2. A history table with one row per version of a record and `valid_from` / `valid_to` columns, so you can query any past state. See [replicating-databases-to-the-lake.md](data-engineering/replicating-databases-to-the-lake.md).
_Avoid:_ SCD type 2

**Sampling**: How an LLM picks each next token, which makes generation non-deterministic: the same prompt can return different wording each run, so exact-text tests are unreliable. See [claude-api-foundations.md](ai/ai-engineering/claude-api-foundations.md).

**Schema-on-read / schema-on-write**: Applying structure when data is read (lakes) vs defining it before loading (warehouses, databases). See [data-lakes-and-warehouses.md](data-engineering/data-lakes-and-warehouses.md).

**Sectioning**: The parallelization variant that splits a task into independent subtasks run in parallel. See [agent-orchestration.md](ai/ai-engineering/agent-orchestration.md).

**SerDe**: Serializer/deserializer. The library a table's storage descriptor names for reading and writing its file format. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**Serverless**: Building and running applications without managing infrastructure, paying only while code runs. See [orchestration-and-automation.md](data-engineering/orchestration-and-automation.md).

**Session (agent)**: The entire multi-turn conversation between a user and an agent, which can contain several traces. See [hill-climb-lifecycle.md](ai/ai-engineering/evals/hill-climb-lifecycle.md).

**Shard**: An ordered unit of a Kinesis stream, with about 1 MB/s in and 2 MB/s out. See [kinesis-data-streams.md](aws/aws-services/aws-analytics/kinesis-data-streams.md).

**Shuffle**: Redistributing rows across Spark executors by key, for a join or group by. The expensive part of a job. See [apache-spark.md](data-engineering/apache-spark.md).

**Site-to-Site VPN**: An encrypted tunnel over the public internet between an on-premises network and AWS. See [site-to-site-vpn.md](aws/aws-services/aws-networking/site-to-site-vpn.md).

**Source endpoint**: The DMS connection to the data store it migrates from. See [dms.md](aws/aws-services/aws-databases/dms.md).

**Span**: A single timed step in an agent trace, such as a model call or a tool call. See [hill-climb-lifecycle.md](ai/ai-engineering/evals/hill-climb-lifecycle.md).

**Spectrum**: Redshift Spectrum, which queries files in S3 from Redshift without loading them. See [redshift.md](aws/aws-services/aws-analytics/redshift.md).

**Spark UI**: The web interface that shows a Spark job's stages, tasks and shuffles, used to find bottlenecks. See [apache-spark.md](data-engineering/apache-spark.md).

**State machine**: A Step Functions workflow made of states such as task, choice, parallel, wait and map. See [step-functions.md](aws/aws-services/aws-application-coordination/step-functions.md).

**stdio (MCP)**: The MCP transport for local servers: the application spawns the server as a subprocess and talks to it over standard input and output. See [tool-use.md](ai/ai-engineering/tool-use.md).

**Storage descriptor**: The part of a Data Catalog table that defines its physical storage: format, S3 location, SerDe and schema. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**Stream**: A continuous, ordered sequence of small records, appended as events happen and kept for a retention period. See [batch-and-streaming.md](data-engineering/batch-and-streaming.md).

**Streamable HTTP**: The MCP transport for remote servers: POST carries client-to-server messages, and an optional GET-based SSE stream carries server-initiated ones. It replaces the deprecated SSE-only transport. See [tool-use.md](ai/ai-engineering/tool-use.md).

**Streaming (LLM)**: Sending a model's response in pieces as it is generated, over the same HTTP connection using server-sent events, so output appears immediately. See [claude-api-foundations.md](ai/ai-engineering/claude-api-foundations.md).

**Structured / semi-structured / unstructured data**: Data in fixed tables, data with flexible structure (JSON, logs), and data with no data model (documents, images, audio, video). See [data-discovery.md](data-engineering/data-discovery.md).

**Structured outputs**: A Claude API mode that constrains the response to a schema. It adds first-request latency and input tokens, can still return non-matching output on a refusal or truncation, and can't be combined with prefilling. See [claude-api-foundations.md](ai/ai-engineering/claude-api-foundations.md).

**Subagent handoff**: Spawning a subagent in its own isolated context window with only the task description it needs, and getting back a summary. Keeps exploration out of the main context. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).

**Survivorship**: The rules that decide which source wins for each field when records are merged into a golden record. See [unified-customer-data.md](data-engineering/unified-customer-data.md).

**Target endpoint**: The DMS connection to the data store it migrates to. See [dms.md](aws/aws-services/aws-databases/dms.md).

**TCO**: Total cost of ownership. Inference, infrastructure, development time and ongoing maintenance, compared against the current process. See [genai-poc.md](ai/ai-engineering/genai-poc.md).

**Thinking block**: The response block that holds Claude's reasoning under extended thinking, placed just ahead of the answer block and carrying a signature. See [claude-api-foundations.md](ai/ai-engineering/claude-api-foundations.md).

**Time travel**: Querying a table as it was at a past snapshot, a feature of open table formats such as Iceberg. See [open-table-formats.md](data-engineering/open-table-formats.md).

**Time-series similarity**: Retrieval that matches sensor readings to past readings with a similar shape, such as vibration patterns that preceded a failure. See [ai-orchestration-on-aws.md](aws/aws-ai-engineering/ai-orchestration-on-aws.md).

**Token**: The unit an LLM reads and writes, and what the API meters for input, output and cost. The context window is measured in tokens. See [claude-api-foundations.md](ai/ai-engineering/claude-api-foundations.md).

**Token counting**: The Claude API's `count_tokens` endpoint, which returns a request's token count without running inference, to check a context budget or gate oversized requests. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).

**Tokenization**: Replacing a sensitive value with a random token, with the real value kept in a separate, secured store, so authorized systems can reverse it. Unlike masking, which can't be reversed. See [troubleshooting-data-lakes.md](data-engineering/troubleshooting-data-lakes.md).

**Trace (agent)**: A factual, immutable record of one agent invocation (a single turn): the model inputs, responses and tool calls, in order, built from spans. See [hill-climb-lifecycle.md](ai/ai-engineering/evals/hill-climb-lifecycle.md).

**Transactional data lake**: A data lake whose tables use an open table format, so they support transactions, record updates and deletes. See [open-table-formats.md](data-engineering/open-table-formats.md).

**Translation table**: The output of a discovery call: one row per item, holding the stakeholder statement, the constraint it implies, the architectural decision it forces, and the assumption to document. See [stakeholder-discovery.md](ai/ai-engineering/stakeholder-discovery.md).

**Trust boundary**: The line between inputs someone else can write (untrusted) and what the system is allowed to do, set in the design document as the smallest actions and access the feature needs. See [design-document.md](ai/ai-engineering/design-document.md).

**User simulation**: Directing an AI to impersonate a user and running it against the real agent under evaluation, to generate multi-turn test data. See [evaluation-plan.md](ai/ai-engineering/evals/evaluation-plan.md).

**Vibe testing**: Exploratory, informal review of a prototype's output to observe early behavior, before formal rubrics and metrics exist. See [evaluation-plan.md](ai/ai-engineering/evals/evaluation-plan.md).

**Virtual private gateway**: The AWS end of a Site-to-Site VPN, attached to a VPC. See [site-to-site-vpn.md](aws/aws-services/aws-networking/site-to-site-vpn.md).
_Avoid:_ VPN gateway

**Visibility timeout**: How long an SQS message stays hidden from other consumers while one processes it. See [sqs.md](aws/aws-services/aws-application-coordination/sqs.md).

**Visual ETL**: Building an ETL job by drag and drop, without code: sources, transforms, targets. See [glue.md](aws/aws-services/aws-analytics/glue.md).

**Voting**: The parallelization variant that runs the same task several times to get diverse outputs. See [agent-orchestration.md](ai/ai-engineering/agent-orchestration.md).

**VPC endpoint**: Private access from a VPC to AWS services such as S3, Glue or KMS without the internet. See [vpc.md](aws/aws-services/aws-networking/vpc.md).

**Workflow (AI)**: An agentic system where code orchestrates LLMs and tools through predefined steps; the code, not the LLM, is in control. See [agent-orchestration.md](ai/ai-engineering/agent-orchestration.md).
_Avoid:_ model chaining

**Zero-ETL**: Querying or replicating data without building ETL pipelines. See [orchestration-and-automation.md](data-engineering/orchestration-and-automation.md).

**Zero-shot prompting**: A prompt with no examples, relying only on the model's pre-trained knowledge. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).

## Service names

**Amazon Data Firehose**: Managed delivery of streaming data to S3, Redshift, OpenSearch and more. See [data-firehose.md](aws/aws-services/aws-analytics/data-firehose.md).
_Avoid:_ Kinesis Data Firehose

**Amazon Managed Service for Apache Flink**: Real-time stream processing. See [managed-service-for-apache-flink.md](aws/aws-services/aws-analytics/managed-service-for-apache-flink.md).
_Avoid:_ Kinesis Data Analytics

**Amazon OpenSearch Service**: Managed search and log analytics. See [opensearch-service.md](aws/aws-services/aws-databases/opensearch-service.md).
_Avoid:_ Amazon Elasticsearch Service

**Amazon QuickSight**: BI dashboards, sold under the Amazon Quick Suite branding. See [quicksight.md](aws/aws-services/aws-analytics/quicksight.md).
_Avoid:_ Quick Suite (when meaning the BI service)

**Amazon SageMaker AI**: The ML build, train and deploy service; "SageMaker" alone is the broader data, analytics and AI platform. See [sagemaker.md](aws/aws-services/aws-ai/sagemaker.md).

**Control Tower control**: A preventive or detective rule in a Control Tower landing zone. See [control-tower.md](aws/aws-services/aws-security/control-tower.md).
_Avoid:_ guardrail

**DataSync**: AWS DataSync. See [datasync.md](aws/aws-services/aws-migration-and-transfer/datasync.md).

**DMS**: AWS Database Migration Service. See [dms.md](aws/aws-services/aws-databases/dms.md).

**KDS**: Amazon Kinesis Data Streams. See [kinesis-data-streams.md](aws/aws-services/aws-analytics/kinesis-data-streams.md).

**MSK**: Amazon Managed Streaming for Apache Kafka. See [msk.md](aws/aws-services/aws-analytics/msk.md).

**MWAA**: Amazon Managed Workflows for Apache Airflow. See [mwaa.md](aws/aws-services/aws-application-coordination/mwaa.md).
