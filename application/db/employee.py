import sqlalchemy as sa
from .base import BaseModel


class Employee(BaseModel):
    __tablename__ = 'employees'

    first_name = sa.Column(sa.String(length=40))
    last_name = sa.Column(sa.String(length=40))
    date_birth = sa.Column(sa.Date)
    
    def __repr__(self):
        res = '{} {}'.format(self.first_name, self.last_name)
        return res
