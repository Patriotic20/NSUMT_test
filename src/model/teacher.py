from sqlalchemy import Column , Integer , String , ForeignKey
from sqlalchemy.orm import relationship
from src.settings.base import Base

class Teacher(Base):
    __tablename__ = "teachers"
    
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    last_name = Column(String(50), nullable=True)
    first_name = Column(String(50), nullable=True)
    patronymic = Column(String(50), nullable=True)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)
    jshir = Column(String(14), unique=True, nullable=True)
    
    department = relationship("Department", back_populates="teachers")
    subjects = relationship("Subject", back_populates="teacher", cascade="all, delete")
    groups = relationship("Group", back_populates="teacher", cascade="all, delete")
    user = relationship("User", back_populates="teacher", uselist=False)
    questions = relationship("Question", back_populates="teacher", cascade="all, delete-orphan")
    

    
    