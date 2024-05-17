from pyspark.sql.functions import collect_list

data = [(1, "a"), (1, "b"), (1, "a"), (2, "c"), (2, "d"), (2, "d")]
df = spark.createDataFrame(data, ["id", "value"])

collect_list_df = df.groupBy("id").agg(collect_list("value").alias("all_values"))
collect_list_df.display()
