# from dotenv import load_dotenv

# load_dotenv()

import os
from typing import List
import requests
from api import Todo

# DB_URL = os.getenv("DB_URL")

# def url(route: str):
#     return f"{DB_URL}{route}"

#--------------------------------------------
def url(route: str):
    return f"http://127.0.0.1:8000{route}"
#-----------------------------------------




print("Hello from todo app")


def print_menu():
    print(
        """
    1: Add Todo
    2: Get Todo
    3: Delete Todo
    4: Update Todo
    5: Exit program
    """
    )


########### add ###########################################

def add_todo():
    print("Add todo")
    title = input("Todo title: ")
    description = input("Todo description: ")
    new_todo = Todo(title=title, description=description)
    res = requests.post(url("/add_todo"), json=new_todo.dict())
    print(res)
    


########### GET ###########################################

def get_todo():
    todos = [] 
    print("Get todo")
    res = requests.get(url("/todos"))
    if not res.status_code == 200:
        return
    data = res.json()
    for todo in data:  # {"id": 1, "title": "blabla", "description": "blabla"}
        todo = Todo(**todo)  # unpackar dikten
        # Är samma sak som
        # todo = Todo(id=todo["id"], title=todo["title"], description=todo["description"])
        print("_________")
        print(f"ID: {todo.id}")
        print(f"Title: {todo.title}")
        print(f"Details: {todo.description}")
        print("")
        todos.append(todo)
    return todos



########### DELETE ###########################################

def delete_todo():
    print("Delete todo")
    todo_to_delete = input("Id of todo you wish to delete: ")
    if not str.isdigit(todo_to_delete):
        print("Ids are integers")
        return
    res = requests.delete(url(f"/delete_todo/{todo_to_delete}"))
    print(res.json())



########### UPDATE ###########################################


def update_todo(todos: List[Todo]):
    print("Update todo", todos)
    todo_to_update = input("Id of todo you wish to update: ")
    if not str.isdigit(todo_to_update):
        print("Ids are integers")
        return

# om vi hittar rätt todo dvs siffra så skrivs den ut och siffran lagras i "i"
    index = None
    for i, todo in enumerate(todos):
        print(todo.id)
        if todo.id == int(todo_to_update):
            index = i
            break
# om siffran inte finns så får vi felmeddelande och listan returneras
    if index == None:
        print("No such todo")
        return
    todo = todos[index]

    title = input("Todo title (leave blank if same): ")
    description = input("Todo description (Leave blank if same): ")

# om det blir tomt så är det fotf okej 
    if not title:
        title = todo.title
    if not description:
        description = todo.description

    new_todo = Todo(title=title, description=description)
    res = requests.put(url(f"/update_todo/{todo_to_update}"), json=new_todo.dict())
    print(res.json())


########### main ###########################################


def main():
    # todos: List[Todo] = []
    print_menu()
    choice = input("Please choose your action: ")
    choice = choice.strip()
    if not str.isdigit(choice):
        print("Please enter a valid option")
        return 

    match int(choice):
        case 1:
            add_todo()
        case 2:
            todos = get_todo()  #de sparas i todo listan
        case 3:
            delete_todo()
        case 4:
            todos = get_todo()
            update_todo(todos)
        case 5:
            exit()
        case _:
            print("Please enter a valid choice")



## om den här programmet körs så får den namn  __name__ och då blir den main programm
## fattar inte helt
while __name__ == "__main__":
    print("")
    print(__name__)
    main()