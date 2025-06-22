from fastapi import FastAPI
from sqlmodel import SQLModel, Session, select
from .database import engine
from .models import ToDo, ToDoTable

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
