import socket, json

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_HOST = "127.0.0.1"
TCP_PORT = 8070
BUFFER_SIZE = 1024

CLIENT.connect((TCP_HOST, TCP_PORT))


def get_robot_connection():
    return CLIENT


def disconnect():
    CLIENT.close()


def send_movement(leftEngine, rightEngine):
    if leftEngine or rightEngine:
        client = get_robot_connection()
        data = [{"l": leftEngine}, {"r": rightEngine}]
        json_data = json.dumps(data).encode()
        client.send(json_data)
