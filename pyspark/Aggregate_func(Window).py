from pyspark.sql.functions import sum, avg, min, max, count
from pyspark.sql.window import Window

data = [(1, 10), (1, 20), (1, 30), (1, 30), (2, 40), (2, 50), (2, 60)]
df = spark.createDataFrame(data, ["id", "value"])

# Define window specification
window_spec = Window.partitionBy("id")

# Compute cumulative sum, average, min, max, and count
df_with_aggregations = df.withColumn("sum", sum("value").over(window_spec)) \
                         .withColumn("avg", avg("value").over(window_spec)) \
                         .withColumn("min", min("value").over(window_spec)) \
                         .withColumn("max", max("value").over(window_spec)) \
                         .withColumn("row_count", count("value").over(window_spec))

df_with_aggregations.display()
