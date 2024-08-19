from hand_display import HandDisplay
from dealer_hand import DealerHand
from player import Player
from shuffle import Shuffle
import time


class Dealer(Player):

    def __init__(self, shuffle: Shuffle, hand_displayer: HandDisplay, time_delay: float = 1.5):
        super().__init__(name="Dealer", shuffle=shuffle, hand_displayer=hand_displayer, hands_amount=1, response_provider=None)
        self.hands = [DealerHand()]
        self.time_delay = time_delay

    def make_hand(self, hand_number: int = 0) -> int:
        hand = self.hands[0]
        value: int = hand.get_value()
        print("----------------------------------------")
        self.hand_displayer.display_hand(self.name, hand)
        while value < 17:
            time.sleep(self.time_delay)
            hand.add_card(self.shuffle.hit())
            value = hand.get_value()
            self.hand_displayer.display_hand(self.name, hand)
            print("------")

        return value

    def get_first_card(self):
        hand = self.hands[0]
        return hand.get_first_card()

    # def show_hand(self, hand_number: int = 0):
    #     hand = self.hands[0]
    #     cards = hand.show_cards()
    #     print(f"Dealer has: {cards}")
    #     if hand.has_blackjack():
    #         print(f"Dealer has BlackJack.")
    #     else:
    #         print(f"Dealer has {hand.get_value()}")
