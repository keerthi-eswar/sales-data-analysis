import plotly.express as px

def plot_total_sales(total_sales):
    pdf = total_sales.toPandas()
    return px.bar(pdf, x="Region", y="Total_Sales", title="Total Sales by Region", color="Region")

def plot_avg_sales(avg_sales):
    pdf = avg_sales.toPandas()
    return px.pie(pdf, names="Product", values="Avg_Sales", title="Average Sales by Product")

def plot_gender_sales(gender_sales):
    pdf = gender_sales.toPandas()
    return px.bar(pdf, x="Gender", y="Gender_Sales", title="Gender-wise Sales", color="Gender")

def plot_age_sales(age_sales):
    pdf = age_sales.toPandas()
    return px.line(pdf, x="Age", y="Age_Sales", title="Age-wise Sales")

def plot_state_sales(state_sales):
    pdf = state_sales.toPandas()
    return px.bar(pdf, x="State", y="State_Sales", title="State-wise Sales", color="State")

def plot_company_sales(company_sales):
    pdf = company_sales.toPandas()
    return px.pie(pdf, names="Company", values="Company_Sales", title="Company-wise Sales")

def plot_district_sales(district_sales):
    pdf = district_sales.toPandas()
    return px.bar(pdf, x="District", y="District_Sales", title="District-wise Sales", color="District")
