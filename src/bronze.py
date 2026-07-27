from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = (
    spark.read
    .option("header", True)
    .csv("data/customers.csv")
)

df.write.mode("overwrite").saveAsTable(
    "main.customer.bronze_customers"
)

print("Bronze table created successfully.")