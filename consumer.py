#!/usr/bin/env python
import pika

url = "amqp://btvgehsd:3wZjvPw9VTE--vbGBFeiKLXo_T9Hi2eY@spotted-monkey.rmq.cloudamqp.com/btvgehsd"
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel

def callback(ch, method, properties, body):
  print "[x] received %r" % (body)

channel.basic_consume(callback, queue='hello', no_ack=True)
channel.start_consuming()
