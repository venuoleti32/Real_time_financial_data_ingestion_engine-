-- scripts/silver_load.sql
COPY INTO financial_db.raw_ingestion.silver_stock_prices 
(SYMBOL, TRADE_DATE, OPEN_PRICE, HIGH_PRICE, LOW_PRICE, CLOSE_PRICE, VOLUME) -- We list only 7 columns
FROM (
  SELECT 
    'IBM',               -- 1
    $1::DATE,            -- 2
    $2::FLOAT,           -- 3
    $3::FLOAT,           -- 4
    $4::FLOAT,           -- 5
    $5::FLOAT,           -- 6
    $6::NUMBER           -- 7
  FROM @FINANCIAL_DB.RAW_INGESTION.STOCK_DATA_STAGE
)
FILE_FORMAT = (FORMAT_NAME = 'my_csv_format')
ON_ERROR = 'CONTINUE';
