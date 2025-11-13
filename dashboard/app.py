import streamlit as st
from src.data_loader import load_data
from src.data_cleaner import clean_data
from src.sales_analysis import analyze_sales
from src.visualizer import plot_total_sales, plot_avg_sales

st.set_page_config(page_title="Sales Data Analysis Dashboard", layout="wide")

st.title("📊 Sales Data Analysis Dashboard")

data_path = "../data/sales_data.csv"

st.sidebar.header("Data Settings")
if st.sidebar.button("Load and Analyze Data"):
    df = load_data(data_path)
    df = clean_data(df)
    total_sales, avg_sales = analyze_sales(df)

    st.subheader("Total Sales by Region")
    st.plotly_chart(plot_total_sales(total_sales), use_container_width=True)

    st.subheader("Average Sales by Product")
    st.plotly_chart(plot_avg_sales(avg_sales), use_container_width=True)
