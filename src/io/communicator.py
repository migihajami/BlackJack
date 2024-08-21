from src.black_jack.card import Card
from src.black_jack.hand import Hand
from src.io.hand_display import HandDisplay
from src.io.response_provider import ResponseProvider
from src.io.message_sender import MessageSender


class Communicator(MessageSender, HandDisplay, ResponseProvider):

    def __init__(self, message_sender: MessageSender, hand_display: HandDisplay, response_provider: ResponseProvider):
        self.message_sender = message_sender
        self.hand_display = hand_display
        self.response_provider = response_provider

    def send_message(self, message):
        self.message_sender.send_message(message)

    def clear(self):
        self.message_sender.clear()

    def display_cards(self, cards: list):
        self.hand_display.display_cards(cards)

    def display_hand(self, name: str, hand: Hand):
        self.hand_display.display_hand(name, hand)

    def display_card(self, name: str, card: Card):
        self.hand_display.display_card(name, card)

    def get_response(self, question: str) -> str:
        return self.response_provider.get_response(question)


