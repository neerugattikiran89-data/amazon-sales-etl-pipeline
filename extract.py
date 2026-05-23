#Extract(E):

from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, upper
#Create Spark Session:

spark = SparkSession.builder \
    .appName("ETL-Project") \
    .getOrCreate()

#Read CSV file:

df = spark.read.csv(
    "data/Amazon Sale Report.csv",
    header=True,
    inferSchema=True
) 

#Show data
df.show()

#show schema
df.printSchema()

#Transform(T)
print("Total Rows:", df.count())

print(df.columns)

df = df.drop("Unnamed: 22")

print(df.columns)

shipped_df = df.filter(df["Status"] == "Shipped")

shipped_df.show()

clean_df = shipped_df.select(
    "Order ID",
    "Category",
    "Amount",
    "ship-state",
    "Qty"
)

clean_df.show()

clean_df.filter(clean_df["Amount"].isNull()).show()

clean_df = clean_df.dropna(subset=["Amount"])

clean_df = clean_df.withColumn(
"ship-state",
 upper(clean_df["ship-state"])
)
print("Clean Rows:", clean_df.count())


from pyspark.sql.functions import sum

clean_df.groupBy("ship-state") \
    .agg(sum("Amount").alias("Total Sales")) \
    .show()

from pyspark.sql.functions import sum
state_sales = clean_df.groupBy("ship-state") \
    .agg(sum("Amount").alias("total Sales")) 

state_sales.orderBy("Total Sales", ascending=False).show()

#Load(L):

clean_df.toPandas().to_csv(
    "output_clean_orders.csv",
    index=False
)

print("ETL Pipeline Completed Successfully")

spark.stop()
