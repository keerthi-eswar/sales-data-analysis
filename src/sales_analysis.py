from pyspark.sql.functions import sum, avg

def analyze_sales(df):
    total_sales = df.groupBy("Region").agg(sum("Sales").alias("Total_Sales"))
    avg_sales = df.groupBy("Product").agg(avg("Sales").alias("Avg_Sales"))

    gender_sales = df.groupBy("Gender").agg(sum("Sales").alias("Gender_Sales"))
    age_sales = df.groupBy("Age").agg(sum("Sales").alias("Age_Sales"))
    state_sales = df.groupBy("State").agg(sum("Sales").alias("State_Sales"))
    company_sales = df.groupBy("Company").agg(sum("Sales").alias("Company_Sales"))
    district_sales = df.groupBy("District").agg(sum("Sales").alias("District_Sales"))

    return (
        total_sales,
        avg_sales,
        gender_sales,
        age_sales,
        state_sales,
        company_sales,
        district_sales
    )
