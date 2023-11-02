from deck import Deck


def main():
    deck = Deck()
    while len(deck.cards) > 0:
        card = deck.pull_card()
        print(card)
        input()

### Den gär att filen som körs blir automatisk en main fil 
if __name__ == "__main__":
    main()