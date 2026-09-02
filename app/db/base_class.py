from sqlalchemy import Column,DateTime
from typing import Any
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr

class Base(DeclarativeBase):
    id:Any
    __name__:str


    @declared_attr
    def __tablename(cls)->str:
        return cls.__name__.lower()

    created_at=Column(DateTime,default=datetime.utcnow)
    modefide_at=Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)