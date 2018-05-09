import json
from robotClient import CLIENT


def get_robot_connection():
    return CLIENT


def disconnect():
    CLIENT.close()


def send_movement(leftEngine, rightEngine):
    client = get_robot_connection()
    data = [{"l": leftEngine}, {"r": rightEngine}]
    json_data = json.dumps(data).encode()
    client.send(json_data)
