import json
from robotClient import CLIENT


def get_points():
    data = CLIENT.recv(1024)
    decoded_data = data.decode()
    return json.loads(decoded_data)