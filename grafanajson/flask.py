"""Provides a Flask blueprint for defining Grafana endpoints."""

from __future__ import absolute_import
import json
from flask import Blueprint, jsonify


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
        return jsonify(resource.query('abc'))

    @grafana.route('/search')
    def search():
        return jsonify(resource.search())

    return grafana
