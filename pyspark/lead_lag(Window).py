from pyspark.sql.functions import lead, lag
from pyspark.sql.window import Window

data = [(1, 10), (1, 20), (1, 30), (2, 40), (2, 50), (2, 60)]
df = spark.createDataFrame(data, ["id", "value"])
display(df)
window_spec = Window.partitionBy("id").orderBy("value")

# Compute lead
df_with_lead = df.withColumn("next_value", lead("value", 1).over(window_spec))
# df_with_lead.display()

# Compute lag
df_with_lag = df_with_lead.withColumn("previous_value", lag("value", 1).over(window_spec))
df_with_lag.display()