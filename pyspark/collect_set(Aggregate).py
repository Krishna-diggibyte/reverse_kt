from pyspark.sql.functions import collect_set

data = [(1, "a"), (1, "b"), (1, "a"), (2, "a"), (2, "c"), (2, "d"), (2, "d")]
df = spark.createDataFrame(data, ["id", "value"])

collect_set_df = df.groupBy("id").agg(collect_set("value").alias("unique_values"))
collect_set_df.display()
