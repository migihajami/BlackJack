from abc import ABC, abstractmethod
from card import Card
from hand import Hand


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
    def display_card(self, name: str, card: Card):
        print(f"{name} has {card}")

    def display_hand(self, name: str, hand: Hand):
        cards = hand.cards
        print(f"{name}'s cards: {" ".join([str(card) for card in cards])}")
        if hand.has_blackjack():
            print(f"{name} has BlackJack!")
        else:
            print(f"{name}'s hand has value of '{hand.get_value()}")

    def display_cards(self, cards: list):
        print(cards)
