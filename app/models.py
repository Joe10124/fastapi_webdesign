from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

#.表示相對路徑
# Define the database model
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    sort = Column(Integer)
    priority = Column(Integer, default=1)
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primaty = True, index=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=True)
    priority = Column(Integer, default=1)