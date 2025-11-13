from pyspark.sql.functions import sum, avg, col

def analyze_sales(df):
    total_sales = df.groupBy("Region").agg(sum("Sales").alias("Total_Sales"))
    avg_sales = df.groupBy("Product").agg(avg("Sales").alias("Avg_Sales"))
    return total_sales, avg_sales
