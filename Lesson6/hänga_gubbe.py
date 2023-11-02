# Antngen har vi en lista med ord vi väljer från 
# Eller så skriver 1 person ett ord i början (Börjar här)

# kolla om bokstaven finns
# öka scoren när det är fel 
from typing import List



def main():
    game_list = []
    goal_string = input("What is the word? ")
    goal_string = goal_string.strip()  # remove spaces 

    for _ in range(len(goal_string)):
        game_list.append("_ ")

    print(game_list)



def take_input(letter:str):
    letter = True

    while letter:
        letter = input("Give me a letter: ")

        for letter in goal_string:
        
        pass





main()      