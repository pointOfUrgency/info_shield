from pydantic import BaseModel
from datetime import datetime

class GetContent(BaseModel):
    id: int
    title: str
    body: str
    author: str
    date_time: datetime


class createContent(BaseModel):
    title: str
    body: str
    author: str


class GetComment(BaseModel):
    id: int
    post_id: int
    author_id: int
    text: str
    date_time: datetime


class createComment(BaseModel):
    text: str


