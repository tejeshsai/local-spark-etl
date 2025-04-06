from pyspark.sql import SparkSession

def sparkSession(appName = "GlobalHouseMarketApp"):
    spark = SparkSession.builder.appName(appName).getOrCreate()
    return spark