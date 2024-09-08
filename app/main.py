from fastapi import FastAPI
from app.api.v1.endpoints import tasks, users, events
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["tasks"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(events.router, prefix="/api/v1/events", tags=["events"])

@app.get("/")
async def root():
    return {"message": "Welcome to MindMaple API"}
