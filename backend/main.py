from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
import models
import routers_users
import routers_tasks
import routers_projects


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers_users.router)
app.include_router(routers_tasks.router)
app.include_router(routers_projects.router)


@app.get("/health")
def health():
    return {"status": "ok"}
