import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'

    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String(length=40))
    last_name = sa.Column(sa.String(length=40))
    date_birth = sa.Column(sa.Date)

class Employees(Base):
    id = sa.Column(sa.Integer, primary_key=True)


