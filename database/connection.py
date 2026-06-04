import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        database='ecommerce_db',  
        user='postgres',
        password='root'
    )
    return conn