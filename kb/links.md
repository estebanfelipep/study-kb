# Links

This file lists every external link in this KB in one place. Each entry says what the link is and which topic file explains it. When a topic file gains a link, add it here too.

Each entry looks like this:

`- [Title](url): what it is. See [topic.md](path/to/topic.md).`

## Official docs

- [Using Amazon S3 as a target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html): AWS DMS User Guide, S3 target settings. See [dms.md](aws/aws-services/aws-databases/dms.md).
- [AWS DataSync User Guide](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html): the official DataSync guide. See [datasync.md](aws/aws-services/aws-migration-and-transfer/datasync.md).
- [AWS DataSync FAQs](https://aws.amazon.com/datasync/faqs/): DataSync frequently asked questions. See [datasync.md](aws/aws-services/aws-migration-and-transfer/datasync.md).
- [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html): the official S3 guide. See [s3.md](aws/aws-services/aws-general-services/s3.md).
- [Defining S3 bucket and path names for data lake layers on the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/defining-bucket-names-data-lakes/welcome.html): AWS Prescriptive Guidance, naming buckets and paths per zone. See [s3.md](aws/aws-services/aws-general-services/s3.md).
- [Amazon S3 storage classes](https://aws.amazon.com/s3/storage-classes/): the storage classes compared. See [s3.md](aws/aws-services/aws-general-services/s3.md).
- [Optimizing storage costs using Amazon S3](https://aws.amazon.com/s3/cost-optimization/): S3 cost optimization. See [s3.md](aws/aws-services/aws-general-services/s3.md).
- [Managing the lifecycle of objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html): Amazon S3 User Guide, lifecycle rules. See [s3.md](aws/aws-services/aws-general-services/s3.md).
- [Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/userguide/analytics-storage-class.html): Amazon S3 User Guide, analyzing access patterns. See [s3.md](aws/aws-services/aws-general-services/s3.md).
- [Best practices design patterns: optimizing Amazon S3 performance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html): Amazon S3 User Guide, performance. See [s3.md](aws/aws-services/aws-general-services/s3.md).
- [Central storage: Amazon S3 as the data lake storage platform](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/amazon-s3-data-lake-storage-platform.html): AWS whitepaper (Storage Best Practices for Data and Analytics Applications), S3 as the lake's storage. See [s3.md](aws/aws-services/aws-general-services/s3.md).
- [Data lake foundation](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/data-lake-foundation.html): AWS whitepaper (Storage Best Practices for Data and Analytics Applications), the zones of a data lake. See [data-lake-zones.md](data-engineering/data-lake-zones.md).
- [Cost Modeling Data Lakes for Beginners](https://docs.aws.amazon.com/whitepapers/latest/cost-modeling-data-lakes/welcome.html): AWS whitepaper, including the storage costs of analytics services. See [s3.md](aws/aws-services/aws-general-services/s3.md).
- [What Is a Data Catalog?](https://aws.amazon.com/what-is/data-catalog/): AWS overview of data catalogs and the Glue Data Catalog. See [glue.md](aws/aws-services/aws-analytics/glue.md).
- [Data discovery and cataloging in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html): AWS Glue User Guide, the Data Catalog and crawlers. See [glue.md](aws/aws-services/aws-analytics/glue.md).
- [Optimizing query performance using column statistics](https://docs.aws.amazon.com/glue/latest/dg/column-statistics.html): AWS Glue User Guide, column-level statistics. See [glue.md](aws/aws-services/aws-analytics/glue.md).
- [AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html): AWS Glue User Guide, Data Quality. See [glue.md](aws/aws-services/aws-analytics/glue.md).
- [Using custom connectors and connections with AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/ug/connectors-chapter.html): AWS Glue Studio User Guide, connectors. See [glue.md](aws/aws-services/aws-analytics/glue.md).
- [DynamicFrame class](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-dynamic-frame.html): AWS Glue Developer Guide, DynamicFrame. See [glue.md](aws/aws-services/aws-analytics/glue.md).
- [Data Quality Definition Language (DQDL) reference](https://docs.aws.amazon.com/glue/latest/dg/dqdl.html): AWS Glue Developer Guide, DQDL. See [glue.md](aws/aws-services/aws-analytics/glue.md).
- [Detect and process sensitive data](https://docs.aws.amazon.com/glue/latest/dg/detect-PII.html): AWS Glue Developer Guide, the Detect PII transform. See [glue.md](aws/aws-services/aws-analytics/glue.md).
- [Using the Delta Lake framework in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-delta-lake.html): AWS Glue User Guide, Delta Lake in Glue. See [transactional-data-lake-on-aws.md](aws/aws-data-engineering/transactional-data-lake-on-aws.md).
- [LangChain text splitters](https://docs.langchain.com/oss/javascript/integrations/splitters): LangChain docs, the package for chunking documents. See [core-concepts.md](ai/core-concepts.md).
- [LangChain length-based splitter](https://docs.langchain.com/oss/javascript/integrations/splitters#length-based): LangChain docs, fixed-size chunking. See [core-concepts.md](ai/core-concepts.md).
- [LangChain text-structure-based splitter](https://docs.langchain.com/oss/javascript/integrations/splitters#text-structure-based): LangChain docs, structural chunking. See [core-concepts.md](ai/core-concepts.md).
- [Reciprocal rank fusion (Elasticsearch docs)](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion): Elasticsearch reference, RRF and its `k` constant. See [core-concepts.md](ai/core-concepts.md).
- [Ranking and reranking (Elastic docs)](https://www.elastic.co/docs/solutions/search/ranking): Elastic docs, ranking and reranking search results. See [core-concepts.md](ai/core-concepts.md).

## Courses and training

- [AWS Generative AI Developer Advanced Learning Plan (includes Labs)](https://skillbuilder.aws/learning-plan/BGTH16YCTU/aws-generative-ai-developer-advanced-learning-plan-includes-labs/ZDN46CX881): AWS Skill Builder learning plan for generative AI developers. See [ai-engineering.md](ai/ai-engineering/ai-engineering.md) and [ai-orchestration-on-aws.md](aws/aws-ai-engineering/ai-orchestration-on-aws.md).
- [Claude Certified Developer: Foundations (Anthropic Skilljar)](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations): Anthropic's learning path; the "Foundations" and "Evals and judges" material. See [claude-api-foundations.md](ai/ai-engineering/claude-api-foundations.md) and [design-document-and-llm-judge.md](ai/ai-engineering/design-document-and-llm-judge.md).
- [Stakeholder Engagement, Lifecycle & GTM (Anthropic Skilljar)](https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional/stakeholder-engagement-lifecycle-gtm/486650/scorm/xdrwlkyjtpf): Claude Certified Architect – Professional learning path, the "Stakeholder Engagement, Lifecycle & GTM" section. See [stakeholder-discovery.md](ai/ai-engineering/stakeholder-discovery.md).
- [Chunking intro (AI Hero)](https://www.aihero.dev/workshops/retrieval-skill-building-day-2-u45nl/chunking-intro-2lxwn): AI Hero retrieval workshop lesson, introduction to chunking. See [core-concepts.md](ai/core-concepts.md).
- [Fixed-size chunks (AI Hero)](https://www.aihero.dev/workshops/retrieval-skill-building-day-2-u45nl/fixed-size-chunks-dsxci): AI Hero retrieval workshop lesson, fixed-size chunking. See [core-concepts.md](ai/core-concepts.md).
- [Structural chunking (AI Hero)](https://www.aihero.dev/workshops/retrieval-skill-building-day-2-u45nl/structural-chunking-h4xti): AI Hero retrieval workshop lesson, structural chunking. See [core-concepts.md](ai/core-concepts.md).
- [Overview of the BM25 algorithm (AI Hero)](https://www.aihero.dev/workshops/retrieval-skill-building-kmlhc/overview-of-the-bm-25-algorithm~qrr4a): AI Hero retrieval workshop lesson, BM25. See [core-concepts.md](ai/core-concepts.md).
- [Rank fusion (AI Hero)](https://www.aihero.dev/workshops/retrieval-skill-building-kmlhc/rank-fusion-r3fg2): AI Hero retrieval workshop lesson, reciprocal rank fusion. See [core-concepts.md](ai/core-concepts.md).
- [Reranking (AI Hero)](https://www.aihero.dev/workshops/retrieval-skill-building-day-2-u45nl/reranking-tgdxs): AI Hero retrieval workshop lesson, reranking. See [core-concepts.md](ai/core-concepts.md).

## Practice exams

_None yet._

## Videos and articles

- [Create an AWS Glue Data Catalog with AWS DMS](https://aws.amazon.com/blogs/database/create-an-aws-glue-data-catalog-with-aws-dms/): AWS Database Blog, DMS populating the Glue Data Catalog. See [dms.md](aws/aws-services/aws-databases/dms.md).
- [Understanding Apache Iceberg on AWS with the new technical guide](https://aws.amazon.com/blogs/big-data/understanding-apache-iceberg-on-aws-with-the-new-technical-guide/): AWS Big Data Blog, Iceberg on AWS. See [transactional-data-lake-on-aws.md](aws/aws-data-engineering/transactional-data-lake-on-aws.md).
- [Build your Apache Hudi data lake on AWS using Amazon EMR – Part 1](https://aws.amazon.com/blogs/big-data/part-1-build-your-apache-hudi-data-lake-on-aws-using-amazon-emr/): AWS Big Data Blog, Hudi on EMR. See [transactional-data-lake-on-aws.md](aws/aws-data-engineering/transactional-data-lake-on-aws.md).
- [Okapi BM25 (Wikipedia)](https://en.wikipedia.org/wiki/Okapi_BM25): Wikipedia article on the BM25 ranking function. See [core-concepts.md](ai/core-concepts.md).
- [Clarification loop (YouTube)](https://youtu.be/xc63tFIIfeA?si=4tuG4M-HB6KnE_QO&t=227): video on the clarification loop in RAG. See [core-concepts.md](ai/core-concepts.md).
- [Building effective agents (Anthropic)](https://www.anthropic.com/engineering/building-effective-agents): Anthropic engineering article on workflow types and agents, with examples and use cases. See [agent-orchestration.md](ai/ai-engineering/agent-orchestration.md).
- [What is an agent? (AI Hero)](https://www.aihero.dev/what-is-an-agent): AI Hero article on what makes a system an agent. See [agent-orchestration.md](ai/ai-engineering/agent-orchestration.md).
- [Agents vs workflows (YouTube)](https://www.youtube.com/watch?v=F8NKVhkZZWI): video on agents and workflows. See [agent-orchestration.md](ai/ai-engineering/agent-orchestration.md).
- [How to improve your LLM-powered app (AI Hero)](https://www.aihero.dev/how-to-improve-your-llm-powered-app): AI Hero article on improving an LLM-powered app. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).
- [Prompting Guide](https://www.promptingguide.ai/): guide to prompt engineering techniques. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).
- [Prompt engineering overview (Claude docs)](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview): Anthropic's prompt engineering documentation. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).
- [System prompts (Claude docs)](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/system-prompts): Anthropic's documentation on role-based prompting. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).
- [Prompt library (Claude docs)](https://docs.claude.com/en/resources/prompt-library/library): library of example prompts. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).
- [Write clear instructions (OpenAI)](https://platform.openai.com/docs/guides/prompt-engineering#strategy-write-clear-instructions): OpenAI's prompt engineering guide, the strategy on writing clear instructions. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).
- [Prompting good practices (YouTube)](https://www.youtube.com/watch?v=ysPbXH0LpIE): video on prompting good practices and the structure of a great system prompt. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).
- [The template (AI Hero)](https://www.aihero.dev/workshops/ai-sdk-v5-crash-course/the-template-hmys8): AI SDK v5 crash course lesson on the prompt template. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).
- [Exemplars (AI Hero)](https://www.aihero.dev/workshops/ai-sdk-v5-crash-course/exemplars-n4ry4/solution): AI SDK v5 crash course lesson on exemplars. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).
- [Chain of thought (AI Hero)](https://www.aihero.dev/workshops/ai-sdk-v5-crash-course/chain-of-thought-2y3wd/solution): AI SDK v5 crash course lesson on chain-of-thought. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).
- [How to build production-grade generative AI applications (freeCodeCamp)](https://www.freecodecamp.org/news/how-to-build-production-grade-generative-ai-applications/#heading-qa-for-llm-applications-test-more-than-you-think): article whose QA section shows fixes for common agent malfunctions. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).
- [Long context isn't the answer (HumanLayer)](https://www.humanlayer.dev/blog/long-context-isnt-the-answer): blog post on why a longer context window doesn't solve the problem. See [prompt-and-context-engineering.md](ai/ai-engineering/prompt-and-context-engineering.md).

## Code and repos

- [Structural chunking in action: chunks.ts](https://github.com/estebanfelipep/ai-hero-cohort-002-skill-building/blob/main/exercises/03-retrieval-day-2-skill-building/03.03-structural-chunking/problem/api/chunks.ts): AI Hero cohort exercise, structural chunking code. See [core-concepts.md](ai/core-concepts.md).
- [Retrieval with BM25 exercise](https://github.com/estebanfelipep/poland-vercel-ai-sdk-workshop/tree/main/exercises/08-retrieval/08.1-retrieval-with-bm25/problem): Vercel AI SDK workshop exercise, retrieval with BM25. See [core-concepts.md](ai/core-concepts.md).
- [Rank fusion explainer](https://github.com/estebanfelipep/poland-vercel-ai-sdk-workshop/tree/main/exercises/08-retrieval/08.3-rank-fusion/explainer): Vercel AI SDK workshop explainer, rank fusion. See [core-concepts.md](ai/core-concepts.md).
