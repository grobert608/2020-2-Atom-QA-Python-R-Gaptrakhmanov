from api.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')
    parser.addoption('--username', default='nocifhcdfkcxtapzqx@avxrja.com')
    parser.addoption('--password', default='Zx123456')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    username = request.config.getoption('--username')
    password = request.config.getoption('--password')

    return {'url': url, 'username': username, 'password': password}
