
# try  OK 
# except  OK
# else  OK
# finally OK 
# raise OK 
# assert OK 
# custom exceptions OK


### CUSTOM EXCEPTIONS ###

class TooLowNumberValueError(Exception):
    msg: str    

    def __init__(self, msg):
        self.msg = msg




def do_something(a):
    res = int(a)
    if res < 2:
        raise TooLowNumberValueError("The number is way too low")    # raise kommer sen att peka ut syntaxerror om den finns
    return res


# vi kan ha logiken i try
try: 
    print("trying")
    assert 2 == 2               #påstår att 2 == 1 (true eller false) ger AssertionError
    print(do_something("1"))
except AssertionError:
    print("AssertionError")     # value error handlar om values
except ValueError: 
    print("ValueError")
except SyntaxError:             # här säger vi att det ska va ett error om det logiken stämmer
    print("SyntaxError")
except TooLowNumberValueError as vadsom:     # e is a variable and e.msg is ärv
    print(vadsom.msg)
else:  # den här blir när try har körts och det blir inget fel 
    print("ALLT OK")
finally: 
    print("this executes always, at the and")

