#!/usr/bin/env python3
import pika
import json

def main():
    # Connect to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declare the same queue to listen to
    channel.queue_declare(queue='transactions')

    # Define the callback when a message is received
    def callback(ch, method, properties, body):
        body = json.loads(body)
        print(" [x] Received:", body)

    # Start consuming messages
    channel.basic_consume(queue='transactions', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    main()
