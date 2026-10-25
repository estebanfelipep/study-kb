# aws-general-services — index

Services that belong to two or more categories, such as S3, which is both web storage and the data lake.

## How to read this folder

- **Before:** Read [data-lakes-and-warehouses.md](../../../data-engineering/data-lakes-and-warehouses.md) for what a data lake is.
- **Order:** Read S3 before any other service file, since most of them read from or write to it.
- **After:** the other foundations, [aws-identity](../aws-identity/aws-identity.md) and [aws-networking](../aws-networking/aws-networking.md).

## Files

- [s3.md](s3.md): Amazon S3 object storage: buckets, objects, keys, use cases, storage classes, security, performance, event notifications, static websites, and its role as the data lake. Read when: you need how S3 works, its limits or storage classes, or why the lake is built on it.
