from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base
from .connectDB import Base, Asanali
from pydantic import BaseModel, validator, ValidationError
import bcrypt

class UserCreate(BaseModel):
    name: str
    email:str
    password: str
    config_password: str

    @validator('config_password')
    def checkPassword(cls, value, values):
        if('password' in value and value != values):
            raise ValidationError("Пароли не совподают")
        return value

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True, nullable=True)
    hashed_password = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    created_at = Column(DateTime, server_default=func.now())
