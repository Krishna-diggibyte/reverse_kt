from pyspark.sql.functions import row_number
from pyspark.sql.window import Window

data = [(1, "A"), (1, "B"), (1, "C"), (2, "D"), (2, "E"), (2, "F")]
df = spark.createDataFrame(data, ["id", "value"])

# Define window specification
window_spec = Window.partitionBy("id").orderBy("value")

# Compute row number
df_with_row_number = df.withColumn("row_number", row_number().over(window_spec))
df_with_row_number.display()
