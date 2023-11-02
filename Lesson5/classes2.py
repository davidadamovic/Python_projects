
from dataclasses import dataclass


class Person:
    name: str
    age: int
    __spy_name: str

    def __init__(self, name: str, age: int, spy_name: str):
        self.name = name
        self.age = age
        self.__spy_name = spy_name    # __variabel   =  skapar privat variabel 

### denna metoden skapar en privat variabel som inte kan ändras
    def get_spy_name(self):
      #  print(self.__spy_name)
        return self.__spy_name

### denna metoden gör att man kan ändra privata den privata variabeln 
    def set_spy_name(self, spy_name: str):
        self.__spy_name = spy_name  # den innehåller attribut så self måste deklareras här så att angett attribut hittar vägen till Klassen
       # return self.__spy_name        ## annars så ändras det ingenting

### en privat metod. skapas också med __funtkion()  som gör __spy_name till uppercase
    def __shoutout_spy_name(self): 
        print(self.__spy_name.upper())   
###för att kunna anropa metoden måste vi skapa en ny metod som gör det 
### JAG VET INTE VARFÖR
   
    def hjälp_metod(self):      
        self.__shoutout_spy_name()
    
#________STATIC METOD______________
### den behöver ingen self men behöver en @staticmethod function 
### den blir mer som en funktion i en class (och inte en method)
    @staticmethod 
    def say_hi():    #kan ta in argument 
        print("Hi")


        


# david.age()  kan inte funka för att age är en attribut, och ingen metod

david = Person("David", 22, "Brratzs")
#david.__spy_name = "Beverly"   # namnet är inte privat och kan ändras utanför klassen 


print(david.name)  # man måste alltid ange punkt och atribut efter variabeln
#print(david.__spy_name) # den kommer va ändrad
#_______________________________________________________________
### Anropa metoden = variabel.metod
david.get_spy_name() 
### nu kommer vi få det utskrivet eftersom vi har skapat en metod i Klassen som skriver ut den privata variabeln
### och returnerar bara den och den kan inte ändras utanför Klassen 
#________________________________________________________________

### För att ändra värdet på privata variaveln 
david.set_spy_name("Mirko")
### Sedan måste vi anropa den gamla metoden som skapar privata variabler för att få fram resultatet
## david.get_spy_name()  ### om man har print funktion i metoden 
print(david.get_spy_name())

#__________________________________________________________________

#david.__shoutout_spy_name()  ### Vi går meddelanden att metoden inte finns så vi anropar metoden som anropar våran metod
david.hjälp_metod()
#__________________________________________________________________

david.say_hi()

#_________________________________________________________________
### den här klassen kan man sedan importera i en annan fil och så har man Calculator
###  Det är bara att skriva =  from lession5.classes2 import Calculator
class Calculator:
### vi behöver ingen __init__ för att vi sparar ingen data i de
### statiska metoder är som enskilda funktioner fast i en klass 

    @staticmethod
    def div (a,b):
        return(a/b)
    
    @staticmethod
    def mul (a,b):
        return(a*b)

    @staticmethod
    def sub (a,b):
        return(a-b)

    @staticmethod
    def add (a,b):
        return(a+b)


result = Calculator.div(10,5)
print(round(result))

#__________________________DATA CLASSES_________________________________________
### dataclass är en standardbibliotek i Python vilken är en funktion och en dekorator
### Vad gär en dataclass?
### Dataclasses är nyare och enklare. Den är inte för logik 

### man behöver inte __init__ metod. Den är redan inbyggt i en dataclass
### i dataclasser måste man ange attributen och typen 
@dataclass
class Animal:
    name: str  # attribut och typ 
    height: float
    weight: float
    diet: str
    pass

    def update_name(self, name:str):
        self.name = name


### Det rekommenderas inte att göra multiple inheritance med Dataclass eller vanlig klass men här e exemplet ändå 
@dataclass
class Dog (Animal):
    race: str
    pass



mouse = Animal("Mouse", 5, 300, "Omnivore")
print(mouse)

#_________________________________________________________
### Vi kan bara göra "print(variabel)" och så får man önskad svar
### i vanliga klasser måste man skriva atribut variabel.attribut

mouse.update_name("Rat")
print(mouse)

#___________________________________________________
### Dog är en underklass så den använder samma argument som Animal 

fido = Dog("Fido", 60, 23, "NMP", "Doberman")
print(fido)
    