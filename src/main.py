from fastapi import FastAPI
from .routers import category


app = FastAPI()
app.include_router(category.router)
