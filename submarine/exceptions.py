

class SubmarineException(Exception):
    """
    Generic exception thrown to surface failure information about external-facing operations.
    """
    def __init__(self, message):
        """
        :param message: The message describing the error that occured.
        """
        self.message = message
        super(SubmarineException, self).__init__(message)
