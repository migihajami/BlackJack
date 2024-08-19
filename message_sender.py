from abc import ABC, abstractmethod
from replit import clear


class BaseMessageSender(ABC):

    @abstractmethod
    def send_message(self, message):
        pass

    @abstractmethod
    def clear(self):
        pass


class ConsoleMessageSender(BaseMessageSender):

    def send_message(self, message):
        print(message)

    def clear(self):
        clear()
