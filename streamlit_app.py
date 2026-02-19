import streamlit as st
from snowflake.snowpark.context import get_active_session

# Page Setup
st.set_page_config(layout="wide")
st.title("🚀 Portfolio Command Center")

# Connect to Snowflake
session = get_active_session()


metrics_query = """
    SELECT 
        SUM(CURRENT_VALUE) as TOTAL_VAL,
        SUM(TOTAL_PROFIT_LOSS) as TOTAL_PL,
        (SUM(TOTAL_PROFIT_LOSS) / NULLIF(SUM(TOTAL_COST), 0)) * 100 as ROI
    FROM FINANCIAL_DB.RAW_INGESTION.PORTFOLIO_PERFORMANCE
"""
metrics = session.sql(metrics_query).to_pandas()


col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Portfolio Value", f"${metrics['TOTAL_VAL'][0]:,.2f}")
with col2:
    st.metric("Total Profit/Loss", f"${metrics['TOTAL_PL'][0]:,.2f}")
with col3:
    st.metric("Return on Investment", f"{metrics['ROI'][0]:.2f}%")


st.write("---")
holdings_query = "SELECT SYMBOL, CURRENT_VALUE FROM FINANCIAL_DB.RAW_INGESTION.PORTFOLIO_PERFORMANCE"
holdings_df = session.sql(holdings_query).to_pandas()

st.subheader("Value by Stock Symbol")
st.bar_chart(data=holdings_df, x="SYMBOL", y="CURRENT_VALUE")


st.subheader("Detailed Portfolio Breakdown")
st.dataframe(session.sql("SELECT * FROM FINANCIAL_DB.RAW_INGESTION.PORTFOLIO_PERFORMANCE").to_pandas())
