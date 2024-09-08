from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas import task as task_schema
from app.models import task as task_model

router = APIRouter()

@router.post("/", response_model=task_schema.Task)
def create_task(task: task_schema.TaskCreate, db: Session = Depends(get_db)):
    db_task = task_model.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/", response_model=list[task_schema.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = db.query(task_model.Task).offset(skip).limit(limit).all()
    return tasks

# 他のCRUD操作も同様に実装
