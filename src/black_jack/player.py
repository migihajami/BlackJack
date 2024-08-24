import time
from src.black_jack.table import Table
from src.io.communicator import Communicator
from src.black_jack.hand import Hand, DealerHand
from src.black_jack.shuffle import Shuffle
from abc import ABC, abstractmethod


class AbstractPlayer(ABC):

    def __init__(self, name: str, table: Table, communicator: Communicator):
        self.name = name
        self.table = table
        self.hands = [Hand(5, 200)]
        self.communicator = communicator

    def hit(self, hand_number: int = 0):
        hand = self.hands[hand_number]
        hand.add_card(self.table.hit())

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

    def __init__(self, name: str, table: Table, communicator: Communicator, balance: int):
        super().__init__(name, table, communicator)
        self.balance = balance

    def __str__(self):
        return self.name

    def make_bet(self, bet_amount: int, hand_number: int) -> int:
        if bet_amount > self.balance:
            self.communicator.send_message("Not enough balance to make this bet")
            return 0

        self.balance -= bet_amount
        self.hands[hand_number].make_bet(bet_amount)
        return bet_amount

    def double(self, hand_number: int):
        self.make_bet(self.hands[hand_number].bet, hand_number)
        self.hands[hand_number].double()

    def receive_win(self, amount: float):
        self.balance += amount

    def add_hand(self):
        self.hands.append(Hand(self.table.min_bet, self.table.max_bet))

    def remove_hand(self, hand_number: int = 0):
        if len(self.hands) > 1:
            self.hands.pop(hand_number)

    def make_hand(self, hand_number: int = 0) -> int:
        hand = self.hands[hand_number]
        need_more = True
        value = hand.get_value()

        self.communicator.display_hand(self.name, self.hands[hand_number])

        while need_more and value < 21 and not self.hands[hand_number].is_doubled:
            need_more_str = self.communicator.get_response("Need more?")
            need_more = need_more_str.lower() == "y" or need_more_str.lower() == "yes" or need_more_str.lower() == "d"
            if need_more:
                if need_more_str.lower() == "d":
                    self.double(hand_number)
                hand.cards.append(self.table.hit())
                value = hand.get_value()
                self.communicator.display_hand(self.name, self.hands[hand_number])

        return value


class Dealer(AbstractPlayer):

    def __init__(self, table: Table, communicator: Communicator, time_delay: float = 1.5):
        super().__init__("Dealer", table, communicator)
        self.hands = [DealerHand()]
        self.time_delay = time_delay

    def make_hand(self, hand_number: int = 0) -> int:
        hand = self.hands[0]
        value: int = hand.get_value()
        self.communicator.display_hand(self.name, hand)
        while value < 17:
            time.sleep(self.time_delay)
            hand.add_card(self.table.hit())
            value = hand.get_value()
            self.communicator.display_hand(self.name, hand)

        return value

    def get_first_card(self):
        hand = self.hands[0]
        return hand.get_first_card()
