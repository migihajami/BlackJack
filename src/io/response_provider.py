from abc import ABC, abstractmethod


class ResponseProvider(ABC):

    @abstractmethod
    def get_response(self, question: str) -> str:
        pass

    @abstractmethod
    def get_bet_amount(self, question: str) -> int:
        pass


class ConsoleResponseProvider(ResponseProvider):

    def get_response(self, question: str) -> str:
        response = input(question)
        return response

    def get_bet_amount(self, question: str) -> int:
        response = float(input(question))
        return int(response)
