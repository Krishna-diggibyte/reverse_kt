from pyspark.sql.functions import collect_set

data = [("a",), ("b",), ("a",), ("a",), ("c",), ("d",), ("d",)]
df = spark.createDataFrame(data, ["id"])

collect_set_df = df.agg(collect_set("id").alias("unique_values"))
df.display()
collect_set_df.display()