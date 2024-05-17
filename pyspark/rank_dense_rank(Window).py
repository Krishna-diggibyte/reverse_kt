from pyspark.sql.functions import rank, dense_rank
from pyspark.sql.window import Window

data = [(1, 50), (1, 20), (1, 50),(1, 10), (2, 30), (2, 30), (2, 10)]
df = spark.createDataFrame(data, ["id", "score"])

window_spec = Window.partitionBy("id").orderBy(df["score"].desc())

df_with_rank = df.withColumn("rank", rank().over(window_spec))

df_with_dense_rank = df_with_rank.withColumn("dense_rank", dense_rank().over(window_spec))
df_with_dense_rank.display()
