# Apache Spark

This file covers Apache Spark: what it's for, how it splits a job across machines, its APIs, how it differs from MapReduce and Flink, and a worked example of a daily batch job from the raw zone to the curated zone.

## What it's for

Spark processes data that is too big for one machine. It's the open-source **distributed processing engine** that most managed ETL and big data services run on. It ingests, processes and integrates data at scale, in **batch and streaming**.

Typical jobs run for minutes to hours on GB to TB of data:

- Cleaning raw data: filtering, deduplicating, fixing types.
- Joining sources, such as events with customers.
- Aggregating, such as revenue per country per day.
- Converting formats, such as JSON or CSV to partitioned Parquet.
- Feature engineering and model training for machine learning.

## How it works

A Spark job has one **driver** and many **executors** (workers):

- The **driver** turns the code into a plan of steps and hands out the work.
- The data is split into **partitions**, chunks that each executor processes in parallel. These are in-memory chunks of work, not the `key=value/` folders of a partitioned lake table.
- Steps that work row by row (filter, select, deduplicate within a chunk) run on each partition independently.
- Steps that need rows with the same key together (join, group by) trigger a **shuffle**: rows are redistributed across executors by key over the network. Shuffles are the expensive part of a job.
- **Lazy evaluation:** transformations only build the plan. Nothing runs until an **action**, such as writing the output or counting rows. That lets Spark optimize the whole plan first.
- Intermediate results stay **in memory** between steps where possible.

```
            Driver: plans the job, hands out work
                            │
         ┌──────────────────┼──────────────────┐
         ▼                  ▼                  ▼
    Executor 1         Executor 2         Executor N
    partition 1        partition 2        partition N
    filter, dedupe     filter, dedupe     filter, dedupe
         │                  │                  │
         └────────── shuffle by key ───────────┘
                            ▼
              join, group by, aggregate
                            ▼
                write output files
```

A bigger input needs more executors, not different code.

## APIs

| API | What it's for |
| --- | --- |
| **DataFrames** | Tables of rows and named columns, the main API for ETL |
| **Spark SQL** | Plain SQL over DataFrames and catalog tables |
| **PySpark** | The Python API. Spark also has Scala, Java and R APIs |
| **Structured Streaming** | The same DataFrame code over a stream, processed as micro-batches |
| **MLlib** | Distributed machine learning |

## Tuning and monitoring

- The **Spark UI** shows a running or finished job's stages, tasks and shuffles, and how long each took. It's where to look first for a slow job: one huge task, a big shuffle, or executors sitting idle.
- **Dynamic allocation** lets Spark request executors when tasks queue up and release idle ones, so an application isn't sized for its peak.
- **Rightsizing:** executors with too little memory fail or spill to disk, and too many sit idle and cost money.

## Spark vs MapReduce vs Flink

| | Hadoop MapReduce | Spark | Flink |
| --- | --- | --- | --- |
| Main use | Batch | Batch, plus streaming | Real-time streaming |
| Between steps | Writes to disk | Keeps data in memory where possible | Streams records through |
| Streaming model | None | Micro-batches | Record by record |
| Pick it when | Legacy Hadoop jobs | General large-scale ETL and analytics | Lowest latency, windowed aggregations on a stream |

Spark replaced MapReduce for most work because keeping data in memory makes multi-step jobs much faster.

## Example: daily revenue from clickstream events

A shop's website writes about 400 GB of JSON events a day to the raw zone, across thousands of files. Analysts want revenue per country per day. That's too much for one machine, and too long for a short-lived function.

**Input, raw zone** (`raw/clickstream/2026-11-06/*.json`):

| event_id | ts | customer_id | event | amount |
| --- | --- | --- | --- | --- |
| e1 | 2026-11-06 09:01 | c42 | view | null |
| e2 | 2026-11-06 09:03 | c42 | purchase | 59.90 |
| e2 | 2026-11-06 09:03 | c42 | purchase | 59.90 |
| e3 | 2026-11-06 10:15 | c07 | purchase | 120.00 |
| e4 | 2026-11-06 10:20 | null | purchase | 15.00 |

The input has a duplicate (e2), a purchase with no customer (e4), and view events that don't count toward revenue.

**The job, in PySpark:**

```python
from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("daily-revenue").getOrCreate()

events = spark.read.json("raw/clickstream/2026-11-06/")
customers = spark.read.parquet("cleaned/customers/")

revenue = (
    events
    .filter(F.col("event") == "purchase")      # keep purchases
    .dropDuplicates(["event_id"])              # drop e2's copy
    .filter(F.col("customer_id").isNotNull())  # drop e4
    .join(customers, "customer_id")            # add country
    .groupBy(F.to_date("ts").alias("day"), "country")
    .agg(F.sum("amount").alias("revenue"),
         F.count("*").alias("orders"))
)

(revenue.write.mode("overwrite")               # the action
    .partitionBy("day")
    .parquet("curated/daily_revenue/"))
```

The filters and deduplication run on each partition independently. The join and the group by trigger shuffles. Nothing runs until `write`.

**Output, curated zone** (`curated/daily_revenue/day=2026-11-06/`):

| day | country | revenue | orders |
| --- | --- | --- | --- |
| 2026-11-06 | ES | 59.90 | 1 |
| 2026-11-06 | MX | 120.00 | 1 |

The output is Parquet, partitioned by `day`, so a query for one week reads only seven folders.

## Related

- [modern-data-architecture.md](modern-data-architecture.md): Spark is the engine under the managed ETL and big data framework kinds of the process stage, and a big data framework for delivery.
- [batch-and-streaming.md](batch-and-streaming.md): Spark is mainly a batch engine. Its Structured Streaming processes a stream as micro-batches, while Flink processes it record by record.
- [data-lake-zones.md](data-lake-zones.md): Spark jobs move data between the zones, as in the example from raw to curated.
- [partitioning.md](partitioning.md): Spark writes partitioned tables with `partitionBy`. Those `key=value/` folders are different from the in-memory partitions Spark splits a job into.
- [data-lakes-and-warehouses.md](data-lakes-and-warehouses.md): Spark usually writes Parquet, the columnar format that file explains.
- [open-table-formats.md](open-table-formats.md): Spark is one of the engines that read and write Iceberg, Hudi and Delta Lake tables.
- [emr.md](../aws/aws-services/aws-analytics/emr.md): EMR runs open-source Spark on clusters you control, or on EMR Serverless with no clusters.
- [glue.md](../aws/aws-services/aws-analytics/glue.md): Glue jobs are serverless Spark, with Glue's ETL library extending Spark with extra data types and operations.
- [troubleshooting-data-lakes.md](troubleshooting-data-lakes.md): slow or failing Spark jobs are its main transformation and performance issues, diagnosed with the Spark UI and fixed by rightsizing.
