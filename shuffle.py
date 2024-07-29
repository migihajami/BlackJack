import random
import card

card_set: dict = {
    'Two'  : 2,
    'Three': 3,
    'Four' : 4,
    'Five' : 5,
    'Six'  : 6,
    'Seven': 7,
    'Eight': 8,
    'Nine' : 9,
    'Ten'  : 10,
    'Jack' : 10,
    'Queen': 10,
    'King' : 10,
    'Ace'  : 11
}

suits = [ "Hearts", "Clubs", "Diamonds", "Spades"]
setsInDeck: int = 4
deck = []

def shuffle_init(dec_amount: int):
    deck.clear()
    for _ in range(dec_amount):
        for card_name in card_set:
            for suit in suits:
                deck.append(card.Card(card_name, suit, card_set[card_name]))

def stir(dec_amount: int):
    result = [] 
    shuffle_init(dec_amount)
    while len(deck) > 0:
        result.append(deck.pop(random.randint(0, len(deck) - 1)))
    
    return result


