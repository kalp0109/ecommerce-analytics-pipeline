# ecommerce-analytics-pipeline
Real-time Ecommerce Analytics Pipeline using Apache Airflow, Kafka, PostgreSQL, Docker, and Power BI.


# Overview
This project demonstrates a real-time Ecommerce Analytics Pipeline built using Apache Airflow, PostgreSQL, Python, and Power BI. The pipeline simulates ecommerce events, stores them in a PostgreSQL database, and generates business insights through interactive Power BI dashboards.

# Architecture
Producer → PostgreSQL → Analytics Views → Power BI Dashboard

The workflow includes:

Event generation using Python
Data ingestion into PostgreSQL
SQL-based analytical transformations
Dashboard visualization in Power BI
# Tech Stack
Python
Apache Airflow
PostgreSQL
SQL
Power BI
Docker
# Project Structure
Ecommerce_analytics/
│
├── config/
│   └── settings.py
│
├── consumer/
│   └── consumer.py
│
├── database/
│   ├── __init__.py
│   └── connection.py
│
├── producer/
│   └── event_generator.py
│
├── Ecommerce_analytics.pbix
├── ecommerce_analytics.sql
├── ecommerce_analytics.drawio.png
└── README.md
# Features
Simulates ecommerce user activity
Stores event data in PostgreSQL
Generates analytical metrics using SQL views
Creates interactive Power BI dashboards
Supports automated orchestration with Airflow
# Database Metrics

The project tracks:
Total Events
Purchase Count
Revenue
Product Performance
Event Distribution by Time
User Activity Trends

# Dashboard Preview
Add screenshots inside an images folder and reference them here.
<img width="1996" height="1114" alt="image" src="https://github.com/user-attachments/assets/9d5b2b68-fd3e-475c-8258-639973032d24" />

# Business Insights

The dashboard provides insights into:

Revenue generation
Purchase behavior
Product popularity
Event activity trends
Overall ecommerce performance
# Key Learnings
Data pipeline design
PostgreSQL database integration
SQL analytics and reporting
Workflow orchestration with Airflow
Business intelligence using Power BI
End-to-end data engineering practices
# Future Enhancements
Apache Kafka integration
Real-time streaming analytics
Cloud deployment on AWS/Azure
Data quality monitoring
Automated alerting system



