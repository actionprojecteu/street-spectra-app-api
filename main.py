from pydantic.types import UUID4
from fastapi import FastAPI, Response
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.exceptions import HTTPException
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

from api.services.app import routers as front_routers
from api.utils.postgres import postgres
from api.config import settings


app = FastAPI()

app.include_router(front_routers.router, prefix="/front/1.0")

app.add_middleware(TrustedHostMiddleware, allowed_hosts=[settings.external_hostname])
app.add_middleware(GZipMiddleware)
app.add_middleware(ProxyHeadersMiddleware, trusted_hosts="*")

@app.get("/info")
def read_root():
    return {"app": "streetspectra-app-api",
            "ver": "0.1.0"}

@app.on_event("startup")
async def startup():
    await postgres.connect()
    print("Connected to DB")


@app.on_event("shutdown")
async def shutdown():
    await postgres.disconnect()
    print("Disconnected from DB")


