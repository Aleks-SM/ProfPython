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
    dsn = "{}://{}:{}@localhost:{}/{}".format(self.bd, self.bd_username, self.bd_pass, self.bd_port, self.bd_name)
  return dsn

  def create_tables(self, engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
