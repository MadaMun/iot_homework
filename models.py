from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    short = Column(String, index=True)
    catagory = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer, index=True)
    is_published = Column(Boolean, index=True)

class Drink(Base):
    __tablename__ = 'drinks'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    menu = Column(String, index=True)
    prics = Column(Integer, index=True)

    
class Order(Base):
    __tablename__ = 'orders'

    drink_id = Column(Integer, ForeignKey('drinks.id'))
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    menu = Column(String, index=True)
    much = Column(Integer, index=True)
    note = Column(String, index=True)

