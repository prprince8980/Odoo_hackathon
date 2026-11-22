from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db


router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("", response_model=schemas.ProjectOut, status_code=status.HTTP_201_CREATED)
def create_project(data: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db, data)


@router.get("", response_model=list[schemas.ProjectOut])
def list_projects(db: Session = Depends(get_db)):
    return crud.list_projects(db)


@router.get("/{item_id}", response_model=schemas.ProjectOut)
def get_project(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_project(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return item


@router.put("/{item_id}", response_model=schemas.ProjectOut)
def update_project(item_id: int, data: schemas.ProjectUpdate, db: Session = Depends(get_db)):
    item = crud.get_project(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return crud.update_project(db, item, data)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_project(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Project not found")
    crud.delete_project(db, item)
