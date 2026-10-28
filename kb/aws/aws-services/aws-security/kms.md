# AWS Key Management Service (KMS)

This file covers KMS: encryption keys, key types, envelope encryption, and how it protects pipeline data at rest.

## What it is

KMS lets you **create and control encryption keys** and **encrypts and decrypts data** using **customer managed** or **AWS managed keys**. It is a security service used across every stage of the pipeline, and part of **sensitive data protection**, one of the five security areas.

## Characteristics

- **Course correction:** the course says KMS protects data "at rest and in transit". KMS is for **data at rest** (S3, EBS, RDS, Redshift encryption). Data **in transit** is protected by **HTTPS/TLS**, with certificates from [ACM](../aws-apis/acm.md), as the course's own best-practices section says. KMS is involved in transit mostly when an app encrypts data itself before sending it.
- **AWS managed keys:** created automatically by a service (for example, `aws/s3`). No control over the policy or rotation.
- **Customer managed keys:** you control the **key policy**, rotation, disabling and deletion, and get a [CloudTrail](../aws-monitoring/cloudtrail.md) record of every use.
- **Envelope encryption:** KMS encrypts a small data key; the data key encrypts the data. Large data never leaves for KMS.
- Integrated with S3, Redshift, Glue, Kinesis, EBS, RDS, DynamoDB and more.
- [Glue](../aws-analytics/glue.md) security configurations use KMS to encrypt job output, CloudWatch logs, job bookmarks, the Data Catalog and connection passwords.
- Best practice: **encrypt data at rest and in transit**: KMS at rest, HTTPS/TLS in transit.

## Example

The `curated/finance/` bucket uses a customer managed key. Its key policy allows decryption only by the finance analyst role and the Glue job role. Even an admin with full S3 access can download the objects but can't read them without permission on the key.

Default bucket encryption with a customer managed key, plus a bucket policy that denies non-HTTPS requests.

## Related

- [choosing-security-and-monitoring-services.md](../../aws-data-engineering/choosing-security-and-monitoring-services.md): compares KMS with ACM (keys for data at rest vs certificates for data in transit), and with CloudHSM and Secrets Manager (managed keys vs dedicated hardware vs stored passwords).
- [exam-traps.md](../../aws-data-engineering/exam-traps.md): course correction: the course says KMS encrypts data at rest and in transit, but KMS protects data at rest; in transit is TLS with ACM.
- [security-and-monitoring-on-aws.md](../../aws-data-engineering/security-and-monitoring-on-aws.md): KMS is a course service for sensitive data protection, and implements the "encrypt data at rest" best practice.
- [data-security-and-monitoring.md](../../../data-engineering/data-security-and-monitoring.md): KMS implements encryption at rest, part of sensitive data protection and of the "encrypt data at rest and in transit" best practice.
- [acm.md](../aws-apis/acm.md): ACM covers the half KMS doesn't: TLS certificates for encryption in transit.
- [cloudtrail.md](../aws-monitoring/cloudtrail.md): every use of a customer managed key is recorded in CloudTrail.
- [glue.md](../aws-analytics/glue.md): Glue security configurations use KMS to encrypt job output, logs, job bookmarks, the Data Catalog and connection passwords.
- [s3.md](../aws-general-services/s3.md): S3 buckets use KMS keys for default encryption; with a customer managed key, the key policy decides who can read objects even if they can download them.
- [iam.md](../aws-identity/iam.md): a job's IAM role needs `kms:Decrypt` on a bucket's key to read encrypted data, in addition to the key policy allowing it.
