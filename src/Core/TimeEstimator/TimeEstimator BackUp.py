#!/usr/bin/env python
import pika
import time
import os
from google.protobuf.struct_pb2 import Struct
import GeneralMsg_pb2 #this file exist in TimeEstimator folder for debug, but it 

RMQHOST="rmq"
QNAME="timeestimation"

user=os.environ['USERNAME']
pswd=os.environ['PASSWORD']
#print(user+" "+pswd)

######### Self Initialization 
PCT={} #make PCT a dictionary 
######### Queue Initialization
thecredential=pika.PlainCredentials(user,pswd)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RMQHOST,credentials=thecredential))
channel = connection.channel()
channel.queue_declare(queue=QNAME)

###### Testing section
#create mock up distribution
aDist={}
aDist['abc']=[10,20,30,40]
PCT['amachinetype']=aDist
######### Send a test message
testmessage=GeneralMsg_pb2.ServiceRequest()
testmessage.Operation="time_query"
testmessage.ReturnDest="self"
S= Struct()
S.update({"task_type": "amachinetype"})
S.update({"machine_type": "abc"})
print(S)
testmessage.details['task_type']='amachinetype'
testmessage.details['machine_type']='abc'
channel.basic_publish(exchange='', routing_key=QNAME, body=testmessage.SerializeToString()) #will change qname later, after this test
#ts = ((time.time())*1000)
#channel.basic_publish(exchange='', routing_key=QNAME, body=str(ts))



def msghandling(aRequest):
    if (aRequest.operation == 'time_query'):
        tasktype=aRequest.details['task_type']
        machinetype=aRequest.details['machine_type']

        machine_distribution=PCT[machinetype]
        if(machine_distribution==None):
            print("requested distribution of unknown machine type")
            return
        
        distribution=machine_distribution[tasktype]
        if(distribution==None):
            print("requested distribution of unknown task type")
            return
        #so... we have it... 
        returnmsg=GeneralMsg_pb2.ServiceRequest()
        returnmsg.Operation="time_distribution"
        returnmsg.ReturnDest=""
        returnmsg.details=Struct()
        returnmsg.details['task_type']=tasktype
        returnmsg.details['machine_type']=machinetype
        channel.basic_publish(exchange='', routing_key=QNAME, body=returnmsg.SerializeToString()) #will change qname later, after this test
    elif (aRequest.operation =='time_learn'):
        pass
    else:
        print("unknown request type:"+aRequest.operation)

        pass



######## Msg handler
def callback(ch, method, properties, body):
    #print(" [x] Received %r" % body)
    #ts = ((time.time())*1000)
    #delay=ts-float(body)
    #print("Received " + str(body) + " at " + str(ts)+ " delay="+str(delay))    
    
    print("Received a message")
    #do time estimator thing to 'body'
    # #body = OPERATION, CALLBACKQUEUE, paremeters
    parsedbody = GeneralMsg_pb2.ServiceRequest()
    parsedbody.ParseFromString(body)
    msghandling(parsedbody)
    ch.basic_ack(delivery_tag = method.delivery_tag)


############### String version
    # msg=body.decode().split()
    # if(len(msg)>3):
    #     returnqueuename=msg[1]
    #     if(msg[0]=='time_query'):
    #         aPCT=PCT.get(msg[2])
    #         if(aPCT != None):
    #             distribution=aPCT.get(msg[3])
    #             if(distribution != None):
    #                 channel.basic_publish(exchange='', routing_key=returnqueuename, body='time_return '+msg[2]+' '+msg[3]+' '+str(distribution))
    #     elif (msg[1]=='time_learn'):
    #         #pass
    #         s = Struct()
            
    #     else:
    #         channel.basic_publish(exchange='', routing_key=returnqueuename, body='Error, Unknown operation received')


    #



###### which will be received by...
channel.basic_consume(
    queue=QNAME, on_message_callback=callback) # auto_ack=True removed

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
