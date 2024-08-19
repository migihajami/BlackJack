from abc import ABC, abstractmethod


class BaseMessageSender(ABC):

    @abstractmethod
    def send_message(self, message):
        pass


class ConsoleMessageSender(BaseMessageSender):

    def send_message(self, message):
        print(message)
