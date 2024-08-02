import random
import card

CARD_SET: dict = {
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

SUITS = ["Hearts", "Clubs", "Diamonds", "Spades"]


class Shuffle:
    deck: list
    dec_amount: int

    def __init__(self, dec_amount: int):
        self.deck = []
        self.dec_amount = dec_amount

    def shuffle_init(self):
        self.deck.clear()
        for _ in range(self.dec_amount):
            for card_name in CARD_SET:
                for suit in SUITS:
                    self.deck.append(card.Card(card_name, suit, CARD_SET[card_name]["Value"], CARD_SET[card_name]["Nick"]))

    def stir(self):
        result = []
        self.shuffle_init()
        while len(self.deck) > 0:
            result.append(self.deck.pop(random.randint(0, len(self.deck) - 1)))

        return result
