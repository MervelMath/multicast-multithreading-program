import socket
import sys
import time
import json
from Crypto.Cipher import PKCS1_OAEP
from thread import myThread

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007
thread1 = myThread(1, "Thread-1", 1)
thread1.start()
# regarding socket.IP_MULTICAST_TTL
# ---------------------------------
# for all packets sent, after two hops on the network the packet will not
# be re-sent/broadcast (see https://www.tldp.org/HOWTO/Multicast-HOWTO-6.html)
MULTICAST_TTL = 2

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

# For Python 3, change next line to 'sock.sendto(b"robot", ...' to avoid the
# "bytes-like object is required" msg (https://stackoverflow.com/a/42612820)
while True:
    x =  json.dumps('{ "name": {MCAST_GRP}, "age": "chave"}')
    sock.sendto(bytes(x, encoding="utf-8"), (MCAST_GRP, MCAST_PORT))
    time.sleep(2)



