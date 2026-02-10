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
