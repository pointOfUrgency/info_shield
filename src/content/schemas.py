from pydantic import BaseModel
from datetime import datetime


class GetContent(BaseModel):
    id: int
    title: str
    body: str
    author: str 
    date_time: datetime


class createContent(BaseModel):
    id: int
    title: str
    body: str
    author: str


