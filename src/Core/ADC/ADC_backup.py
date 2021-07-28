from http.server import BaseHTTPRequestHandler, HTTPServer
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
        self._set_headers()
        self.send_response(200, "ok")       
        self.send_header('Access-Control-Allow-Origin', '*')                
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")        
        self.end_headers()

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-Type") 
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_HEAD(self):
        print("Header method")
        self._set_headers()
        
    # GET sends back a Hello world message
    def do_GET(self):
        print("Get method")
        self._set_headers()
        self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}))
        
    # POST echoes the message adding a JSON field
    def do_POST(self):
        print("Post method")
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        
        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return
            
        # read the message and convert it into a python dictionary
        length = int(self.headers.getheader('content-length'))
        message = json.loads(self.rfile.read(length))
        print(message)

        # add a property to the object, just to mess with data
        message['received'] = 'ok'
        message['returnedurl']='bug'
        
        # send the message back, will move this code up later
        self._set_headers()
        self.wfile.write(json.dumps(message))
        ### now, forward message to scheduler, on RMQ
        #SchedulerMsg.Start(msgbuilder)
        #SchedulerMsg.AddOperation(msgbuilder,OpType.OpType().time_distribution)
        #...
        themessage=SchedulerMsg.End(msgbuilder)
        msgbuilder.Finish(themessage)
        channel.basic_publish(exchange='', routing_key=SENDQNAME, body=msgbuilder.Output()) #will change qname later, after this test

        
def run(server_class=HTTPServer, handler_class=Server, port=myport):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    print ('Starting httpd on port %d...',port);
    httpd.serve_forever()
    
if __name__ == "__main__":
    from sys import argv
    
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
        
