#!/usr/bin/env python
import pika
import os

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=os.environ.get("RABBITMQ_HOST"))
)
channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange="", routing_key="hello", body="Ola Juliana World!")
print(" [x] Envia 'Oi Juliana'")
connection.close()
