# sf-crime-data-project

1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
	 - Changing SparkSession property params values affects the `processedRowsPerSecond` rate, which represents data throughput and latency.
2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
	- We want to maximize `processedRowsPerSecond`. From testing and researching online, I found that the following SparkSession property key/value pairs affected `processedRowsPerSecond` the most:
		- **spark.sql.shuffle.partitions**
			- This configures the number of partitions that are used when shuffling data for joins or aggregations. By default, the number of partitions is set to 200, but depending on how many cores you have in your Spark cluster, this may actually be adversely affect performance. If there are too many partitions, then task scheduling may take more time than execution time. If there are too few, then you will have idle worker nodes due to less concurrency. The recommended way to find the number of partitions for RDDs is to make it the number equal to the number of cores in the Spark cluster.
		- **spark.default.parallelism**
			- This is the default number of partitions in RDDs returned by transformations  (e.g., join, reduceByKey). This is already equal to the number of cores in the cluster, but depending on the skewness of returned partitions, like aggregation transformation for the police-calls, you may want to adjust this number.
		- **spark.streaming.kafka.maxRatePerPartition**
			- This caps the rate of processing per partition. This can prevent the first ingestion batch from being overwhelmed from large numbers of unprocessed messages. This can also prevent batches from being overwhelmed during sudden surges of messages from producers.
