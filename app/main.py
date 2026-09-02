from fastapi import FastAPI
from app.core.config import settings

app=FastAPI(
    title=settings.PORJECT_NAME,
    version=settings.PORJECT_VERSION,
    openapi_url=f"{settings.API_URL}/openapi.json"
)