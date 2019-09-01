from submarine.entities._submarine_object import _SubmarineObject


class Metric(_SubmarineObject):
    """
    Metric object.
    """

    def __init__(self, key, value, worker_index, timestamp, step):
        self._key = key
        self._value = value
        self._worker_index = worker_index
        self._timestamp = timestamp
        self._step = step

    @property
    def key(self):
        """String key corresponding to the metric name."""
        return self._key

    @property
    def value(self):
        """Float value of the metric."""
        return self._value

    @property
    def worker_index(self):
        """Float value of the metric."""
        return self.worker_index

    @property
    def timestamp(self):
        """Metric timestamp as an integer (milliseconds since the Unix epoch)."""
        return self._timestamp

    @property
    def step(self):
        """Integer metric step (x-coordinate)."""
        return self._step
