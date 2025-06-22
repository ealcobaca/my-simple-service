from sqlmodel import SQLModel, Field
from pydantic import BaseModel


class ToDo(BaseModel):
    name: str
    description: str | None = None
    author: str | None = None


class ToDoTable(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str | None = None
    author: str | None = None
