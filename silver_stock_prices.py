import os
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

conn = snowflake.connector.connect(
    user=os.getenv('SF_USER'),
    password=os.getenv('SF_PASS'),
    account=os.getenv('SF_ACCT'),
    warehouse='COMPUTE_WH',
    database='FINANCIAL_DB',
    schema='RAW_INGESTION'
)
