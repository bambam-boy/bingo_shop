import uuid

from sqlalchemy import Column,Integer,String
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base
# TODO add realation for product images and users 


class Products(Base):
    id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    name=Column(String,nullable=False)
    count=Column(Integer,nullable=False)
    price=Column(Integer,nullable=False)
    