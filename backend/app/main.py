from fastapi import FastAPI
from routers import campus, group, teacher

app = FastAPI()

app.include_router(campus.router)
app.include_router(group.router)
app.include_router(teacher.router)