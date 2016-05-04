"""Provides a Flask blueprint for defining Grafana endpoints."""

from __future__ import absolute_import
from flask import Blueprint, json, Response


def make_blueprint(resource):
    """Create the Flask blueprint.

    :param resource: the Grafana JSON resource
    :return: a blueprint

    """
    grafana = Blueprint('grafanajson', __name__)

    @grafana.route('/')
    def index():
        return ''

    @grafana.route('/query')
    def query():
        data = json.dumps(resource.query('abc'))
        return Response(data, mimetype='application/json')

    @grafana.route('/search')
    def search():
        data = json.dumps(resource.search())
        return Response(data, mimetype='application/json')

    return grafana
