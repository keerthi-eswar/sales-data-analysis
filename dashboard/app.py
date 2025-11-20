import os
import streamlit as st
import sys
from src.data_loader import load_data
from src.data_cleaner import clean_data
from src.sales_analysis import analyze_sales
from src.visualizer import (
    plot_total_sales, plot_avg_sales,
    plot_gender_sales, plot_age_sales,
    plot_state_sales, plot_company_sales,
    plot_district_sales
)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.set_page_config(page_title="Sales Data Analysis Dashboard", layout="wide")
st.title("📊 Sales Data Analysis Dashboard")

data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/sales_data.csv"))

st.sidebar.header("Data Settings")

if st.sidebar.button("Load & Analyze Data"):

    df = load_data(data_path)
    df = clean_data(df)

    (total_sales, avg_sales, gender_sales,
     age_sales, state_sales, company_sales,
     district_sales) = analyze_sales(df)

    st.subheader("📌 Total Sales by Region")
    st.plotly_chart(plot_total_sales(total_sales), use_container_width=True)

    st.subheader("📌 Average Sales by Product")
    st.plotly_chart(plot_avg_sales(avg_sales), use_container_width=True)

    st.subheader("📌 Gender-wise Sales")
    st.plotly_chart(plot_gender_sales(gender_sales), use_container_width=True)

    st.subheader("📌 Age-wise Sales")
    st.plotly_chart(plot_age_sales(age_sales), use_container_width=True)

    st.subheader("📌 State-wise Sales")
    st.plotly_chart(plot_state_sales(state_sales), use_container_width=True)

    st.subheader("📌 Company-wise Sales")
    st.plotly_chart(plot_company_sales(company_sales), use_container_width=True)

    st.subheader("📌 District-wise Sales")
    st.plotly_chart(plot_district_sales(district_sales), use_container_width=True)

