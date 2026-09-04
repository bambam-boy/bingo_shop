from uuid import UUID,uuid4

from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy.dialects.postgresql import UUID as DB_UUID
from app.db.base_class import Base
from sqlalchemy import ForeignKey

class Products(Base):
    id:Mapped[UUID]=mapped_column(DB_UUID(as_uuid=True),primary_key=True,default=uuid4)
    name:Mapped[str]=mapped_column(nullable=False)
    count:Mapped[int]=mapped_column(nullable=False)
    price:Mapped[int]=mapped_column(nullable=False)
    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"))
    user:Mapped["Users"]=relationship(back_populates="products")
    