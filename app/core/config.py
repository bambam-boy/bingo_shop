from pydantic_settings import BaseSettings,SettingsConfigDict
from typing import Optional
from pydantic import ValidationInfo,field_validator,PostgresDsn

class Settings(BaseSettings):
    POSTGRES_USERNAME:str
    POSTGRES_PASSWORD:str
    POSTGRES_HOST:str
    POSTGRES_PORT:str
    POSTGRES_DB:str

    PORJECT_NAME:str="BINGO SHOP"
    PORJECT_VERSION:str="0.1.0"
    API_URL:str="/api/v1"

    SQLALCHEMY_DATABASE_URI:Optional[str]=""

    @field_validator("SQLALCHEMY_DATABASE_URI",mode="before")
    @classmethod
    def attach_db_url(cls,v:Optional[str]|None,values:ValidationInfo):
        if not v is None and not v=="":
            return v
        datas=values.data
        url=PostgresDsn.build(
            scheme="postgresql",
            username=datas.get("POSTGRES_USERNAME"),
            password=datas.get("POSTGRES_PASSWORD"),
            host=datas.get("POSTGRES_HOST"),
            port=int(datas.get("POSTGRES_PORT")),
            path=datas.get("POSTGRES_DB")
        ).encoded_string()

        return url

    SQLALCHEMY_DATABASE_URI_ASYNC:Optional[str]=""

    @field_validator("SQLALCHEMY_DATABASE_URI_ASYNC",mode="before")
    @classmethod
    def attach_db_url_async(cls,v:Optional[str]|None,values:ValidationInfo):
        if not v is None and not v=="":
            return v
        datas=values.data
        url=PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=datas.get("POSTGRES_USERNAME"),
            password=datas.get("POSTGRES_PASSWORD"),
            host=datas.get("POSTGRES_HOST"),
            port=int(datas.get("POSTGRES_PORT")),
            path=datas.get("POSTGRES_DB")
        ).encoded_string()

        return url    


    model_config=SettingsConfigDict(env_file=".env")

settings=Settings()