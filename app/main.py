from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from .database import Base, engine, SessionLocal
from .models import Todo
from .schemas import TodoBase, TodoCreate, TodoResponse
from .routers import router

#Initialize FastAPI
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

#Register Router
app.include_router(router=router, prefix="/api",tags=["Todos"])