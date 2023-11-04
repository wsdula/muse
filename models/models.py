#This file will contain all models for our database(s)

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column, Mapped, relationship
#from typing import List, Optional


class Base(DeclarativeBase):
    pass

class Idea(Base):
    #This table will store user ideas and accompanying attributes
    __tablename__ = "ideas"

    id: Mapped[int] = mapped_column(primary_key=True)
    #File: this will be a path to a media file somewhere on disk, or a Blob representation of the media to be stored
    media: Mapped[LargeBinary]
