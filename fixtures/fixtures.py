from behave import fixture
import threading
from wsgiref import simple_server

@fixture
def wsgi_server(context, port=8000):
    pass