#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
message="Hello World!!!!"

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                     body=message)
print(" [x] Sent {0}".format(message))
connection.close()


