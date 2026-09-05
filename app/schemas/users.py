from pydantic import BaseModel,EmailStr


class UserBase(BaseModel):
    username:str | None=None
    email:EmailStr | None=None
    password:str | None=None
    is_active:bool=True
    is_superuser:bool =False

class UserCreat(UserBase):
    username:str
    email:EmailStr
    password:str

class UserUpdate(UserBase):
    username:str | None=None
    email:str | None=None
    password:str | None=None
    