from pyspark.sql.functions import mean

data = [(1,), (2,), (4,)]
df = spark.createDataFrame(data, ["numbers"])

mean_df = df.select(mean("numbers").alias("mean_value"))
mean_df.display()
