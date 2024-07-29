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
shuffle = []

def shuffle_init(dec_amount: int):
    shuffle.clear()
    for _ in range(dec_amount):
        for card_name in card_set:
            for suit in suits:
                shuffle.append(card.Card(card_name, suit, card_set[card_name]))

def stir(dec_amount: int):
    result = [] 
    shuffle_init(dec_amount)
    while len(shuffle) > 0:
        result.append(shuffle.pop(random.randint(0, len(shuffle) - 1)))
    
    return result


