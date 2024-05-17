df.display()
# save
df.write.format('csv').save("dbfs:/FileStore/reversekt/mydata")
# list file
%fs ls dbfs:/FileStore/reversekt/mydata
# saveastable
df.write.format('delta').saveAsTable("mydata1")
