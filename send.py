#!/usr/bin/env python
import pika

url = "amqp://btvgehsd:3wZjvPw9VTE--vbGBFeiKLXo_T9Hi2eY@spotted-monkey.rmq.cloudamqp.com/btvgehsd"
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
