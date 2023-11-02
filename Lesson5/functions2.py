

def a_function():
    print(" A function")

def another_function():
    print("Another function")

# Grejen är att man behöver inte alltid anropa funktioner
# man kan lägga funktionen i en variabel och få det att funka
a_variable = a_function

# gär man så här så sparas a_function i andra fintionen så skriv inte över den 
# another_function = a_function


#anropa funtioner
#a_function()
#another_function()
#a_variable()  # man måste ha parantes med annars så kör den inte funktionen 

#print(a_function, a_variable) #för att få lite information 

def first_function(a):  # man måste ange a för att veta hur många argument ska man ha
  #  print(a(1,2)) # vi anropar a där vi har lagrat  secod_function i a där nere
    print("First function", a)  
    # vänder man platser så skrivs ut a före "print"
    # 

def second_function(a,b):
    print("Second function")
    #return "Hola"

#first_function("Hej")  # nu hamnar Hej i i variabel a 
first_function(second_function) #för att få definitionen av andra funktionen



print(" ")
print("_______________________lambda funktioner______________________")

# En lambda funktion är en anonym funktion
def my_lambda (a, b):
    return a+b
# print(my_lambda(1, 2))

# när man kör den så får man resultat på en gång 


#bättre exempel på lambda funktioner
first_function(lambda a,b: a+b) # man får 3 
# det är sytaxen, parametrar : vad den returnerar

people = [{"name": "David", "Age": "22"},
        {"name": "Alma", "Age": "21"},
        {"name": "Aid", "Age": "54"},
        {"name": "Nima", "Age": "32"}]

#när man anropar sorted måste man använda funktionen key för att det går inte att jamföra dikter
# sorterat baserat på oldern
# vanlig utskrift
print(sorted(people, key=  lambda vadsomhelst: vadsomhelst["Age"] ))  # tänk att det står return after person:
print(people)



# samma sak 
# key här en funktion i båda fallen som gör jobbet
def compare_name(b):
    return b["name"]

# man kan sortera enligt namn på denna sättet
print(sorted(people, key=compare_name ))
# eller
print(sorted(people, key = lambda variabel: variabel ["name"]))





print(" ")
print("_______________________decorator______________________")

# här kommer man också ha en funktion i en funktion 

def func_two(func): # den tar emot en funktion som argument som angett annars skriver den info bara
 #   print("func 2")    # om vi skriver print här så skrivs ut denna först 
    def wrapper():     # i den funktionen anropar vi en annan som returneras sedan 
        func()   #parameter argument
        print("func 2")
    return wrapper

# decorator funktion 
# den tar in en funktion sen kan den göra lite logik (om vi vill) och returnerar en annan funktion som vi definerar innuti func_two
# i vilken vi kör den första funktionen 
# med andra ord = func_one är egentligen func_two med sig själv i sig 
@func_two  #den säger func_two funtionen innhehåller funktionen nedan
def func_one():
    print("func 1")
# den här gör egentligen 


### func_one()  
# func_two(func_one) # då kommer den köra båda två - func 1 först sedan func 2


# man skulle istället kunna skriva 
# func_one = func_two(func_one)  # och få samma resultat (efter att man har tagit bort @func_two)
# men eftersom vi har använt oss av dekorator så räcker det med att anropa bara func_one för att den redan innehåller func_two i sig 
# func_one() 





def func_three():
     print("func 3")

# den samma sak
# först körs func_three sen func_two
func_three = func_two(func_three)

func_one()    
print("_______")
func_three()
 







