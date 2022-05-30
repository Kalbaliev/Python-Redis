import redis
import time
import sys
import ast

r = redis.Redis(host='localhost', port=6379, db=0)

def subscribeChannel(channels):
    p = r.pubsub()
    p.subscribe(channels)

    while True:
        message = p.get_message()
        if message:
            print(message)
        time.sleep(0.01)

def publishChannel(channel,msg):
    r.publish(channel, msg)



if __name__ == "__main__":
    args = sys.argv

    
    if args[1]=='subscribeChannel':
        
        args[2]=bytes(args[2],"utf-8")
        args[2] = args[2].decode("UTF-8")
        args[2]= ast.literal_eval(args[2])
        for channel in args[2]:
            print(f"subscribed to : {channel}\n")
        globals()[args[1]](args[2])

    elif args[1]=='publishChannel':
        print(f"Published Message : {args[3]}")
        globals()[args[1]](args[2],args[3])

    