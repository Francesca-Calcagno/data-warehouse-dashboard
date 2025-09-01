import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


@st.cache_data
def load_data():
    df = pd.read_csv("final_joined_dataset.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()


st.sidebar.header("Date Range Filter")
start_date = st.sidebar.date_input("Start date", pd.to_datetime("2024-01-01"))
end_date = st.sidebar.date_input("End date", pd.to_datetime("2024-12-31"))


filtered_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]

st.title("Time Analysis Dashboard")


st.subheader("Total Transactions Over Time")
transactions_over_time = filtered_df.groupby('Date').size()
st.line_chart(transactions_over_time)


st.subheader("Top 3 Traded Symbols by Transaction Count")
top_symbols = filtered_df['Symbol'].value_counts().head(3)
st.bar_chart(top_symbols)


st.subheader("Top 5 Sectors by Transaction Count")
top_sectors = filtered_df['sector'].value_counts().head(5)
st.bar_chart(top_sectors)


st.subheader("Top 5 Industries by Transaction Count")
top_industries = filtered_df['industry'].value_counts().head(5)
st.bar_chart(top_industries)
