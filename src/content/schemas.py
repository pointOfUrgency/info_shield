from pydantic import BaseModel
from datetime import datetime


class GetContent(BaseModel):
    id: int
    title: str
    body: str
    photo_name: str
    author: str 
    date_time: datetime


class createContent(BaseModel):
    id: int
    title: str
    body: str
    photo_name: str
    author: str


class GetComment(BaseModel):
    id: int
    post_id: int
    author: int
    text: str
    date_time: datetime


class createComment(BaseModel):
    text: str
    post_id: str


