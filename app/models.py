from .database import Base
from sqlalchemy import String, Column, Integer, Identity

class Item(Base):
    __tablename__ = 'item'
    item_id = Column(Integer, Identity(start=1, cycle=True), nullable=False, unique=True, primary_key=True)
    name = Column(String(40), nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Item name={self.name}>"

class File(Base):
    __tablename__ = 'file'
    name = Column(String(40), nullable=False, primary_key=True, unique=True)
    filepath = Column(String(500), nullable=False, unique=True)

    def __repr__(self):
        return f"<File name={self.name}>"