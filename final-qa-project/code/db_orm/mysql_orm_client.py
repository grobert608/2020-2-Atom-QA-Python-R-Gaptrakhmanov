import sqlalchemy
from sqlalchemy.orm import sessionmaker


class MysqlOrmConnection:

    def __init__(self, user, password, db_name):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = '192.168.0.64'
        self.port = 3306

        self.connection = self.connect()

        session = sessionmaker(bind=self.connection.engine,
                               autocommit=True,
                               autoflush=True,
                               enable_baked_queries=False,
                               expire_on_commit=True)
        self.session = session()

    def get_connection(self, db_created=False):
        engine = sqlalchemy.create_engine(
            'mysql+pymysql://{user}:{password}@{host}:{port}/{db}'.format(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                db=self.db_name if db_created else '')
        )

        return engine.connect()

    def connect(self):
        connection = self.get_connection()
        connection.close()

        return self.get_connection(db_created=True)
