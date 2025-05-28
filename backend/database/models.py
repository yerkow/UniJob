from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, Float, JSON, Boolean
from sqlalchemy.orm import relationship
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
    student = relationship("Student", back_populates="user", uselist = False)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    short_about = Column(String(255))          
    region = Column(String(100))               
    city = Column(String(100))                 
    birth_date = Column(String(20))            
    gender = Column(String(10))                
    phone = Column(String(30))                               
    desired_salary = Column(Integer)          
    about = Column(String(1000))               
    about_prof = Column(String(1000))          
    work_experience = Column(String(1000))     
    achievements = Column(String(1000))        
    education_level = Column(String(100))
    education_area = Column(String(255))       
    direction_name = Column(String(255))       
    specialization = Column(String(255))       
    skills = Column(String(1000))              
    languages = Column(String(255))
    # Остальные поля, если нужны
    user = relationship("User", back_populates="student", uselist=False)
    
class Universities(Base):
    __tablename__ = "universities"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique= True, index= True, nullable= True)
    city = Column(String, nullable=False)
    region = Column(String)  # например: Южный Казахстан
    country = Column(String, default="Казахстан")
    ownership_type = Column(String(20))  # например: 'государственный', 'частный'
    created_at = Column(DateTime, server_default=func.now())

