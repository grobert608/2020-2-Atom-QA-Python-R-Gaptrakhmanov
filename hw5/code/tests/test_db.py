import pytest

from models.models import ClientError, ServerError, BiggestRequest
from parsers.parser import Parser
from tests.builder import OrmBuilder


class TestOrmMysql:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, orm_client):
        self.bd = orm_client
        self.builder = OrmBuilder(orm_client)
        self.parser = Parser()
        self.biggest_request, self.client_error, self.server_error = self.parser.parse_logs(log_path='access.log',
                                                                                            result='access.log',
                                                                                            save_bd=True)

    def test_biggest_request_insert(self):
        for biggest_request in self.biggest_request:
            splitted = biggest_request[1].split()
            self.builder.add_biggest_request(splitted[0], splitted[2], biggest_request[0])

        res = self.bd.session.query(BiggestRequest).all()
        if len(self.biggest_request) > 10:
            assert len(res) == 10
        else:
            assert len(res) == len(self.biggest_request)

    def test_client_error_insert(self):
        for client_error in self.client_error:
            self.builder.add_client_error(client_error[0].split(sep=':')[0],
                                          int(client_error[0].split(sep=':')[1]),
                                          client_error[1])

        res = self.bd.session.query(ClientError).all()
        if len(self.client_error) > 10:
            assert len(res) == 10
        else:
            assert len(res) == len(self.client_error)

    def test_server_error_insert(self):
        for server_error in self.server_error:
            self.builder.add_server_error(server_error[0].split(sep=':')[0],
                                          int(server_error[0].split(sep=':')[1]),
                                          server_error[1])

        res = self.bd.session.query(ServerError).all()
        if len(self.server_error) > 10:
            assert len(res) == 10
        else:
            assert len(res) == len(self.server_error)
