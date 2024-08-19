from abc import ABC, abstractmethod


class BaseResponseProvider(ABC):

    @abstractmethod
    def get_response(self, question: str) -> str:
        pass


class ConsoleResponseProvider(BaseResponseProvider):
    
    def get_response(self, question: str) -> str:
        response = input(question)
        return response
