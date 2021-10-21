from sqlalchemy import Column, SmallInteger, String

from models.base_model import BaseModel


class User(BaseModel):

    __tablename__ = "user"

    name = Column(String(50), comment="姓名")
    age = Column(SmallInteger, comment="年龄")
