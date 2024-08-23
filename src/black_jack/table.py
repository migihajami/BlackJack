from src.black_jack.card import Card
from src.black_jack.shuffle import Shuffle


class Table:

    max_hands = 3

    def __init__(self, shuffle: Shuffle, min_bet: int = 5, max_bet: int = 200):
        self.min_bet = min_bet
        self.max_bet = max_bet
        self.shuffle = shuffle

    def hit(self) -> Card:
        return self.shuffle.hit()

