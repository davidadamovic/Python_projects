from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from mssql_db import DB
# from db import DB

# lite som en dataclass, behöver ingen _init_ metod
class Todo(BaseModel):
    id: int = None
    title: str
    description: str


app = FastAPI()
# db = DB("todo.db")
db = DB()




# manuell id
app.curr_id = 1

## den här är för att spara lite saker utan att skapa databasen
app.todos: List[Todo] = []
#-------------------


#___________________________________________________________

@app.get("/")
def root():
    return "Return a list of all available tasks"



#--------------------------
# @app.get("/todos")
# def get_todos():
#     return app.todos
#--------------------------

@app.get("/todos")
def get_todos():
    get_todo_query = """
    SELECT * FROM todo
    """
    data = db.call_db(get_todo_query)
    todos = []
    for element in data:
        id, title, description = element
        todos.append(Todo(id=id, title=title, description=description))
    print(data)
    return todos

#--------------------------
# @app.get("/todo/{id}")
# def get_todo(id: int):
#     return "Returns a single task with id " + str(id)


#--------------------------

# @app.post("/add_todo")
# def add_todo(todo: Todo):
#     print(todo)
#     todo.id = app.curr_id
#     app.todos.append(todo)
#     app.curr_id += 1
#     return "Add a task"

#--------------------------
@app.post("/add_todo")
def add_todo(todo: Todo):
    insert_query = """
    INSERT INTO todo (title, description)
    VALUES ( ?, ? )
    """
    db.call_db(insert_query, todo.title, todo.description)

    print(todo)
    todo.id = app.curr_id
    app.todos.append(todo)
    app.curr_id += 1
    return "Adds a task"


#--------------------------
# @app.delete("/delete_todo/{id}")
# def delete_todo(id: int):
#     app.todos = list(filter(lambda todo: todo.id != id, app.todos))
#     return True


#--------------------------
@app.delete("/delete_todo/{id}")
def delete_todo(id: int):
    delete_query = """
    DELETE FROM todo WHERE id = ?
    """
    db.call_db(delete_query, id)
    # app.todos = list(filter(lambda x: x.id != id, app.todos))
    return True




#--------------------------
# @app.put("/update_todo/{id}")
# def update_todo(id: int, new_todo:Todo):
#     for todo in app.todos:
#         if todo.id == id:
#             todo.title = new_todo.title
#             todo.description = new_todo.description 
#     return True
#--------------------------


@app.put("/update_todo/{id}")
def update_todo(id: int, new_todo: Todo):
    update_todo_query = """
    UPDATE todo
    SET title = ?, description = ?
    WHERE id = ?
    """

    db.call_db(update_todo_query, new_todo.title, new_todo.description, id)
    # for todo in app.todos:
    #     if todo.id == id:
    #         todo.title = new_todo.title
    #         todo.description = new_todo.description
    return True