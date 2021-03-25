from sqlalchemy import Column, Integer, String, TIMESTAMP, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'test_users'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(16), default=None, unique=True)
    password = Column(String(255), nullable=False)
    email = Column(String(64), nullable=False, unique=True)
    access = Column(SMALLINT, default=None)
    active = Column(SMALLINT, default=None)
    start_active_time = Column(TIMESTAMP, default=None)

    def __repr__(self):
        return f"<Log(" \
               f"id='{self.id}'," \
               f"username='{self.username}', " \
               f"password='{self.password}', " \
               f"email='{self.email}', " \
               f"access='{self.access}', " \
               f"active='{self.active}'" \
               f"start_active_time='{self.start_active_time}'" \
               f")>"
