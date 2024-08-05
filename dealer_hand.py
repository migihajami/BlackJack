import time

from card import Card
from hand import Hand
from shuffle import Shuffle


class DealerHand(Hand):

    def __init__(self, shuffle: Shuffle, card1: Card, card2: Card):
        super().__init__(shuffle, card1, card2)

    def make_hand(self):
        value: int = self.get_value()
        print("----------------------------------------")
        self.show_hand()
        while value < 17:
            time.sleep(1.5)
            self.cards.append(self.shuffle.hit())
            value = self.get_value()
            self.show_hand()
            print("------")

        return value

    def show_hand(self):
        cards = self.show_cards()
        print(f"Dealer has: {cards}")
        print(f"Dealer has {self.get_value()}")
