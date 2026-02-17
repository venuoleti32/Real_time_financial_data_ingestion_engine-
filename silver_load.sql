COPY INTO financial_db.raw_ingestion.silver_stock_prices 
(SYMBOL, TRADE_DATE, OPEN_PRICE, HIGH_PRICE, LOW_PRICE, CLOSE_PRICE, VOLUME) 
FROM (
  SELECT 
    'IBM',               
    $1::DATE,            
    $2::FLOAT,           
    $3::FLOAT,           
    $4::FLOAT,           
    $5::FLOAT,           
    $6::NUMBER           
  FROM @FINANCIAL_DB.RAW_INGESTION.STOCK_DATA_STAGE
)
FILE_FORMAT = (FORMAT_NAME = 'my_csv_format')
ON_ERROR = 'CONTINUE';
