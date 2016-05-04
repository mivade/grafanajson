import json
from flask import Flask, jsonify
from grafanajson import Resource
from grafanajson.flask import make_blueprint

class TestResource(Resource):
    """Basic test resource to return random values."""
    def query(self, body):
        try:
            q = json.loads(body)
        except ValueError:
            raise ValueError('body must be JSON-decodable')
        result = jsonify([
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

app = Flask(__name__)
app.debug = True
blueprint = make_blueprint(TestResource(['a', 'b', 'c']))
app.register_blueprint(blueprint, url_prefix='/grafana')

@app.route('/')
def index():
    return 'Try <a href="/grafana">/grafana</a>!'

app.run()
