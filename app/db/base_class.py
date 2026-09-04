from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped,mapped_column
from typing import Any
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr

class Base(DeclarativeBase):
    id:Any
    __name__:str


    @declared_attr
    def __tablename__(cls)->str:
        return cls.__name__.lower()

    created_at:Mapped[datetime]=mapped_column(DateTime,nullable=False,default=datetime.utcnow)
    modefide_at:Mapped[datetime]=mapped_column(DateTime,nullable=False,default=datetime.utcnow,onupdate=datetime.utcnow)