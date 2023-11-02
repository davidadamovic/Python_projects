
# skapa en funktion och gör en print som bara säger "calculator". 
# utsktifter i terminalen får inte ske någon annanstans än i main() funktionen 

from typing import Tuple

global OPERATIONS    #han skapade en global variabel för att den kan användas i alla funktioner så att han slipper o upprepa sig
OPERATIONS = ['+', '-', '/', '*']

def addition(num1: int, num2:int):
   return num1 + num2 

def subtraction(num1:int, num2:int):
   return num1 - num2

def multiplication(num1:int, num2:int):
   return num1 * num2 

def division(num1:int, num2:int):
    if num2 == 00:
        print("kan inte dividera med 0 ")
        num1, num2 = get_input(prev_value=num1)
    return num1 / num2




def get_input(prev_value: int | float | None)-> Tuple [int | float , int]:
    valid = False
    if prev_value: #
        valid = True #
        validated1 = prev_value # den här prev_value har vi lagt till så att vi kan lagra resultatet i 
    while not valid:   # ako broj koji upisemo nije validan 
        choice1 = input("Vilket är ditt nummer?: ") # choice1 pise tekst i trazi input
        valid = validate_input(choice1) # valid jer nova varijabla koja provjerava choice1(input koji smo unijeli)
        if valid: # ako je broj koji smo unijeli validan 
            validated1 = int(choice1) #validation sadrzi provjerenu varijablu ali je mjenja u int 
    valid = False # ako ne dodje do if onda ostaje da je valid False kao iz pocetka
    while not valid: # while loop za drugi broj 
        choice2 = input("Vad är ditt andra nummer?: ")
        valid = validate_input(choice2)
        if valid:
            validated2 = int(choice2) #variabla koja se returna 
    return(validated1, validated2)



def validate_input (choice_string:str) ->bool:   # kan vara int så vet inte varför han valde string
    valid = str.isdigit(choice_string)
    if not valid:
        print("Felaktigt input")
    return valid



def get_operation() -> str:
    global OPERATIONS  #globala variabler kommer först så att vi vet att de ska användas i funktionen 
    valid = False 
    while not valid:
        operation = input("Vilken beräkning vill du göra? ('+', '-', '/', '*'): ")
        if operation in OPERATIONS: # om operationen finns in OPERATIONS returnera operationen 
            valid = True 
        return operation 

def get_continiue() -> bool:
    while True:
        choice = input("Vill du forstätta? (y) eller (n) ") 
        if choice == "y":
            return True        # man gör ingen speciell input nu. Det gör man i slutet 
        if choice == "n":
            return False

    

def get_re_use_res() -> bool:
     while True:
        choice = input("Vill du återanvända resultatet? (y) eller (n) ") 
        if choice == "y":
            return True        # man gör ingen speciell input nu. Det gör man i slutet 
        if choice == "n":   
           return False    



# som i uppgiften står får utskrifter i terminalelen ske bara när main funktionen anropas
# för att hjälpfunktionerna ska användas i en main funktion de ska lagras i en variabel isf

def main ():
    print("Kalkylator")

    will_continiue = True 
    res = 0 
    reuse = False
    while will_continiue:
        if not reuse:
            res = None
        num1, num2 = get_input(prev_value=res)
        operation = get_operation()

        if operation == "+":
            res = addition(num1, num2)
        elif operation == "-":
            res = subtraction(num1, num2)
        elif operation == "*":
            res = multiplication(num1, num2)
        elif operation == "/":
            res = division(num1, num2)
        print(res)

        will_continiue = get_continiue()  
        if not will_continiue:
            break
        reuse = get_re_use_res()
        
    








main()




   
   







