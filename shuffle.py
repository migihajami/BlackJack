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
CARDS_IN_ONE_DECK = 52

class Shuffle:
    sorted_deck: list
    dec_amount: int
    deck: list

    def __init__(self, dec_amount: int):
        self.sorted_deck = []
        self.deck = []
        self.dec_amount = dec_amount
        self.stir()

    def shuffle_init(self):
        self.sorted_deck.clear()
        for _ in range(self.dec_amount):
            for suit in SUITS:
                block = [card.Card(item, suit, value["Value"], value["Nick"]) for (item, value) in CARD_SET.items()]
                self.sorted_deck.extend(block)


    def stir(self):
        self.deck.clear()
        self.shuffle_init()
        while len(self.sorted_deck) > 0:
            self.deck.append(self.sorted_deck.pop(random.randint(0, len(self.sorted_deck) - 1)))

    def hit(self):
        if len(self.deck) < 10:
            self.stir()

        return self.deck.pop(0)

    def __len__(self):
        return len(self.deck)
