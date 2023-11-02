import sqlite3

# connection = sqlite3.connect("test.db")    
# ## för att skapa en databas och koppla till en API
# # #för att den ska hamna rätt så måste man gå in i rätt terminal o sen  i terminalen till rätt fil 
# # # connection.close() ## stänger kopplingen till databasen så att man 
# cursor = connection.cursor() 
# # ## cursor går igenom data basen och vi behöver det för att redigera data
# cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY)")
# cursor.execute("CREATE TABLE IF NOT EXISTS test2 (id INTEGER PRIMARY KEY)")
# cursor.execute("CREATE TABLE IF NOT EXISTS test3 (id INTEGER PRIMARY KEY)")
# cursor.execute("CREATE TABLE IF NOT EXISTS test4 (id INTEGER PRIMARY KEY)")


# res = cursor.execute("SELECT name FROM sqlite_master")
# cursor.execute("DROP TABLE IF EXISTS test4")
# cursor.execute("DROP TABLE IF EXISTS test2")
# cursor.execute("DROP TABLE IF EXISTS test3")

# # res2 = cursor.execute("DROP TABLE IF EXISTS test4")
# # res = cursor.execute("SELEC name FROM sqlite_master")
# # print(res.fetchall(), res2.fetchall())
# print(res.fetchall()) 
# # print(res.fetchone()) 
# # fetchone är en metod for att välja en tabel
# # fetchall för alla tabeller
# cursor.close()
# # # när man är klar med sql kommer man vilja stänga det som nedan 
# connection.close()

#_____________________________________________________________________
# skriver en funktion så att man slipper upprepa den hela tiden 


def call_db(query: str):  
    print(query)
    connection = sqlite3.connect("test.db")   #först skapa databas
    cursor = connection.cursor()    # skapa cursor
    res = cursor.execute(query)     # skapa en varibel med cursor som exekverar en query 
    data = res.fetchall()           # hämtar all data och sparar i variabel data
    cursor.close()                  # stänger cursorn
    connection.commit()          # vi måste commita våran connection innan vi stänger den annars går det tillbaka
    connection.close() 
    return data

# call_db( skriv querry here )



# data = call_db("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY)")
# print(data)


#----------------------------------
# vi kan fixa att variabel querry blir en mall 

# skapa tabellen

# query = """
# CREATE TABLE IF NOT EXISTS book(
#     id INTEGER PRIMARY KEY,
#     title VARCHAR (255),
#     author VARCHAR (255)
# );
# """
# data = call_db(query)
# print(data)

# # -------------------


# # lägg till data
# query = """
# INSERT INTO book (title, author) 
#     VALUES ('it', 'Stephen King');
#     """

# data = call_db(query)
# print(data)

# # -------------------

# # visa tabellen 
# query = """
# SELECT * FROM book 
# WHERE title = "it";
# """
# data = call_db(query)
# print(data)

# #----------

# call_db("DROP TABLE book")
# --------------------