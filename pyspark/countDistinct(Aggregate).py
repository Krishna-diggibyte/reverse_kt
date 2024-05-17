from pyspark.sql.functions import countDistinct

data = [(1, "a"), (1, "b"), (1, "a"), (2, "c"), (2, "d"), (2, "d")]
df = spark.createDataFrame(data, ["id", "value"])

distinct_value_count = df.agg(countDistinct("value").alias("distinct_values"))
display(distinct_value_count)

result_df = df.agg(collect_set("value").alias("unique_values"))
display(result_df)