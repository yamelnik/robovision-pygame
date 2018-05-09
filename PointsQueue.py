

class PointsQueue(object):
    def __init__(self, queue_max_length):
        super()
        self._queue = []
        self._queue_max_length = queue_max_length

    def put(self, list_of_points):
        self._queue.extend(list_of_points)
        num_of_overflowing_items = len(self._queue) - self._queue_max_length
        if num_of_overflowing_items > 0:
            del self._queue[:num_of_overflowing_items]


    def get(self):
        return self._queue


    def clear(self):
        self._queue = []