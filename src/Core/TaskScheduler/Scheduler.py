#!/usr/bin/env python
import pika
import time
import os
import MSC_msg.OpType as OpType
import MSC_msg.SchedulerMsg as SchedulerMsg
import MSC_msg.MachineReportMsg as MachineReportMsg

import flatbuffers

RMQHOST="rmq"
QNAME="timeestimation"
LOGQNAME="logqueue"
MYROLE="TimeEstimator"


user=os.environ['USERNAME']
pswd=os.environ['PASSWORD']
#loglvl=os.environ['LOGLVL']
#print(user+" "+pswd)


###### status: something wrong with connection... it worked, now it is not.

######### Self Initialization 
PCT={} #make PCT a dictionary 
######### Queue Initialization
thecredential=pika.PlainCredentials(user,pswd)
#print("Connecting to RMQHOST"+)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RMQHOST,credentials=thecredential))
channel = connection.channel()
channel.queue_declare(queue=QNAME)
msgbuilder=flatbuffers.Builder(1024)

###### Testing section
#create mock up distribution
aDist={}
aDist['abc']=[10,20,30,40]
PCT['amachinetype']=aDist
######### Send a test message
selfdest = msgbuilder.CreateString('self')
atasktype = msgbuilder.CreateString('abc')
amachinetype=msgbuilder.CreateString('amachinetype')

SchedulerMsg.Start(msgbuilder)
SchedulerMsg.AddOperation(msgbuilder,OpType.OpType().time_query)
SchedulerMsg.AddReturnDest(msgbuilder,selfdest)
SchedulerMsg.AddUserId(msgbuilder,0)
SchedulerMsg.AddPriority(msgbuilder,0)
SchedulerMsg.AddTaskType(msgbuilder,atasktype)
SchedulerMsg.AddMachineType(msgbuilder,amachinetype)
####### finally
themessage=SchedulerMsg.End(msgbuilder)
#print(themessage)
msgbuilder.Finish(themessage)

channel.basic_publish(exchange='', routing_key=QNAME, body=msgbuilder.Output()) #will change qname later, after this test
#ts = ((time.time())*1000)
#channel.basic_publish(exchange='', routing_key=QNAME, body=str(ts))



def msghandling(aRequest):
    print(aRequest)
    #print(aRequest.Operation())
    #print("OPTYPE:"+str(OpType.OpType.time_query))
    if (aRequest.Operation() == OpType.OpType.time_query):
        tasktype=aRequest.TaskType().decode('UTF-8')
        machinetype=aRequest.MachineType().decode('UTF-8')
        print("machinetype=")
        print(tasktype)
        print("tasktype=")
        print(machinetype)
        
        
        if(not machinetype in PCT):
            print("requested distribution of unknown machine type")
            return
        machine_distribution=PCT[machinetype]
        if(not tasktype in machine_distribution):
            print("requested distribution of unknown task type")
            return
        distribution=machine_distribution[tasktype]
        #so... we have it...  ## to do, retry with mutable message?
        SchedulerMsg.Start(msgbuilder)
        SchedulerMsg.AddOperation(msgbuilder,OpType.OpType().time_distribution)
        SchedulerMsg.AddReturnDest(msgbuilder,selfdest)
        SchedulerMsg.AddPriority(msgbuilder,0)
        SchedulerMsg.AddTaskType(msgbuilder,atasktype)
        SchedulerMsg.AddMachineType(msgbuilder,amachinetype)
        #set time distribution...
        #?????
        #
        ####### finally
        themessage=SchedulerMsg.End(msgbuilder)
        #print(themessage)
        msgbuilder.Finish(themessage)
        channel.basic_publish(exchange='', routing_key=QNAME, body=msgbuilder.Output()) #will change qname later, after this test
    elif (aRequest.Operation() ==OpType.OpType.time_learn):
        pass
    else:
        print("unknown request type:"+str(aRequest.Operation()))

        pass



######## Msg handler
def callback(ch, method, properties, body):
    #print(" [x] Received %r" % body)
    #ts = ((time.time())*1000)
    #delay=ts-float(body)
    #print("Received " + str(body) + " at " + str(ts)+ " delay="+str(delay))    
    
    print("Received a message")
    ch.basic_ack(delivery_tag = method.delivery_tag) ## debugging stage, ack first, before parse

    #do time estimator thing to 'body'
    parsedbody = SchedulerMsg.SchedulerMsg.GetRootAs(body,0)
    
    msghandling(parsedbody)


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
