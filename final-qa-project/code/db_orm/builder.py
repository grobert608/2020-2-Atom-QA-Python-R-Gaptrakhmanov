from sqlalchemy.exc import InvalidRequestError, SQLAlchemyError

from db_orm.models.models import Base, User
from db_orm.mysql_orm_client import MysqlOrmConnection


class DeleteException(Exception):
    pass


class BlockException(Exception):
    pass


class MysqlOrmBuilder:

    def __init__(self, connection: MysqlOrmConnection):
        self.connection = connection
        self.engine = connection.connection.engine
        self.create_test_users()

    def create_test_users(self):
        if not self.engine.dialect.has_table(self.engine, 'test_users'):
            Base.metadata.tables['test_users'].create(self.engine)

    def add_user(self, username, password, email):
        user = User(
            username=username,
            password=password,
            email=email
        )

        self.connection.session.add(user)

        return user

    def delete_user_by_username(self, username):
        try:
            self.connection.session.query(User).filter(User.username == username).delete()
        except SQLAlchemyError:
            raise DeleteException

    def delete_user_by_email(self, email):
        try:
            self.connection.session.query(User).filter(User.email == email).delete()
        except SQLAlchemyError:
            raise DeleteException

    def block_user(self, username):
        try:
            self.connection.session.query(User).filter(User.username == username) \
                .update({User.access: User.access == 0}, synchronize_session=False)
            self.connection.session.commit()
        except SQLAlchemyError:
            raise BlockException

    def unblock_user(self, username):
        try:
            self.connection.session.query(User).filter(User.username == username) \
                .update({User.access: User.access == 1}, synchronize_session=False)
            self.connection.session.commit()
        except SQLAlchemyError:
            raise BlockException
