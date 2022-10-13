# an example of an sql alchemy model - how to define our tables using a python class

import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db

# table and table fields
class Organizations(db.Model):
  __tablename__='organizations'
  org_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  name = db.Column(db.String(), nullable=False, unique=True)
  phone = db.Column(db.String())
  city = db.Column(db.String())
  state = db.Column(db.String())
  active = db.Column(db.Boolean(), default=True)
  # backref joins automatically between users and orgs
  users = db.relationship('Users', backref='organization', lazy=True)

# how to set values on table fields
  def __init__(self, name, phone, city, state, active):
    self.name = name
    self.phone = phone
    self.city = city
    self.state = state
    self.active = active