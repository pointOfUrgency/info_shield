from sqlalchemy.orm import Session
from fastapi_users import FastAPIUsers
from . import models, schemas



def get_content(db: Session, content_id: int):
    return db.query(models.Content).filter(models.Content.id == content_id).first()


def get_contents(db:Session):
    return db.query(models.Content).all()


def create_content(db: Session, content: schemas.createContent = schemas.createContent):
    db_content = models.Content(id=content.id, title=content.title, body=content.body, author=content.author)
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content
