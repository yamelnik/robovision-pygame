from __future__ import print_function
import socket
import json

TCP_HOST = "127.0.0.1"
TCP_PORT = 8082
BUFFER_SIZE = 1024
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((TCP_HOST, TCP_PORT))
SERVER.listen(1)

POINTS = [
    {"x": 20, "y": 20}
]

mainloop = True

while True:
    conn, addr = SERVER.accept()
    print("Accepted connection from: ", addr[0], ":", addr[1])
    while 1:
        try:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(json.dumps(POINTS).encode())
        except KeyboardInterrupt:
            mainloop = False
        except Exception as ex:
            if type(ex) != ConnectionResetError:
                raise
    conn.close()