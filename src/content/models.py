from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from content.database import Base
from datetime import datetime
from auth.database import User

class Content(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    photo_name = Column(String, nullable=False)
    body = Column(String, nullable=False)
    author = Column(String, nullable=True)
    date_time = Column(TIMESTAMP, default=datetime.utcnow)


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("content.id"))
    author_id = Column(Integer, ForeignKey(User.id))
    author = relationship("User", back_populates="posts")
    text = Column(String, nullable=False)
    date_time = Column(TIMESTAMP, default=datetime.utcnow)