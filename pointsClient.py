import socket
import json

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_HOST = "127.0.0.1"
TCP_PORT = 8082
BUFFER_SIZE = 1024

CLIENT.connect((TCP_HOST, TCP_PORT))


def get_points():
    CLIENT.send(b'a')
    data = CLIENT.recv(1024)
    decoded_data = data.decode()
    return json.loads(decoded_data)