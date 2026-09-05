from typing import TypeVar,Generic
from app.db.session import session_async,engine_async,engine,session
from app.db.base import Base
from pydantic import BaseModel

ModelType=TypeVar("MedelType",bound=Base)
CreatModelType=TypeVar("CreatModelType",bound=BaseModel)
UpdateModelType=TypeVar("UpdateModelType",bound=BaseModel)


class CRUDBase(Generic[ModelType,CreatModelType,UpdateModelType]):
    def __init__(self,model:ModelType):
        self.model=model
