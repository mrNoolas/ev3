from utils import utils
from vitals import vitals
from checkColor import checkColor
from movement import movement
from threading import Thread
from doMovements import doMovements
from time import sleep
from receiveMessage import receiveMessage
import bluetooth

server_mac = 'CC:78:AB:50:B2:46'

def main():
    u = utils()
    v = vitals(u)
    m = movement(v, u) 
    
    move = doMovements(v,m)
    c = checkColor(u)
    r = receiveMessage(u, c)
    
    behaviors = [move,r,c]
    runBluetooth(behaviors)
    print("Shutting down...")
    return 0
   
    
def connect():
    port = 3
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind((server_mac, port))
    server_sock.listen(1)
    print('MASTER: Listening...')
    client_sock, address = server_sock.accept()
    print('MASTER: Accepted connection from ', address)
    return client_sock, client_sock.makefile('r'), client_sock.makefile('w')

def runBluetooth(behaviors):
    sock, sock_in, sock_out = connect()
    listener = Thread(target=listen, args=(sock_in, sock_out, behaviors))
    listener.start()
    sender = Thread(target=send, args=(sock_in, sock_out, behaviors))
    sender.start()
    Thread(target=go, args=[behaviors]).start()
    Thread(target=doAction, args=[behaviors]).start() 
    while not behaviors[2].foundAllColors:
        sleep(1)
    
    
    sock_out.close()
    sock.close()
    sock_in.close()
    
    
def listen(sock_in, sock_out, behaviors):
    print('MASTER: Now listening...')
    while not behaviors[2].foundAllColors:
        data = int(sock_in.readline())
        print('MASTER: Received ' + str(data))
        behaviors[1].receivedColor = data
        behaviors[1].user = "Master"
        behaviors[1].receivedMessage = True
            
def send(sock_in, sock_out, behaviors):
    while not behaviors[2].foundAllColors:
        if behaviors[2].readyToSend:
            print("MASTER: Ready to send!")
            sock_out.write(str(behaviors[2].lastColor) + '\n')
            sock_out.flush()
            print('MASTER: Sent ' + str(behaviors[2].lastColor))
            behaviors[2].readyToSend = False
        
def go(behaviors):
    activeBehavior = 0 #Standard = movement
    highest = 0 #Standard = movement
    behaviors[highest].active = True
    while not behaviors[2].foundAllColors: 
        #print("MASTER: Current running behavior " + str(activeBehavior))
        #print("Colors to be checked:")
        #print(behaviors[1].colorsToFind)
        for i in range(len(behaviors)-1, -1, -1):
            if i > activeBehavior:
                if behaviors[i].takeControl() and behaviors[activeBehavior].active:
                    print("MASTER: Behavior " + str(i) + " wants to take control!")
                    print("MASTER: Suppressing behavior " + str(activeBehavior))
                    behaviors[activeBehavior].suppress()
                    print("MASTER: Starting behavior " + str(i))
                    behaviors[i].suppressed = False
                    behaviors[i].active = True
                    activeBehavior = i
            elif not behaviors[activeBehavior].active:
                #No behavior is running, thus the highest can be started. 
                if behaviors[i].takeControl():
                    print("MASTER: Starting behavior " + str(i))
                    behaviors[i].suppressed = False
                    behaviors[i].active = True
                    activeBehavior = i
        sleep(0.1)
                    
def doAction(behaviors):
    while not behaviors[2].foundAllColors:
        for i in range(len(behaviors)-1, -1, -1): 
            if behaviors[i].active:
                #print("MASTER: Thread runs behavior " + str(i))
                behaviors[i].action();
    
main()
