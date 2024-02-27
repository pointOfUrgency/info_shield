from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from content.database import Base
from datetime import datetime



class Content(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    author = Column(String, nullable=False)
    date_time = Column(TIMESTAMP, default=datetime.utcnow)

    # for_post = relationship("Comment", back_populates="post")

    class Config:
        orm_mode = True


