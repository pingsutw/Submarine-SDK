from submarine.entities._submarine_object import _SubmarineObject


class Param(_SubmarineObject):
    """
    Parameter object.
    """

    def __init__(self, key, value, worker_index):
        self._key = key
        self._value = value
        self._worker_index = worker_index

    @property
    def key(self):
        """String key corresponding to the parameter name."""
        return self._key

    @property
    def value(self):
        """String value of the parameter."""
        return self._value

    @property
    def worker_index(self):
        """String value of the parameter."""
        return self._worker_index
