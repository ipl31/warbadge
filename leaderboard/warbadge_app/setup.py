from setuptools import setup
from pip.req import parse_requirements

setup(
    name='warbdage_app',
    version='1.0',
    long_description=__doc__,
    packages=['warbadge_app'],
    include_package_data=True,
    zip_safe=False,
    install_reqs=parse_requirements('../requirements.txt', session='hack')
)
