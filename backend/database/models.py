from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base
from .connectDB import Base, Asanali
from pydantic import BaseModel, validator, root_validator
import bcrypt

class UserCreate(BaseModel):
    email:str
    password: str
    config_password: str
    name: str
    surname: str
    type: str

    @root_validator
    def passwords_match(cls, values):
        pw = values.get('password')
        cpw = values.get('config_password')
        if pw != cpw:
            raise ValueError('Пароли не совпадают')
        return values

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True, nullable=True)
    hashed_password = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    types = Column(String(10))
    created_at = Column(DateTime, server_default=func.now())
