import time

from communicator import Communicator
from dealer_hand import DealerHand
from hand import Hand
from shuffle import Shuffle
from abc import ABC, abstractmethod


class AbstractPlayer(ABC):

    def __init__(self, name: str, shuffle: Shuffle, communicator: Communicator, hands_amount: int = 1):
        self.name = name
        self.shuffle = shuffle
        self.hands = []
        self.communicator = communicator
        for i in range(hands_amount):
            self.hands.append(Hand())

    def hit(self, hand_number: int = 0):
        hand = self.hands[hand_number]
        hand.add_card(self.shuffle.hit())

    def has_blackjack(self, hand_number: int = 0):
        hand = self.hands[hand_number]
        return hand.has_blackjack()

    def get_value(self, hand_number: int = 0):
        hand = self.hands[hand_number]
        return hand.get_value()

    def flush(self):
        for hand in self.hands:
            hand.flush()

    @abstractmethod
    def make_hand(self, hand_number: int = 0) -> int:
        pass


class Player(AbstractPlayer):

    def __init__(self, name: str, shuffle: Shuffle, communicator: Communicator, hands_amount: int = 1):
        super().__init__(name, shuffle, communicator, hands_amount)

    def __str__(self):
        return self.name

    def add_hand(self):
        self.hands.append(Hand())

    def remove_hand(self, hand_number: int = 0):
        if len(self.hands) > 1:
            self.hands.pop(hand_number)

    def make_hand(self, hand_number: int = 0) -> int:
        hand = self.hands[hand_number]
        need_more: bool = True
        value: int = hand.get_value()

        self.communicator.display_hand(self.name, self.hands[hand_number])

        while need_more and value < 21:
            need_more_str = self.communicator.get_response("Need more?")
            need_more = need_more_str.lower() == "y" or need_more_str.lower() == "yes"
            if need_more:
                hand.cards.append(self.shuffle.hit())
                value = hand.get_value()
                self.communicator.display_hand(self.name, self.hands[hand_number])

        return value


class Dealer(AbstractPlayer):

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
