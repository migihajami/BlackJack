import time

from card import Card
from hand import Hand


class DealerHand(Hand):

    def __init__(self, deck: list, card1: Card, card2: Card):
        super().__init__(deck, card1, card2)

    def make_hand(self):
        value: int = self.get_value()
        print("----------------------------------------")
        self.show_hand()
        while value < 17:
            time.sleep(1.5)
            self.cards.append(self.deck.pop(0))
            value = self.get_value()
            self.show_hand()
            print("------")

        return value

    def show_hand(self):
        cards = self.show_cards()
        print(f"Dealer has: {cards}")
        print(f"Dealer has {self.get_value()}")
