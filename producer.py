#!/usr/bin/env python3
import json
import pika

# Connect to RabbitMQ server running on localhost
conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = conn.channel()

# Declare a queue named 'transactions'
channel.queue_declare(queue="transactions")

# Send a test transaction message
channel.basic_publish(
    exchange="",
    routing_key="transactions",
    body=json.dumps({
        "card_num": 12340000,
        "total": 4.10
    })
)

print(" [x] Sent transaction")
conn.close()
