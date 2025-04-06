from src.spark_session import sparkSession
from src.transformations import load_data, clean_data, show_data, describe_data

def main():
    spark = sparkSession()

    df = load_data(spark, "dataset/global_housing_market_extended.csv")
    cleaned_df = clean_data(df)
    show_data(cleaned_df)
    # print the schema of the dataframe
    print(cleaned_df.printSchema())
    # print country columns
    print(cleaned_df.select("Country").show())
    spark.stop()

if __name__ == "__main__":
    main()