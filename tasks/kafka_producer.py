import json
import os

from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=[os.getenv("KAFKA_HOST", "kafka:9092")],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


def send_kafka_message(topic, message):
    producer.send(topic, message)
    producer.flush()
