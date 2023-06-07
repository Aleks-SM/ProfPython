from sqlalchemy import Column, VARCHAR, Integer, ForeignKey
from .base import BaseModel

class Department(BaseModel):
  __tablename__ = 'departmens'
  
  name = Column(VARCHAR(100), nullable=False)

class EmployeeDepartments(BaseModel):
  __tablename__ = 'employee_departments'
  
  employee_id = Column(Integer, ForeignKey('employees.id', nullable=False))
  deppartment_id = Column(Integer, ForeignKey('departments.id', nullable=False))
