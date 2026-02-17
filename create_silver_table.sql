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

