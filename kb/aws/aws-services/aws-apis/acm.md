# AWS Certificate Manager (ACM)

This file covers ACM: SSL/TLS certificates and encryption in transit for pipeline endpoints.

## What it is

ACM provisions, manages and deploys **SSL/TLS certificates** for AWS services and applications. The course lists it under **access management**. It is what makes **encryption in transit** (HTTPS/TLS) work for your own endpoints _(added)_.

## Characteristics

- **Public certificates are free** when used with integrated services (ALB, CloudFront, API Gateway) and **renew automatically** _(added)_.
- **Private certificates** come from **AWS Private CA** (paid) for internal services _(added)_.
- Manages certificates (public/private key pairs tied to a domain), not encryption keys for stored data; that's [KMS](../aws-security/kms.md) _(added)_.

## Example

_(added)_ A data API behind [API Gateway](api-gateway.md) serves `https://data.example.com`. ACM issues the certificate and renews it every year without anyone touching it, so clients' connections stay encrypted and no certificate ever expires in production.

## Related

- [kms.md](../aws-security/kms.md): the two split encryption. ACM certificates protect data in transit (TLS); KMS keys protect data at rest.
- [api-gateway.md](api-gateway.md): API Gateway serves HTTPS endpoints with ACM certificates, which ACM renews automatically.
- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares ACM with KMS: ACM manages certificates for HTTPS, KMS manages encryption keys for stored data.
- [security-and-monitoring-on-aws.md](../../aws-data-engineering/security-and-monitoring-on-aws.md): ACM is listed under access management, and in the secured pipeline example partners reach API Gateway over HTTPS with an ACM certificate.
