import sys
sys.path.append("../")

import socket
from proto import request_pb2

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 9999
s.connect((host, port))
request = request_pb2.request()
request.type = 4
request.expressCom = "YTO"
request.expressCode = "13214124315"
data = request.SerializeToString()
s.send(data)
msg = s.recv(1024)
s.close()
print(msg.decode("utf-8"))

