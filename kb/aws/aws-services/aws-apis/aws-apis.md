# aws-apis — index

Exposing APIs and serving them securely over HTTPS.

## How to read this folder

- **Before:** [lambda.md](../aws-compute/lambda.md), which API Gateway usually calls.
- **After:** [waf.md](../aws-security/waf.md).

## Files (in reading order)

- [api-gateway.md](api-gateway.md): Amazon API Gateway: REST, HTTP and WebSocket APIs in front of Lambda, with auth, throttling and per-request pricing. Read when: you need to expose data or accept submissions through a serverless API.
- [acm.md](acm.md): ACM public and private SSL/TLS certificates and encryption in transit. Read when: you need how an endpoint serves HTTPS, or where encryption in transit comes from.
