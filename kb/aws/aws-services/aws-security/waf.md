# AWS WAF (Web Application Firewall)

This file covers AWS WAF: layer 7 protection for web applications and APIs.

## What it is

AWS WAF protects **web applications** from **common exploits and attacks** and protects **application availability**. The course lists it under **data and network security**.

## Characteristics

- Works at **layer 7** (HTTP/HTTPS) on **CloudFront, ALB, API Gateway, AppSync and Cognito**.
- Rules block **SQL injection, cross-site scripting**, bad IPs and countries, and **rate-limit** requests per IP.
- **Managed rule groups** from AWS and vendors give protection without writing rules.
- Pay per rule and request.
- [Shield](shield.md) Advanced uses WAF for layer 7 DDoS protection.

## Example

A public [API Gateway](../aws-apis/api-gateway.md) endpoint lets partners submit data. WAF blocks requests containing SQL injection patterns and limits each IP to 1,000 requests per 5 minutes, so one bad client can't flood the ingestion [Lambda](../aws-compute/lambda.md).

## Related

- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares WAF with Shield, security groups and Network Firewall: WAF filters HTTP content at layer 7, Shield absorbs DDoS, security groups and NACLs filter IPs and ports at layers 3–4.
- [security-and-monitoring-on-aws.md](../../aws-data-engineering/security-and-monitoring-on-aws.md): WAF is a course service for data and network security, and protects the API Gateway entry point in the example secured pipeline.
- [shield.md](shield.md): Shield Advanced uses WAF for layer 7 DDoS protection.
- [api-gateway.md](../aws-apis/api-gateway.md): WAF attaches to API Gateway to block SQL injection and rate-limit each IP, so one bad client can't flood the ingestion Lambda.
- [vpc.md](../aws-networking/vpc.md): security groups and network ACLs filter by IP and port inside a VPC, while WAF inspects HTTP content in front of the application.
