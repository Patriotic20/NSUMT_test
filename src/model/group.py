from sqlalchemy import Column , Integer , String , ForeignKey
from sqlalchemy.orm import relationship
from src.settings.base import Base
from src.model.teacher_group_association import teacher_group_association


class Group(Base):
    __tablename__ = "groups"
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(25), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    

    subjects = relationship("Subject", back_populates="group", cascade="all, delete")
    students = relationship("Student", back_populates="group", cascade="all, delete")
    department = relationship("Department", back_populates="groups")
    user_tests = relationship("UserTest", back_populates="group")
    teachers = relationship("Teacher", secondary=teacher_group_association, back_populates="groups")
