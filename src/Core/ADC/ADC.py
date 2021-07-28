from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
import json # for front end
import flatbuffers # for back end
import cgi
import pika
import MSC_msg.OpType as OpType
import MSC_msg.SchedulerMsg as SchedulerMsg
import os

RMQHOST="rmq"
SENDQNAME="scheduler"
LOGQNAME="logqueue"
MYROLE="AdmissionControl"

user=os.environ['USERNAME']
pswd=os.environ['PASSWORD']
myport=int(os.environ['PORT'])

######### Queue Initialization
thecredential=pika.PlainCredentials(user,pswd)
#print("Connecting to RMQHOST"+)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RMQHOST,credentials=thecredential))
channel = connection.channel()
channel.queue_declare(queue=SENDQNAME)
msgbuilder=flatbuffers.Builder(1024)

class Server(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        # Send allow-origin header for preflight POST XHRs.
        self.send_response(HTTPStatus.NO_CONTENT.value)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST')
        self.send_header('Access-Control-Allow-Headers', 'content-type')
        self.end_headers()

    def _set_headers(self):
        self.send_response(HTTPStatus.OK.value)
        self.send_header('Content-type', 'application/json')
        # Allow requests from any origin, so CORS policies don't
        # prevent local development.
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
    # GET sends back a Hello world message
    def do_GET(self):
        print("Get method")
        self._set_headers()
        self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}))
        
    # POST echoes the message adding a JSON field
    def do_POST(self):
        print("Post method")
        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length))
            
        print(message)

        # add a property to the object, just to mess with data
        message['received'] = 'ok'
        message['returnedurl']='bug'
        
        # send the message back, will move this code up later
        self._set_headers()
        self.wfile.write(json.dumps(message).encode('utf-8'))
        ### now, forward message to scheduler, on RMQ
        atasktype=msgbuilder.CreateString("ffmpeg-1")
        amachinetype=msgbuilder.CreateString("amachinetype")
        
        SchedulerMsg.Start(msgbuilder)
        SchedulerMsg.AddOperation(msgbuilder,OpType.OpType().task_order)
        #SchedulerMsg.AddReturnDest(msgbuilder,selfdest) #no return destination
        SchedulerMsg.AddPriority(msgbuilder,0)
        SchedulerMsg.AddTaskType(msgbuilder,atasktype)
        SchedulerMsg.AddMachineType(msgbuilder,amachinetype)

        #...
        
        themessage=SchedulerMsg.End(msgbuilder)
        msgbuilder.Finish(themessage)
        channel.basic_publish(exchange='', routing_key=SENDQNAME, body=msgbuilder.Output()) #will change qname later, after this test

        
def run(server_class=HTTPServer, handler_class=Server, port=myport):
    server_address = ('', port)
    httpd = HTTPServer(server_address, handler_class)
    
    print ('Starting httpd on port %d...',port);
    httpd.serve_forever()
    
if __name__ == "__main__":
    from sys import argv
    
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
        
