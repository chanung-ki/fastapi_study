from sqlalchemy import Boolean, Column, Integer, String

from .database import Base # database.py 에서 정의한 Base

# DB에 테이블 정의

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    is_active = Column(Boolean, default=True)