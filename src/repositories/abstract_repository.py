from abc import ABC, abstractmethod

from pydantic import BaseModel

from src.io.data_storage import IDataStorage


class IAbstractRepository(ABC):

    def __init__(self, storage: IDataStorage):
        self.storage = storage

    @abstractmethod
    def insert(self, data):
        raise NotImplementedError()

    @abstractmethod
    def get(self, item_id: str) -> BaseModel:
        raise NotImplementedError()

    @abstractmethod
    def get_all(self, item_filter):
        raise NotImplementedError()

    @abstractmethod
    def update(self, data):
        raise NotImplementedError()

    @abstractmethod
    def delete(self, item_id: str):
        raise NotImplementedError()



