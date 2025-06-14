from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

from sqlmodel import SQLModel, Field, create_engine, Session, select

class ToDo(BaseModel):
    name: str
    description: str | None = None
    author: str | None = None
    id: int | None


class ToDoTable(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    description: str | None = None
    author: str | None = None


engine = create_engine(url="sqlite:///my-database")
SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.post("/todo/")
async def create_item(todo: ToDo):
    with Session(engine) as s:
        todo_dict = todo.model_dump()
        s.add(ToDoTable(**todo_dict))
        s.commit()
    
    return todo


@app.get("/todo/all")
async def get_latest_item():
    with Session(engine) as s:
        stmt = select(ToDoTable)
        result = s.exec(stmt)
        return result.all()
