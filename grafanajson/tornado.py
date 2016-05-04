"""Implementation of request handlers for the Tornado web framework."""

from __future__ import absolute_import
import json
import logging
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    def initialize(self, resource, logger=None):
        """Base handler for Grafana requests.

        :param Resource resource:
        :param str logger:

        """
        self.resource = resource
        logger = logging.getLogger('tornado.application') or logger


class IndexHandler(BaseHandler):
    def get(self):
        return


class SearchHandler(BaseHandler):
    def get(self):
        self.write(json.dumps(self.resource.metrics))


class QueryHandler(RequestHandler):
    def get(self):
        try:
            # res = self.resource.query(self.request.body)
            # print(res)
            # self.write(res)
            pass
        except:
            self.logger.error('Invalid JSON body received: ' + self.request.body)
            return
        self.write('hi')


def add_grafana_handlers(app, resource, prefix='/', host_pattern='.*'):
    """Add request handlers to an existing Tornado app.

    :param tornado.web.Application app:
    :param Resource resource:
    :param str prefix: URL prefix (default: ``'/'``)
    :return: the app with added handlers

    """
    if not prefix.startswith('/'):
        prefix = '/' + prefix
    kwargs = dict(resource=resource)
    app.add_handlers(host_pattern,
                     [(prefix, IndexHandler, kwargs),
                      (prefix + '/search', kwargs),
                      (prefix + '/query', kwargs)])
    return app
