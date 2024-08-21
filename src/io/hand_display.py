from abc import ABC, abstractmethod
from src.black_jack.card import Card
from src.black_jack.hand import Hand
from src.io.message_sender import MessageSender


class HandDisplay(ABC):

    @abstractmethod
    def display_cards(self, cards: list):
        pass

    @abstractmethod
    def display_hand(self, name: str, hand: Hand):
        pass

    @abstractmethod
    def display_card(self, name: str, card: Card):
        pass


class ConsoleHandDisplay(HandDisplay):

    def __init__(self, message_sender: MessageSender):
        self.message_sender = message_sender

    def display_card(self, name: str, card: Card):
        self.message_sender.send_message(f"{name} has {card}")

    def display_hand(self, name: str, hand: Hand):
        cards = hand.cards
        self.message_sender.send_message(f"{name}'s cards: {" ".join([str(card) for card in cards])}")
        if hand.has_blackjack():
            self.message_sender.send_message(f"{name} has BlackJack!")
        else:
            self.message_sender.send_message(f"{name}'s hand has value of '{hand.get_value()}")

    def display_cards(self, cards: list):
        self.message_sender.send_message(cards)
