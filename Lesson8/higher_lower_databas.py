import random
from sqlite_demo import call_db

# UNFINISHED - try to finish it yourself
# skapa en funktion utav ett programm

#________________________________________________
max = 10
min = 1

score = 0

random_num = random.randint(min, max)


#______________________________________________________________
#sparad resultat i databas
#--------först fixar queries


create_table = """
CREATE TABLE IF NOT EXISTS score (
    name VARCHAR(50),
    score INTEGER
)
"""

get_high_scores = """
SELECT * FROM score
"""


#-------nu skapar tabellen och lagrar
call_db(create_table)  

scores = call_db(get_high_scores)

if len(scores) == 0:
    print("No points, sorry")
else:
    print(scores)

#----------------


while True:

    print("ditt nummer är: ", random_num)

    guess = input("Vad är din gissning högre eller lägre? (h/l) (exit): ")
    if guess != "h" and guess != "l" and guess != "exit":
        continue
    if guess == "exit":
        print("Tack för att du spelade!")
        break

    new_num = random.randint(min, max)

    if new_num >= random_num and guess == "h":
        score += 1
        print("Rätt, din score är: ", score)
    elif new_num <= random_num and guess == "l":
        score += 1
        print("Rätt, din score är: ", score)
    else:
        print("Fel din score var: ", score)
        score 

        name = input("skriv ditt namn: ")

        create_score = f""" 
        INSERT INTO score (name, score) 
        VALUES ('{name}', '{score}')  
        """
        call_db(create_score)

        print("prova igen")
        
        # print("Ditt nummer är: ", random_num)

    random_num = new_num



#def get_input() -> str: