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
