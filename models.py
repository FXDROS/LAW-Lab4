from database import Base
from sqlalchemy import String, Column, Integer, Identity

class Item(Base):
    __tablename__ = 'item'
    item_id = Column(Integer, Identity(start=1, cycle=True), nullable=False, unique=True, primary_key=True)
    name = Column(String(40), nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Item name={self.name}>"
