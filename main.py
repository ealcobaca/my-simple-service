from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

class ToDo(BaseModel):
    name: str
    description: Optional[str] = None
    author: Optional[str] = None

app = FastAPI()

MEMORY: List[ToDo] = [ToDo(name="default")]

@app.post("/todo/")
async def create_item(todo: ToDo):
    if todo.description is not None:
        todo_dict = todo.model_dump()
        todo_dict["description_len"] = len(todo.description)
        MEMORY.append(ToDo(**todo_dict))
        return todo_dict
    else:
        MEMORY.append(todo)
        return todo


@app.get("/todo/last")
async def get_latest_item():
    return MEMORY[-1]


@app.get("/todo/first")
async def get_latest_item():
    return MEMORY[0]


@app.get("/todo/all")
async def get_latest_item():
    return MEMORY
