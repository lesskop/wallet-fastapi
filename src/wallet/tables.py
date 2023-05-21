from sqlalchemy import Column, Integer, String, Numeric, Date, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(Text, unique=True)
    username = Column(Text, unique=True)
    password_hash = Column(Text)


class Operation(Base):
    __tablename__ = 'operations'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date)
    kind = Column(String)
    amount = Column(Numeric(10, 2))
    description = Column(String, nullable=True)
