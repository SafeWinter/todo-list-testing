from enum import Enum
from typing import Optional

from sqlalchemy import Integer, MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from database.uri import uri


class Base(DeclarativeBase):
    pass


class Status(Enum):
    DRAFT = "draft"
    IN_PROGRESS = "in progress"
    COMPLETE = "complete"


meta = MetaData()


class Task(Base):
    __tablename__ = "task"
    metadata = meta
    id = mapped_column(Integer, primary_key=True)

    description: Mapped[str]
    status: Mapped[Status]


class User(Base):
    __tablename__ = "profile"
    metadata = meta

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str]
    hashed_password: Mapped[str]
    email: Mapped[Optional[str]]
    full_name: Mapped[Optional[str]]
    disabled: Mapped[Optional[bool]]


engine = create_engine(uri)


meta.create_all(engine)
