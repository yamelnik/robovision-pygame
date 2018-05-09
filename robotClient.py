import socket

TCP_HOST = "192.168.137.81"
TCP_PORT = 8070
BUFFER_SIZE = 1024

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT.connect((TCP_HOST, TCP_PORT))