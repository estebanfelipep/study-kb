# Amazon API Gateway

This file covers Amazon API Gateway: serverless REST, HTTP and WebSocket APIs in front of Lambda, with an example.

## What it is

API Gateway creates **RESTful and HTTP APIs** that integrate with Lambda functions. With it you can build serverless applications where the **business logic runs in Lambda**. In data engineering, it's a way to expose data, such as metrics, to other teams, or to accept data submitted by partners.

## Characteristics

- **API types** _(added)_:
  - **REST APIs:** more features, such as API keys, usage plans, per-client throttling, request validation and caching.
  - **HTTP APIs:** simpler, cheaper and lower latency. Use them when you don't need the REST-only features.
  - **WebSocket APIs:** two-way, real-time connections, for example chat or live dashboards.
- Handles authentication (IAM, Cognito, Lambda authorizers), throttling and scaling for you _(added)_.
- You pay per request, and it costs nothing when nobody calls it _(added)_.
- Works with [AWS WAF](../aws-security/waf.md) to block web attacks, and with [ACM](acm.md) certificates for HTTPS _(added)_.

## Example

_(added)_ A data team exposes a **metrics API** to other internal teams. A request to `GET /metrics/daily-active-users?date=2026-10-17` goes to API Gateway. API Gateway invokes a Lambda function, which reads the precomputed value from DynamoDB and returns JSON. A rate limit of 100 requests per second per API key keeps one runaway client from overloading the backend.

## Related

- [lambda.md](../aws-compute/lambda.md): API Gateway invokes a Lambda function for each request, and the function runs the API's business logic.
- [dynamodb.md](../aws-databases/dynamodb.md): in the metrics API example, the Lambda behind API Gateway reads the precomputed value from DynamoDB.
- [waf.md](../aws-security/waf.md): WAF sits in front of API Gateway and blocks web attacks such as SQL injection, plus request floods.
- [acm.md](acm.md): ACM provides the certificate that lets an API Gateway endpoint serve HTTPS.
- [choosing-orchestration-services.md](../../aws-data-engineering/choosing-orchestration-services.md): compares API Gateway with an Application Load Balancer: API Gateway has API features (keys, throttling, validation) and per-request pricing for public or partner APIs; ALB is simpler and cheaper at high steady traffic for web apps.
- [zero-etl-and-serverless-on-aws.md](../../aws-data-engineering/zero-etl-and-serverless-on-aws.md): API Gateway is the "expose APIs" role in the serverless services list, the alternative to ALB + EC2.
- [security-and-monitoring-on-aws.md](../../aws-data-engineering/security-and-monitoring-on-aws.md): the secured pipeline example starts with partners sending data to API Gateway over HTTPS, protected by WAF and Shield.
