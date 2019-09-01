from submarine.entities._submarine_object import _SubmarineObject


class Param(_SubmarineObject):
    """
    Parameter object.
    """

    def __init__(self, key, value):
        self._key = key
        self._value = value

    @property
    def key(self):
        """String key corresponding to the parameter name."""
        return self._key

    @property
    def value(self):
        """String value of the parameter."""
        return self._value