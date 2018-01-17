import socket
from proto import request_pb2

global host
global server_socket


def start_host(port):
    global host, server_socket
    try:
        host = "127.0.0.1"
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(10)
        print(str.format("start server success, host{}, port{}", host, port))
    except RuntimeError:
        print("初始化服务器失败")


def accept():
    global server_socket
    if (server_socket == None):
        print("server_socket is None")
    return server_socket.accept()


def get_request(client):
    if client is None:
        return None
    recv_msg = b""
    tmp_msg = client.recv(1024)
    recv_msg = recv_msg + tmp_msg
    print(str.format("read_from_client,data is [{}]", recv_msg))
    request = request_pb2.request()
    request.ParseFromString(recv_msg)
    return request


