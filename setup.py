from setuptools import setup, find_packages
import sys

VERSION = '0.7.4'

setup(name = 'httplib2',
      version = VERSION,
      description = 'A comprehensive HTTP client library.',
      license = 'MIT License',
      author = 'Joe Gregorio',
      author_email = 'joe@bitworking.org',
      url = 'http://github.com/bryanhelmig/httplib2',
      packages = find_packages(),
      keywords = 'httplib2 http certs'
)
