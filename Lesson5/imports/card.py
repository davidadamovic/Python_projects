from dataclasses import dataclass
from enum import Enum

print(__name__)


### denna klassen finns fär att innehålla Constanter som ska användas sen 
class CardValue(Enum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    KNIGHT = "12"
    QUEEN = "13"
    KING = "14"


class CardSuit(Enum):
    HEARTS = "♡"
    DIAMONDS = "♢"
    SPADES = "♠"
    CLUBS = "♣"

### varför här vi denna klassen? 
### Denna klassen finns för att komma åt varje kort lätt  och för att ha ett fint utskrift
### med hjälp av __str__ metoden 
@dataclass
class Card:
    suit: CardSuit
    value: CardValue

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit 


### så vi har en metod i filen deck. Den metoden går igenom varje CardSuit Constant och ger varje värde av sina värden till varje kort 
### därför skriver vi i __str__ metoden self.suit.value(varje suit blir en value, sedan varje suit blir andra value osv)
### self.value.value skriver bara ett value av en Constant i CardValue.
    def __str__(self):
        return f"{self.suit.value} {self.value.value}"     




# kort = Card("HEARTS", "10")
# print(kort)