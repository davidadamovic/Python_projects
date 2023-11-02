
## Ett program som ska fungera som en magic 8 ball. Programmet ska fråga användaren om ett ja/nej fråfa och sedan 
## skriva ut ett slumpmässigt svar 

# Kräver användning av random modulen 
# Kräver användning av input funktionen 
# Kräver användning av lista


from random import choice


replies = [   "It is certain.",
               "It is decidedly so.",
               "Without a doubt.",
               "Yes definitely.",
               "You may rely on it.",
               "As I see it, yes.",
               "Most likely.",
               "Outlook good.",
               "Yes.",
               "Signs point to yes.",
               "Reply hazy, try again.",
               "Ask again later.",
               "Better not tell you now.",
               "Cannot predict now.",
               "Concentrate and ask again.",
               "Don't count on it.",
               "My reply is no.",
               "My sources say no.",
               "Outlook not so good.",
               "Very doubtful.",
]


# random_answer = choice(replies)
# print(random_answer)



will_continiue = True

while will_continiue:
    random_answer = choice(replies)
    print("")
    print("Ask me anything 8-)...")
    svar = input() 
    print("")
    print(random_answer)
    print("")
    
    while True: 
        keep_playing = input("Wanna know more? (y/n): ")
        # if keep_playing != "y" or "n":
        #     print("???")
        #     continue
        if keep_playing == "y":
            will_continiue = True
            break 
        elif keep_playing == "n":
            will_continiue = False
            print("")
            print("K bye")
            print("")
            break
      
                





