from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ClientError(Base):
    __tablename__ = 'top_client_errors'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(50), nullable=False)
    status = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Log(" \
               f"id='{self.id}'," \
               f"url='{self.url}'" \
               f"status='{self.status}', " \
               f"count='{self.count}'" \
               f")>"


class ServerError(Base):
    __tablename__ = 'top_server_errors'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(50), nullable=False)
    status = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Log(" \
               f"id='{self.id}'," \
               f"url='{self.url}'" \
               f"status='{self.status}', " \
               f"count='{self.count}'" \
               f")>"


class BiggestRequest(Base):
    __tablename__ = 'top_largest'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    method = Column(String(10), nullable=False)
    url = Column(String(50), nullable=False)
    address = Column(String(40), nullable=False)
    size = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Log(" \
               f"id='{self.id}'," \
               f"address='{self.address}', " \
               f"method='{self.method}', " \
               f"url='{self.url}'" \
               f"size='{self.size}'" \
               f")>"
