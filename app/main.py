from fastapi import FastAPI, Depends, HTTPException
from .database import Base, engine, SessionLocal
from .routers import router

#Initialize FastAPI
app = FastAPI()

# Create database tables
# Base.metadata.create_all(bind=engine)

#Register Router
app.include_router(router=router, prefix="/api",tags=["Todos"])