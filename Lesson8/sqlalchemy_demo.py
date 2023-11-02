## man behöver inte anvädna SQLALCHEMY i slutuppgiften 
## SQL ALCHEMY WEB kolla på exemplar
# https://docs.sqlalchemy.org/en/20/orm/quickstart.html#orm-quick-start
# Kolla hur man gör insert 


##  CTRL + SHIFT + P  för att byta till virtual enviroment 

from sqlalchemy.orm import declarative_base 
from  sqlalchemy import (
__version__, 
create_engine,
ForeignKey, 
Table, 
Column, 
String,
Integer, 
MetaData,
insert,
Sequence

)
# print(__version__)


Base = declarative_base()

meta_data = MetaData() ## metaData objekt som pratar med databasen 





## Vi skapar en tabell 
user_table = Table(
    "user", 
    meta_data, 
    Column("id", Integer, Sequence("user.id", start=1), primary_key = True),
    Column("first_name", String),
    Column("last_name", String)
    )

## en annan tabell 
movie_table = Table(
    "movie", 
    meta_data, 
    Column("id", Integer, primary_key = True),
    Column("title", String),
    Column("year", Integer),
    Column("director", ForeignKey("director.id")),
    )

## 
director_table = Table(
    "director", 
    meta_data, 
    Column("id", Integer, primary_key = True),
    Column("name", String),
    Column("age", Integer),
    Column("company", String),
)


# 1. var ska man lagra data
# 2. skapa kopplingen 
engine = create_engine("sqlite:///test.db")
meta_data.create_all(engine)


#______________________________ Tabell som klass
# class User(Base):
#     __tablename__ = "User"

#     id = Column(Integer, Primary_key= True)
#     first_name = Column(String)
#     last_name = Column(String)
#     pass


#__________________________________
## insert måste importeras i början, längst uppe
## insert data i tabeller

#---- första sättet----
# statement = insert(user_table).values(first_name = "David", last_name = "Adamovic")

# # execute instruktioner 
# with engine.connect() as conn:
#     conn.execute(statement)

#----andra sättet------
## man kan gära det på det här sättet också 
# with engine.connect() as conn:
#     conn.execute(insert(user_table),
#                  [
#                  {"first_name": "Alma", "last_name": "Berggren"},
#                  {"first_name": "Aid", "last_name": "Mandzukic"},
#                  {"first_name": "Danja", "last_name": "Tucakovic"},
#                  {"first_name": "Nima", "last_name": "Nikbakhtan"},
#                  {"first_name": "Alex", "last_name": "Butilca"},
#                  ],
#             )   


#________________________







# connection = engine.connect()
# res = connection.execute("SELECT * FROM book")
# print(res.fetchall())
### vi måste altid stänga när vi är klara
# res.close()
# connection.close()


#______________________________________________________
# Andra sätt att skapa koppling utan att glömma o stänga den efteråt




# with engine.connect() as conn:
#     res = conn.execute(
#         "INSERT INTO book (title, author) VALUES ('Na Drini Cuprija', 'Ivo Andric')")
    

# with engine.connect() as conn:
#     res = conn.execute(
#         "INSERT INTO book (title, author) VALUES ('Jezeva kucica', 'Branko Copic')")


# with engine.connect() as conn:
#     res = conn.execute("DELETE FROM book WHERE author = 'Ivo Andric'")
#     print(res.fetchall())


# with engine.connect() as conn:
#     res = conn.execute("SELECT * FROM book")
#     print(res.fetchall())



# with engine.connect() as conn:
#     conn.execute(User)