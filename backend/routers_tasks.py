from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("", response_model=schemas.TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(data: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, data)


@router.get("", response_model=list[schemas.TaskOut])
def list_tasks(db: Session = Depends(get_db)):
    return crud.list_tasks(db)


@router.get("/{item_id}", response_model=schemas.TaskOut)
def get_task(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_task(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return item


@router.put("/{item_id}", response_model=schemas.TaskOut)
def update_task(item_id: int, data: schemas.TaskUpdate, db: Session = Depends(get_db)):
    item = crud.get_task(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud.update_task(db, item, data)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_task(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Task not found")
    crud.delete_task(db, item)
