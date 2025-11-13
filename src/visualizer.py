import pandas as pd
import plotly.express as px

def plot_total_sales(total_sales):
    pdf = total_sales.toPandas()
    fig = px.bar(pdf, x="Region", y="Total_Sales", title="Total Sales by Region", color="Region")
    return fig

def plot_avg_sales(avg_sales):
    pdf = avg_sales.toPandas()
    fig = px.pie(pdf, names="Product", values="Avg_Sales", title="Average Sales by Product")
    return fig
