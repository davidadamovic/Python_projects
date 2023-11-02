from typing import List 
from card import Card, CardSuit, CardValue
### Card är klassen som hanterar alla Constanter från en annan klass 

### så att vi vet att när denna filen körs då är den main 
print(__name__)


class Deck:
    cards: List[Card] = []  ##
    
# init metod som ger varje CardValue 4 olika suits.    
# det är ett metod som ger ett deck med 52 kort  
    def __init__(self):
        for suit in CardSuit:
            for value in CardValue:
                self.cards.append(Card(value, suit))       
        # for card in self.cards:    ### i card variabeln lagras svaret från loopen 
        #     print(card)

## denna metoden tar ut ett kort med pop() och den försvinner från decket 
    def pull_card(self):
        return self.cards.pop() 
        ## pop() völjer sista item från listan i en loop
