from pyspark.sql.functions import col, round, avg, desc

def load_data(spark, path):
    return spark.read.csv(path, header=True, inferSchema=True)

def clean_data(df):
    df = df.dropna()
    df = df.dropDuplicates()
    return df

def show_data(df, n=5):
    return df.show(n)

def describe_data(df):
    return df.describe().show()
