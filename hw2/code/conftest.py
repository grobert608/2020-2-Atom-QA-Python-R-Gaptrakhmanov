from ui.fixtures import *
import pytest


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')
    parser.addoption('--username', default='nocifhcdfkcxtapzqx@avxrja.com')
    parser.addoption('--password', default='Zx123456')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--selenoid', default=False)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    username = request.config.getoption('--username')
    password = request.config.getoption('--password')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid')

    return {'browser': browser, 'version': version, 'url': url, 'username': username, 'password': password,
            'selenoid': selenoid}
