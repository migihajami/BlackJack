from abc import ABC, abstractmethod
from typing import List
from pydantic import BaseModel

from src.io.bj_logging import log_execution


class IDataStorage(ABC):

    def __init__(self, field_id: str):
        self.field_id = field_id

    @abstractmethod
    def get(self, entity_name: str, entity_id: str) -> BaseModel:
        raise NotImplementedError()

    @abstractmethod
    def insert(self, entity_name: str, entity: BaseModel) -> str:
        raise NotImplementedError()

    @abstractmethod
    def update(self, entity_name: str, entity: BaseModel) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get_all(self, entity_name: str) -> List[BaseModel]:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, entity_name: str, entity_id: str):
        raise NotImplementedError()


class MemoryStorage(IDataStorage):
    entities = {}

    def __init__(self, field_id: str):
        super().__init__(field_id)

    @log_execution
    def insert(self, entity_name: str, entity: BaseModel) -> str:
        entity_id = getattr(entity, self.field_id)
        self._check_entity(entity_name)

        if entity_id in self.entities[entity_name].keys():
            raise KeyError(f"id '{entity_id}' already exists")

        self.entities[entity_name][entity_id] = entity
        return entity_id

    @log_execution
    def update(self, entity_name: str, entity: BaseModel) -> bool:
        self._check_entity(entity_name)
        entity_id = getattr(entity, self.field_id)
        if entity_id not in self.entities[entity_name]:
            raise KeyError(f"No such entity - {entity_name}.{entity_id}")

        self.entities[entity_name][entity_id] = entity
        return True

    @log_execution
    def get_all(self, entity_name: str) -> List[BaseModel]:
        self._check_entity(entity_name)
        return self.entities.get(entity_name, [])

    @log_execution
    def get(self, entity_name: str, entity_id: str) -> BaseModel:
        self._check_entity(entity_name)
        return self.entities[entity_name][entity_id]

    @log_execution
    def delete(self, entity_name: str, entity_id: str):
        self._check_entity(entity_name)
        del self.entities[entity_name][entity_id]

    def _check_entity(self, entity_name: str):
        if entity_name not in self.entities.keys():
            self.entities[entity_name] = {}
