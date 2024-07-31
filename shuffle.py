import random
import card

card_set: dict = {
    'Two': {"Nick": "2", "Value": 2},
    'Three': {"Nick": "3", "Value": 3},
    'Four': {"Nick": "4", "Value": 4},
    'Five': {"Nick": "5", "Value": 5},
    'Six': {"Nick": "6", "Value": 6},
    'Seven': {"Nick": "7", "Value": 7},
    'Eight': {"Nick": "8", "Value": 8},
    'Nine': {"Nick": "9", "Value": 9},
    'Ten': {"Nick": "10", "Value": 10},
    'Jack': {"Nick": "J", "Value": 10},
    'Queen': {"Nick": "Q", "Value": 10},
    'King': {"Nick": "K", "Value": 10},
    'Ace': {"Nick": "A", "Value": 11}
}

suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
setsInDeck: int = 4
deck = []


def shuffle_init(dec_amount: int):
    deck.clear()
    for _ in range(dec_amount):
        for card_name in card_set:
            for suit in suits:
                deck.append(card.Card(card_name, suit, card_set[card_name]["Value"], card_set[card_name]["Nick"]))


def stir(dec_amount: int):
    result = []
    shuffle_init(dec_amount)
    while len(deck) > 0:
        result.append(deck.pop(random.randint(0, len(deck) - 1)))

    return result
