# managed table
df.write.saveAsTable("mydata12")

# external table
df.write.option("path", "dbfs:/FileStore/reversekt/mydata11").saveAsTable("mydata11")

# list files
%fs ls dbfs:/FileStore/reversekt/