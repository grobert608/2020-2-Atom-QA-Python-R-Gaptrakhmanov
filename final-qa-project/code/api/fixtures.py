import pytest

from api.client import Client


@pytest.fixture(scope='function')
def api_client(config, add_user):
    name, email = add_user
    return Client(name, config['default_password'])
