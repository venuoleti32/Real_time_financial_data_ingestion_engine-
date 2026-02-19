import os
import time
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import requests
from io import StringIO

# 1. Configuration
SYMBOLS = ['IBM', 'AAPL', 'TSLA', 'NVDA', 'GOOGL'] # Add any tickers you want
API_KEY = os.getenv('AV_KEY')

def fetch_data(symbol):
    print(f"Fetching data for {symbol}...")
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}&datatype=csv'
    response = requests.get(url)
    df = pd.read_csv(StringIO(response.text))
    
    # Standardize columns
    df = df.rename(columns={
        'timestamp': 'TRADE_DATE', 'open': 'OPEN_PRICE', 
        'high': 'HIGH_PRICE', 'low': 'LOW_PRICE', 
        'close': 'CLOSE_PRICE', 'volume': 'VOLUME'
    })
    df['SYMBOL'] = symbol
    return df

# 2. Main Loop
all_data = []
for s in SYMBOLS:
    try:
        data = fetch_data(s)
        all_data.append(data)
        time.sleep(15) # Stay under the 5 calls/min limit
    except Exception as e:
        print(f"Error fetching {s}: {e}")

final_df = pd.concat(all_data, ignore_index=True)

# 3. Push to Snowflake
conn = snowflake.connector.connect(
    user=os.getenv('SF_USER'),
    password=os.getenv('SF_PASS'),
    account=os.getenv('SF_ACCT'),
    warehouse='COMPUTE_WH',
    database='FINANCIAL_DB',
    schema='RAW_INGESTION'
)

success, nchunks, nrows, _ = write_pandas(conn, final_df, "SILVER_STOCK_PRICES")
print(f"Success! Total rows loaded: {nrows}")
conn.close()
