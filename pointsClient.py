import json, re
from robotClient import CLIENT

BUFFER_SIZE = 4096

def get_points():
    data = CLIENT.recv(BUFFER_SIZE)
    decoded_data = data.decode()
    all_arrays = re.findall("(\[.+?\])", decoded_data)
    all_arrays_marshalled = [json.loads(array) for array in all_arrays]
    flat_array = [item for sublist in all_arrays_marshalled for item in sublist]
    point_objects = [item["p"] for item in flat_array]
    converted_data = [(datum["a"], datum["d"]) for datum in point_objects]
    return converted_data