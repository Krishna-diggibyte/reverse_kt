from pyspark.sql.functions import avg

data = [(1,), (2,), (None,), (4,)]
df = spark.createDataFrame(data, ["numbers"])

avg_df = df.select(avg("numbers").alias("avg_value"))
avg_df.display()