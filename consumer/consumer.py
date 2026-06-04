from kafka import KafkaConsumer
import json
from datetime import datetime
from config.settings import KAFKA_BROKER, TOPIC_NAME, CONSUMER_GROUP
from database.connection import get_db_connection
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s -%(levelname)s -%(message)s')
logger = logging.getLogger(__name__)

consumer = KafkaConsumer(
            TOPIC_NAME,
             bootstrap_servers = KAFKA_BROKER,
             auto_offset_reset = 'earliest',
             group_id =CONSUMER_GROUP,

             value_deserializer = lambda x: json.loads(x.decode('utf-8'))
)


logger.info("Consumer started... Waiting for messages!!")


# DB connection
conn = get_db_connection()
cursor = conn.cursor()

# insert data into postgres 
insert_query = """insert into orders(event_id,user_id,products,event_type, prices, event_time)
                    values(%s,%s,%s,%s,%s,%s)"""


def is_valid(data):
    required_fields =['event_id', 'user_id','products','event_type','prices','event_time']  

    for field in required_fields:
        if field not in data or data[field] is None:
            return False
    
    return True



for message in consumer:
    data = message.value
    logger.info(f"Recieved: {data}")


    try:
        if not is_valid(data):
            logger.info(f"Skipping invalid record: {data}")
            continue

        # extract fields from Kafka message
        values = (
        data.get('event_id'),
        data.get('user_id'),
        data.get('products'),
        data.get('event_type'),
        data.get('prices'),
        data.get('event_time')
    )
        # insert into postgres
        cursor.execute(insert_query, values)
        conn.commit()
        logger.info("Inserted into PostgreSQL")

    except Exception as e:
        logger.error(f"Error inserting: {e}")
        conn.rollback()
