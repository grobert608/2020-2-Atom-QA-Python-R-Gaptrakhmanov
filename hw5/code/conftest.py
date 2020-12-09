import pytest

from orm_client import OrmConnection


@pytest.fixture(scope='session')
def config():
    db_user = 'root'
    db_password = 'password'
    db_name = 'MYSQL_DB'

    return {'db_user': db_user, 'db_password': db_password, 'db_name': db_name}


@pytest.fixture(scope='session')
def orm_client(config):
    return OrmConnection(user=config['db_user'], password=config['db_password'], db_name=config['db_name'])
