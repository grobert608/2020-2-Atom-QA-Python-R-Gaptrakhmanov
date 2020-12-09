from models.models import Base, ClientError, ServerError, BiggestRequest
from orm_client import OrmConnection


class OrmBuilder:

    def __init__(self, connection: OrmConnection):
        self.connection = connection
        self.engine = connection.connection.engine
        self.create_client_errors()
        self.create_server_errors()
        self.create_biggest_requests()

    def create_biggest_requests(self):
        if not self.engine.dialect.has_table(self.engine, 'top_largest'):
            Base.metadata.tables['top_largest'].create(self.engine)

    def create_client_errors(self):
        if not self.engine.dialect.has_table(self.engine, 'top_client_errors'):
            Base.metadata.tables['top_client_errors'].create(self.engine)

    def create_server_errors(self):
        if not self.engine.dialect.has_table(self.engine, 'top_server_errors'):
            Base.metadata.tables['top_server_errors'].create(self.engine)

    def add_biggest_request(self, url, address, size):
        biggest_request = BiggestRequest(
            address=address,
            url=url,
            size=size
        )

        self.connection.session.add(biggest_request)
        self.connection.session.commit()

        return biggest_request

    def add_client_error(self, url, status, count):
        client_error = ClientError(
            url=url,
            status=status,
            count=count
        )

        self.connection.session.add(client_error)
        self.connection.session.commit()

        return client_error

    def add_server_error(self, url, status, count):
        server_error = ServerError(
            url=url,
            status=status,
            count=count
        )

        self.connection.session.add(server_error)
        self.connection.session.commit()

        return server_error
