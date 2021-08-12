import sys
import os
import pika
RMQHOST="rmq"
INITQUEUENAME="init_queue"
QUEUENAME="" #will be init through init queue
FEEDBACKQUEUENAME="" #feedback_queue, will init after get the message from INITQUEUENAME 
LOGQNAME="worklogqueue"
MYROLE="Worker"
MYID=0 #todo, read ID

#user=os.environ['USERNAME']
#pswd=os.environ['PASSWORD']
#myport=int(os.environ['PORT'])

RepDir="/share_dir/SVSE/sampleRepo/"
ExpDir="/share_dir/SVSE/sampleOutput/"
def HandlerFn_Cmd(args):
    pass

def HandlerFn_ffmpeg(args):
    pass

SUPPORTEDFN={"cmd":HandlerFn_Cmd,"FFmpeg":HandlerFn_ffmpeg}


if __name__ == "__main__":
    #test list dir in shared folder (to see if we can access)
    print(os.listdir("/repodir"));
    print(os.listdir("/outdir"));
    

    # if len(sys.argv)>2:
    #     print("Overwrite host addr with "+sys.argv[2])
    #     RMQHOST=sys.argv[2]
    # if len(sys.argv)>1:
    #     print("I am worker number "+sys.argv[1])
    #     MYID=int(sys.argv[1])
    
