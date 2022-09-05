import socket
import struct
import json
import threading
import time

class myThread (threading.Thread):
            
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        if self.counter is 1:
            listen(self)

        elif self.counter is 2:
            send(self)
        # print ("Starting " + self.name)

def print_time(threadName, counter, delay):
    while counter:
        # if exitFlag:
        #     threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

def listen(self):
        MCAST_GRP = '224.1.1.2'
        MCAST_PORT = 5007
        IS_ALL_GROUPS = True

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if IS_ALL_GROUPS:
            # on this port, receives ALL multicast groups
            sock.bind(('', MCAST_PORT))
        else:
            # on this port, listen ONLY to MCAST_GRP
            sock.bind((MCAST_GRP, MCAST_PORT))
        mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        while True:
            print(json.loads(sock.recv(10240)))


def send(self):
        MCAST_GRP = '224.1.1.2'
        MCAST_PORT = 5007
        MULTICAST_TTL = 2

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)
        while True:
            x =  json.dumps('{ "Servidor": O servidor está escutando!}')
            sock.sendto(bytes(x, encoding="utf-8"), (MCAST_GRP, MCAST_PORT))
            time.sleep(2)