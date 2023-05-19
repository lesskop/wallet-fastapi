from sqlalchemy import Column, Integer, String, Numeric, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Operation(Base):
    __tablename__ = 'operations'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    kind = Column(String)
    amount = Column(Numeric(10, 2))
    description = Column(String, nullable=True)