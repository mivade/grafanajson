import json
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.log import enable_pretty_logging
from grafanajson import Resource
from grafanajson.frameworks.tornado import add_grafana_handlers


class TestResource(Resource):
    """Basic test resource to return random values."""
    def query(self, body):
        try:
            q = json.loads(body)
        except ValueError:
            raise ValueError('body must be JSON-decodable')
        result = json.dumps([
            {
                "target": "upper_75",
                "datapoints": [[622, 1450754160000], [365, 1450754220000]]
            },
            {
                "target": "upper_90",
                "datapoints": [[861, 1450754160000], [767, 1450754220000]]
            }
        ])
        return result


class IndexHandler(RequestHandler):
    def get(self):
        self.write('Try <a href="/grafana">/grafana</a>')


if __name__ == "__main__":
    enable_pretty_logging()
    app = Application(
        [(r'/', IndexHandler)],
        debug=True)
    resource = TestResource(['a', 'b', 'c'])
    add_grafana_handlers(app, resource, prefix='/grafana')
    print(app.handlers)
    app.listen(5839)
    IOLoop.current().start()
