import os.path
from setuptools import setup
from grafanajson import __version__


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as fp:
        return fp.read()

setup(
    name="grafanajson",
    version=__version__,
    author="Michael V. DePalatis",
    author_email="mike@depalatis.net",
    description="Feed data via JSON into Grafana dashboards",
    # long_description=read('README.rst'),
    # license="",
    keywords="grafana http json api metrics analytis data",
    # url="https://bitbucket.org/iontrapgroup/brush",
    # install_requires=requirements,
    packages=['grafanajson']
)
