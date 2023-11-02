import sqlite3
from fastapi import FastAPI 
from pydantic import BaseModel



## här skapas appen som heter app
## skapa en app av en FastAPI konstruktör
app = FastAPI()



#_______________________________________________________
### Återanvänder funktionen som vi skapade förra lektionen

def call_db(query: str , *args):  
    connection = sqlite3.connect("api.db")   #först skapa databas
    cursor = connection.cursor()    # skapa cursor
    res = cursor.execute(query, args)     # skapa en varibel med cursor som exekverar en query 
    data = res.fetchall()           # hämtar all data och sparar i variabel data
    cursor.close()                  # stänger cursorn
    connection.commit()          # vi måste commita våran connection innan vi stänger den annars går det tillbaka
    connection.close() 
    return data


##_______________________________________
# skapar en databas
def populate_database():
    connection = sqlite3.connect("api.db")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS person (id INTEGER PRIMARY KEY, name VARCHAR(100) NOT NULL)"
        )
    # cursor.execute("INSERT INTO person (name) VALUES ( 'David' )")
    # cursor.execute("INSERT INTO person (name) VALUES ( 'Danja' )")
    # cursor.execute("INSERT INTO person (name) VALUES ( 'Alma' )")
    cursor.close()
    connection.commit()
    connection.close()
    pass



a = " This is something big.."
## skapa route to get data och en funktion som gör något
## i denna URLen (/) kommer denna funktionen o köras
@app.get("/") #i parantesen är det som kommer o stå i url (i detta fallet tomt)
def root(): ## 
    return a

#__i teminalen__
## uvicorn main:app --reload 
## detta gör att man behöver inte göra mycket när man lägger till saker. Bara trycka på kör och refreshas det allt på webbsidan

#_____________________________________________________
## detta är en dekotarör (Kolla upp det)
## i denna URLen (/) kommer denna funktionen o köras
@app.get("/test")
def test():
    print("This is the test place")
    return "Hello Test "

#_________________________________________________________________
## använder databasen funktion 
## verkar inte funka, skapar tabellen men inga värden läggs till 

@app.get("/populate")
def test3():
    populate_database()
    return "Populate"

#_______________________________________________________
@app.get("/test/fisk/banan")
def test1():
    print("This is the test place")
    return "Hello Test, fisk, banan"

#_________________________________________________________
## vi kan ha logik och mycket annat men bara resultatet visas på webbsidan 
@app.get("/test/loop")
def test2():
    i = 0 
    while True:
        print("Dobar dan")
        i += 1
        if i > 10:
            break 
    return "Another test"


##_______________________________
# för att visa alla i tabellen 

@app.get("/persons")
def get_people():
    person_query = """
    SELECT * FROM person
    """
    persons = call_db(person_query)

    return persons
    
# /person/?id=Alma
#man måste ha ? efter persons/

# /person/?id=1&name=David

#____________________________________
# för att välja en person bara eligt id

# @app.get("/person/id/{id}")
# def get_person_by_id(id:int):
#     get_person_query = """
#     SELECT * FROM PERSON 
#     WHERE id = ? 
#     """
#     # för att kunna ha två argument här måste man andra det i funktionen call_db 
#     data = call_db(get_person_query, id)
    
#     return data

#  #_____________________________________
#  # Inte valid integer 

# @app.get("/person/name/{name}")
# def get_person_by_id(name:str):
#     get_person_query = """
#     SELECT * FROM PERSON 
#     WHERE name = ? 
#     """
#     data = call_db(get_person_query, name)
    
#     return data

#___________________________________________

@app.get("/person/")
def get_person(name: str = None, id: int = None):
    print(name, id)
        # insert_person_query = """
    # insert into person (name) values (?)
    # """
    # call_db(insert_person_query, name) # Dålig praxis
    return "Get Person"



#_____________________________________________________________
## att använda klass 

class Person(BaseModel):
    name: list
    id: list


#--post

@app.post("/persona")
def post_person(person: Person):
    insert_person_query = """
    insert into person (name) values (?)
    """
    call_db(insert_person_query, person.name)  # Dålig praxis
    return person


#_________________________________________________________

@app.put("/update_person")
def update_person(person: Person):
    update_person_query = """
    UPDATE person SET name = ? WHERE id = ?
    """
    call_db(update_person_query, person.name, person.id) 
    return person



#___________________________________________________

@app.delete("/delete_person/{id}")
def delete_person(id:int):
    delete_person_query = """
    DELETE FROM person WHERE id = ?
    """
    call_db(delete_person_query, id) 
    return id

