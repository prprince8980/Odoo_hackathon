from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db


router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(data: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, data)


@router.get("", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    return crud.list_users(db)


@router.get("/{item_id}", response_model=schemas.UserOut)
def get_user(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_user(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="User not found")
    return item


@router.put("/{item_id}", response_model=schemas.UserOut)
def update_user(item_id: int, data: schemas.UserUpdate, db: Session = Depends(get_db)):
    item = crud.get_user(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db, item, data)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_user(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="User not found")
    crud.delete_user(db, item)
