
from fastapi import FastAPI 
from pydantic import BaseModel

from db import DB
from models import Person

## här skapas appen som heter app
## skapa en app av en FastAPI konstruktör
app = FastAPI()
db = DB("book_api.db")




## GET all persons
@app.get("/persons")
def get_persons():
    data = db.get(table="person")
    return data 

# get person 
@app.get("/persons/{id}")
def get_person_by_id(id:int):
    data = db.get(table="person", 
                  where=("id", str(id)))
    return data 


## POST 
@app.post("/create_person")
def create_user(person: Person):
    db.insert(table = "person", 
              fields={"name": person.name, "age": str(person.age)})
    pass


## DElete
@app.delete("/delete_person/{id}")
def delete_user(id):
    db.delete(table = "person", id=id)


## update person 
@app.put("/update_person")
def update_person(person: Person):
    data = db.update(
        table = "person", 
        fields= {"name": person.name, "age":str(person.age) },
        where= ("id", str(person.id)),
        )
    return data
