import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import requests
from io import StringIO


SYMBOL = 'IBM'
API_KEY = 'XXXXXXXXX'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={SYMBOL}&apikey={API_KEY}&datatype=csv'

response = requests.get(url)
df = pd.read_csv(StringIO(response.text))


df = df.rename(columns={
    'timestamp': 'TRADE_DATE',
    'open': 'OPEN_PRICE',
    'high': 'HIGH_PRICE',
    'low': 'LOW_PRICE',
    'close': 'CLOSE_PRICE',
    'volume': 'VOLUME'
})
df['SYMBOL'] = SYMBOL
df['TRADE_DATE'] = pd.to_datetime(df['TRADE_DATE']).dt.date

# 3. Connect and Push to Snowflake
conn = snowflake.connector.connect(
    user='VENUOLETI32',
    password='XXXXXXXX',
    account='FRVIAWM-LP02516', 
    warehouse='COMPUTE_WH',
    database='FINANCIAL_DB',
    schema='RAW_INGESTION'
)


success, nchunks, nrows, _ = write_pandas(conn, df, "SILVER_STOCK_PRICES")

print(f"Success! Loaded {nrows} rows into Snowflake.")
conn.close()
