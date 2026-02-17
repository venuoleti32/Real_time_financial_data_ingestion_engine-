

COPY INTO financial_db.raw_ingestion.silver_stock_prices
FROM (
  SELECT 
    'IBM',               
    $1::DATE,            
    $2::FLOAT,           
    $3::FLOAT,           
    $4::FLOAT,           
    $5::FLOAT,           
    $6::NUMBER           
  FROM @stock_data_stage
)
FILE_FORMAT = (FORMAT_NAME = 'my_csv_format')
ON_ERROR = 'CONTINUE';   
