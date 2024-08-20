from communicator import Communicator
from dealer_hand import DealerHand
from player import Player
from shuffle import Shuffle
import time


class Dealer(Player):

    def __init__(self, shuffle: Shuffle, communicator: Communicator, time_delay: float = 1.5):
        super().__init__("Dealer", shuffle, communicator, 1)
        self.hands = [DealerHand()]
        self.time_delay = time_delay

    def make_hand(self, hand_number: int = 0) -> int:
        hand = self.hands[0]
        value: int = hand.get_value()
        self.communicator.display_hand(self.name, hand)
        while value < 17:
            time.sleep(self.time_delay)
            hand.add_card(self.shuffle.hit())
            value = hand.get_value()
            self.communicator.display_hand(self.name, hand)

        return value

    def get_first_card(self):
        hand = self.hands[0]
        return hand.get_first_card()

