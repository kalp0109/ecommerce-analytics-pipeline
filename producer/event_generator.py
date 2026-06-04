# Importing required libraries
import random
import json
from datetime import datetime
import time
from kafka import KafkaProducer
import uuid
from config.settings import KAFKA_BROKER, TOPIC_NAME



products = ["Laptop","iPhone","Headphones","Keyboard","Monitor"]

event_types = ["view","add_to_cart","purchase"]


producer = KafkaProducer(bootstrap_servers = KAFKA_BROKER, value_serializer = lambda v : json.dumps(v).encode('utf-8'))

while True:
   
    log_activity ={
            'event_id': str(uuid.uuid4()),
            'user_id': random.randint(100,999),
            'products': random.choice(products),
            'event_type': random.choice(event_types),
            'prices': random.randint(50000, 200000),
            'event_time': str(datetime.now())}


    print(log_activity)

    producer.send(TOPIC_NAME,value = log_activity)
    producer.flush()

    time.sleep(2)

