from sqlalchemy.orm import Session

import models
import schemas


def create_user(db: Session, data: schemas.UserCreate) -> models.User:
    item = models.User(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def list_users(db: Session) -> list[models.User]:
    return db.query(models.User).order_by(models.User.id).all()


def get_user(db: Session, item_id: int) -> models.User | None:
    return db.query(models.User).filter(models.User.id == item_id).first()


def update_user(db: Session, item: models.User, data: schemas.UserUpdate) -> models.User:
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


def delete_user(db: Session, item: models.User) -> None:
    db.delete(item)
    db.commit()


def create_project(db: Session, data: schemas.ProjectCreate) -> models.Project:
    item = models.Project(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def list_projects(db: Session) -> list[models.Project]:
    return db.query(models.Project).order_by(models.Project.id).all()


def get_project(db: Session, item_id: int) -> models.Project | None:
    return db.query(models.Project).filter(models.Project.id == item_id).first()


def update_project(db: Session, item: models.Project, data: schemas.ProjectUpdate) -> models.Project:
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


def delete_project(db: Session, item: models.Project) -> None:
    db.delete(item)
    db.commit()


def create_task(db: Session, data: schemas.TaskCreate) -> models.Task:
    item = models.Task(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def list_tasks(db: Session) -> list[models.Task]:
    return db.query(models.Task).order_by(models.Task.id).all()


def get_task(db: Session, item_id: int) -> models.Task | None:
    return db.query(models.Task).filter(models.Task.id == item_id).first()


def update_task(db: Session, item: models.Task, data: schemas.TaskUpdate) -> models.Task:
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


def delete_task(db: Session, item: models.Task) -> None:
    db.delete(item)
    db.commit()
