import json


class Resource(object):
    """Base resource class. Override the :meth:`query` and
    :meth:`annotations` methods to get data from your own backends.

    :param list metrics: list of available metrics

    """
    def __init__(self, metrics):
        self.metrics = metrics

    def search(self):
        """Returns the list of metrics."""
        return self.metrics

    def query(self, body):
        """Override this method to return the results of the query."""
        raise NotImplementedError

    def annotations(self, body):
        """Override this method to return annotations."""
        raise NotImplementedError
