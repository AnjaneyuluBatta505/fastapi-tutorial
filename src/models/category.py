from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import INTEGER, VARCHAR, Column, TIMESTAMP, func


Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'
    id = Column('id', INTEGER, primary_key=True)
    name = Column('name', VARCHAR(30), nullable=False)
    description = Column('description', VARCHAR(255))
    timestamp = Column('timestamp', TIMESTAMP, server_default=func.now())
