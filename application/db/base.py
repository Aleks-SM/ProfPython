from sqlalchemy.orm import Session

from application.db.models.base import BaseModel

class DBSession():
  
  def __init__(self):
    self.session = session
  
  def query(self):
    return self.session.query()
  
  def commit_session(self, close: bool = False):
    self.session.commit()
    if close:
      self.close.session()
 
  def close_session(self):
      self.session.close()

  def create_conect(self):
    dsn = "{}://{}:{}@{}:{}/{}".format(self.database, self.database_username, self.database_pass, self.database_host self.database_port, self.database_name)
    session = sessionmaker()
    db_session = DBSession()
  return dsn

  def create_tables(self, engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
