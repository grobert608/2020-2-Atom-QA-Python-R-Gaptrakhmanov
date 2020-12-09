import pytest
import time

import requests
from mock_server.http_server import SimpleHTTPServer
from socket_client.http_socket_client import SocketClient
from application import app_server


@pytest.fixture(scope='session')
def config():
    mock_host = '127.0.0.1'
    mock_port = 5000
    app_host = '127.0.0.1'
    app_port = 5001

    return {'mock_host': mock_host, 'mock_port': mock_port, 'app_host': app_host, 'app_port': app_port}


@pytest.fixture(scope='session')
def mock_server(config):
    server = SimpleHTTPServer(config['mock_host'], config['mock_port'])
    server.start()
    yield server
    server.stop()


@pytest.fixture(scope='session')
def socket_client(config):
    time.sleep(1)
    return SocketClient(config['app_host'], config['app_port'])


@pytest.fixture(scope='session')
def socket_client_mock(config):
    time.sleep(1)
    return SocketClient(config['mock_host'], config['mock_port'])


@pytest.fixture(scope='session')
def mock(config, mock_server):
    app_server.run_app(config['app_host'], config['app_port'])
    yield
    requests.get(f'http://{config["app_host"]}:{config["app_port"]}/shutdown')
