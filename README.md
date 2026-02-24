# 📈 Automated Multi-Stock ETL Pipeline & Portfolio Dashboard

A production-grade data engineering project that automates the collection, transformation, and visualization of stock market data using a modern data stack.

## 🏗️ Architecture
The pipeline is fully automated and runs daily without manual intervention:
1. **Extraction:** Python script triggered by **GitHub Actions** fetches daily stock prices from the **Alpha Vantage API**.
2. **Loading:** Data is securely pushed to **Snowflake** using the `snowflake-connector-python`.
3. **Transformation:** SQL views in Snowflake (Silver/Gold layers) calculate 5-day moving averages and daily volatility.
4. **Visualization:** A **Streamlit** dashboard hosted in Snowflake provides real-time portfolio analytics and ROI tracking.



## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Warehouse:** Snowflake
* **Orchestration:** GitHub Actions (CI/CD)
* **Visualization:** Streamlit
* **Security:** GitHub Secrets (Environment Variable Management)

## 🚀 Key Features
* **Multi-Stock Support:** Scalable loop logic to ingest data for multiple tickers (AAPL, TSLA, NVDA, etc.).
* **Automated Scheduling:** CRON job triggers every weekday at 21:00 UTC.
* **Portfolio Analytics:** Dynamic SQL views join manual "buy" data with live market prices to calculate unrealized P/L.
* **Rate-Limit Handling:** Built-in sleep logic to respect API provider constraints.

## Dashboard
> **Note:** The dashboard displays real-time metrics including:
> * Total Portfolio Net Worth
> * Unrealized Profit/Loss (P/L)
> * Return on Investment (ROI %)
> * Asset Distribution Bar Charts

---
*Developed as a showcase of cloud data engineering and automated financial analytics.*
