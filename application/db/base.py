import os

import sqlalchemy as sq
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, Session
from .models.base import Base

class DBSession:
    def __init__(self, session: Session):
        dotenv_path = os.path.join(os.path.dirname(__file__), '.envrc')
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
        self.database = os.getenv('database')
        self.database_host = os.getenv('database_host')
        self.database_port = os.getenv('database_port')
        self.database_name = os.getenv('database_name')
        self.database_username = os.getenv('database_username')
        self.database_pass = os.getenv('database_pass')
        self.file_name = os.getenv('file_name')
        self.paths = os.path.join(os.getcwd(), self.file_name)

  
    def query(self):
      return self.session.query()

    def commit_session(self, close: bool = False):
      self.session.commit()
      if close:
        self.close_session()

    def close_session(self):
        self.session.close()

    def create_conect(self):
        DSN = "{}://{}:{}@{}:{}/{}".format(self.database, self.database_username, self.database_pass, self.database_host, self.database_port, self.database_name)
        engine = sq.create_engine(DSN)
        Session = sessionmaker(bind=engine)
        db_session = Session()
        return db_session

    def create_tables(self, engine):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
