from auth.database import User
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData, Column, String, Integer, Table, JSON, ForeignKey
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String(length=100), nullable=False)
    posts = relationship("Comment", back_populates="author")
    