from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/auth", tags=["auth"])
app.include_router(router, prefix="/contacts", tags=["contacts"])
