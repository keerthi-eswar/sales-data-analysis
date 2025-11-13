from pyspark.sql import SparkSession

def load_data(file_path):
    spark = SparkSession.builder \
        .appName("Sales Data Analysis") \
        .getOrCreate()
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    return df
