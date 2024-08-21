from abc import ABC, abstractmethod
from replit import clear


class MessageSender(ABC):

    @abstractmethod
    def send_message(self, message):
        pass

    @abstractmethod
    def clear(self):
        pass


class ConsoleMessageSender(MessageSender):

    def send_message(self, message):
        print(message)

    def clear(self):
        clear()
