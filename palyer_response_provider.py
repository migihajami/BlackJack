from abc import ABC, abstractmethod


class PlayerResponseProvider(ABC):

    @abstractmethod
    def get_response(self, question: str) -> str:
        pass


class ConsoleResponseProvider(PlayerResponseProvider):
    def get_response(self, question: str) -> str:
        response = input(question)
        return response
