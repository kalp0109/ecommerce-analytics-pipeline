-- Database: ecommerce_db

-- DROP DATABASE IF EXISTS ecommerce_db;

CREATE DATABASE ecommerce_db
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;




create table orders
	(event_id text primary key,
	 user_id int,
	 products text,
	 event_type text,
	 prices int,
	 event_time timestamp);


select * from orders;


select count(*) from orders;


-- Creating view 


CREATE VIEW product_metrics AS
SELECT 
    products,
    COUNT(*) AS total_events,
    SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS purchase_count,
    SUM(CASE WHEN event_type = 'purchase' THEN prices ELSE 0 END) AS revenue
FROM orders
GROUP BY products;


CREATE VIEW daily_sales AS
SELECT
    DATE(event_time) AS sales_date,
    COUNT(*) AS total_events,
    SUM(prices) AS revenue
FROM orders
GROUP BY DATE(event_time)
ORDER BY sales_date;



CREATE VIEW hourly_sales AS
SELECT
    DATE_TRUNC('hour', event_time) AS sales_hour,
    COUNT(*) AS total_events,
    SUM(prices) AS revenue
FROM orders
GROUP BY sales_hour
ORDER BY sales_hour;

drop view hourly_sales;

CREATE VIEW hourly_sales AS
SELECT
    EXTRACT(HOUR FROM event_time) AS event_hour,
    COUNT(*) AS total_events,
    SUM(prices) AS revenue
FROM orders
GROUP BY EXTRACT(HOUR FROM event_time)
ORDER BY event_hour;

