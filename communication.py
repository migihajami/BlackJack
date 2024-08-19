from hand_display import HandDisplay
from response_provider import ResponseProvider
from message_sender import MessageSender


class Communication:

    def __init__(self, message_sender: MessageSender, hand_display: HandDisplay, response_provider: ResponseProvider):
        self.message_sender = message_sender
        self.hand_display = hand_display
        self.response_provider = response_provider