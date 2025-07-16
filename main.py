from fastapi import FastAPI
from config.database import Base, engine
from routers.usuarios import usuarios_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(usuarios_router)


