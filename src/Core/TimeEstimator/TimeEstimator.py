#!/usr/bin/env python
import pika
import time;
import os;

RMQHOST="rmq"
user=os.environ['USERNAME']
pswd=os.environ['PASSWORD']
#print(user+" "+pswd)

thecredential=pika.PlainCredentials(user,pswd)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RMQHOST,credentials=thecredential))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    #print(" [x] Received %r" % body)
    ts = ((time.time())*1000)
    delay=ts-float(body)
    #print("Received " + body + " at " + str(ts)+ " delay="+str(delay))    
    print("Received a message")
    ch.basic_ack(delivery_tag = method.delivery_tag)

######### Send a test message
ts = ((time.time())*1000)
channel.basic_publish(exchange='', routing_key='hello', body=str(ts))

###### which will be received by...
channel.basic_consume(
    queue='hello', on_message_callback=callback) # auto_ack=True removed

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
