import time

from card import Card
from hand import Hand
from shuffle import Shuffle


class DealerHand(Hand):

    def __init__(self):
        super().__init__()

    def get_first_card(self):
        return self.cards[0]
