#!/usr/bin/env python
import pika
import time
import os
from google.protobuf.struct_pb2 import Struct

RMQHOST="rmq"
QNAME="timeestimation"
user=os.environ['USERNAME']
pswd=os.environ['PASSWORD']
#print(user+" "+pswd)

######### Self Initialization 

######### Queue Initialization
thecredential=pika.PlainCredentials(user,pswd)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RMQHOST,credentials=thecredential))
channel = connection.channel()
channel.queue_declare(queue=QNAME)

######## Msg handler
def callback(ch, method, properties, body):
    #print(" [x] Received %r" % body)
    ts = ((time.time())*1000)
    delay=ts-float(body)
    print("Received " + str(body) + " at " + str(ts)+ " delay="+str(delay))    
    #print("Received a message")
    ch.basic_ack(delivery_tag = method.delivery_tag)

######### Send a test message
ts = ((time.time())*1000)
channel.basic_publish(exchange='', routing_key=QNAME, body=str(ts))

###### which will be received by...
channel.basic_consume(
    queue=QNAME, on_message_callback=callback) # auto_ack=True removed

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
