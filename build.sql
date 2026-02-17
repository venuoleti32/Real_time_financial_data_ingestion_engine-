-- Create the logical containers
CREATE DATABASE financial_db;
CREATE SCHEMA financial_db.raw_ingestion;

-- Create a Warehouse (Compute) - X-Small is plenty for this
CREATE WAREHOUSE financial_wh 
  WAREHOUSE_SIZE = 'XSMALL' 
  AUTO_SUSPEND = 60 
  AUTO_RESUME = TRUE;

  USE ROLE SYSADMIN;
USE DATABASE financial_db;
USE SCHEMA raw_ingestion;


-- Create an internal stage to hold your CSVs
CREATE OR REPLACE STAGE stock_data_stage;

-- Create a File Format to tell Snowflake how to read your CSV
CREATE OR REPLACE FILE FORMAT my_csv_format
  TYPE = 'CSV'
  FIELD_DELIMITER = ','
  SKIP_HEADER = 1
  NULL_IF = ('NULL', 'null')
  EMPTY_FIELD_AS_NULL = TRUE;



  CREATE OR REPLACE TABLE daily_stock_prices (
    symbol STRING,
    trade_date DATE,
    open_price FLOAT,
    high_price FLOAT,
    low_price FLOAT,
    close_price FLOAT,
    volume NUMBER,
    ingested_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

CREATE TABLE IF NOT EXISTS financial_db.raw_ingestion.silver_stock_prices (
    symbol STRING,
    trade_date DATE,
    open_price FLOAT,
    high_price FLOAT,
    low_price FLOAT,
    close_price FLOAT,
    volume NUMBER,
    ingested_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP(),
    PRIMARY KEY (symbol, trade_date)
);
