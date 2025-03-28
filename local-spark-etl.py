from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round, avg, desc
import os

# Initialize Spark session


sparkSession = SparkSession.builder.appName("local-spark-etl").getOrCreate()

df = sparkSession.read.csv("dataset/global_housing_market_extended.csv", header=True, inferSchema=True)

df.show()
