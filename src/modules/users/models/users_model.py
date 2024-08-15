from sqlalchemy import Column, BigInteger, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

from src.project_helpers.functions.generate_functions import hash_password

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    unhashed_password = ""
    id = Column(BigInteger, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    _password = Column(String(300), nullable=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self.unhashed_password = value
        self._password = hash_password(value)
