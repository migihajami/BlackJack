from abc import ABC, abstractmethod


class ResponseProvider(ABC):

    @abstractmethod
    def get_response(self, question: str) -> str:
        pass


class ConsoleResponseProvider(ResponseProvider):

    def get_response(self, question: str) -> str:
        response = input(question)
        return response
