from pyspark.sql.functions import count
data = [(1, "a"), (1, "b"), (1, None), (2, "c"), (2, "d"), (2, "d")]
df = spark.createDataFrame(data, ["id", "value"])

total_count = df.agg(count("*").alias("total_rows")).collect()[0]["total_rows"]
print(f"Total number of rows: {total_count}")

value_count = df.agg(count("value").alias("non_null_values"))
value_count.display()