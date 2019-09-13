from abc import ABCMeta


class PagedList(list):

    def __init__(self, items, token):
        super(PagedList, self).__init__(items)
        self.token = token


class AbstractStore:
    """
    Abstract class for Backend Storage.
    This class defines the API interface for front ends to connect with various types of backends.
    """

    __metaclass__ = ABCMeta

    def __init__(self):
        """
        Empty constructor for now. This is deliberately not marked as abstract, else every
        derived class would be forced to create one.
        """
        pass

    def log_metric(self, run_id, metric):
        """
        Log a metric for the specified run
        :param run_id: String id for the run
        :param metric: :py:class:`submarine.entities.Metric` instance to log
        """
        pass

    def log_param(self, run_id, param):
        """
        Log a param for the specified run
        :param run_id: String id for the run
        :param param: :py:class:`submarine.entities.Param` instance to log
        """
        pass
