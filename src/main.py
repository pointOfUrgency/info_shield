from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from auth.database import User
from auth.manager import get_user_manager
from auth.authBackend import auth_backend
from auth.schema import UserCreate, UserRead
from content.database import SessionLocal, engine
from sqlalchemy.orm import Session
from content import schemas, CRUD
from fastapi import Depends, FastAPI, HTTPException


app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/content/{content_id}", response_model=schemas.GetContent)
def get_content(content_id: int, db: Session = Depends(get_db)):
    content = CRUD.get_content(db, content_id=content_id)
    if content is None:
        raise HTTPException(status_code=400, detail="This post does not exist")
    return content


@app.get("/contents", response_model=list[schemas.GetContent])
def get_contents(db: Session = Depends(get_db)):
    contents = CRUD.get_contents(db)
    return contents

current_user = fastapi_users.current_user(active=True, superuser=True)
current_user2 = fastapi_users.current_user(active=True)

@app.get("/user")
def get_current_user(user: User = Depends(current_user), db: Session = Depends(get_db)):
    return {"user": user.id}


@app.post("/content", response_model=schemas.GetContent)
def create_content(content: schemas.createContent = schemas.createContent, db: Session = Depends(get_db), user: User = Depends(current_user)):
    db_content = CRUD.get_content(db, content_id=content.id)
    if db_content:
        raise HTTPException(status_code=400, detail="This post already exists")
    return CRUD.create_content(db=db, content=content)

