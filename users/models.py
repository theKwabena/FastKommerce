from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from config.settings import Base, hash_password, verify_password


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))
    password = Column(String)

    def __init__(self, first_name, last_name, email, password, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = hash_password(password)
