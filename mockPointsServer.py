from __future__ import print_function
import socket
import json

TCP_HOST = "localhost"
TCP_PORT = 8070
BUFFER_SIZE = 1024
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((TCP_HOST, TCP_PORT))
SERVER.listen(1)

POINTS = [
    {"p": {"a": 45, "d": 20}},
    {"p": {"a": 46, "d": 20}},
    {"p": {"a": 45, "d": 21}},
    {"p": {"a": 45, "d": 22}},
]

mainloop = True

while mainloop:
    conn, addr = SERVER.accept()
    print("Accepted connection from: ", addr[0], ":", addr[1])
    try:
        conn.sendall(json.dumps(POINTS).encode())
    except KeyboardInterrupt:
        mainloop = False
    except Exception as ex:
        if type(ex) != ConnectionResetError:
            raise
    conn.close()
