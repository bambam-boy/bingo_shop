from app.db.base_class import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship


class Users(Base):
    id:Mapped[int]=mapped_column(primary_key=True)
    username:Mapped[str]=mapped_column(nullable=False)
    hashed_password:Mapped[str]=mapped_column(nullable=False)
    is_superuser:Mapped[bool]=mapped_column(default=False,nullable=False)
    is_active:Mapped[bool]=mapped_column(default=True,nullable=False)
    products:Mapped[list["Products"]]=relationship(back_populates="users")