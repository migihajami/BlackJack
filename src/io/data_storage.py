from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Dict
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import json
from src.io.bj_logging import log_execution
from src.models.game_model import GameModel
from src.models.player_model import PlayerModel

T = TypeVar('T')


class IDataStorage(ABC, Generic[T]):

    def __init__(self, field_id: str):
        self.field_id = field_id

    @abstractmethod
    def get(self, entity_name: str, entity_id: str) -> T:
        raise NotImplementedError()

    @abstractmethod
    def insert(self, entity_name: str, entity: T) -> str:
        raise NotImplementedError()

    @abstractmethod
    def update(self, entity_name: str, entity: T) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get_all(self, entity_name: str) -> List[T]:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, entity_name: str, entity_id: str):
        raise NotImplementedError()


class MemoryStorageEntities(BaseModel):
    player: Dict[str, PlayerModel]
    game: Dict[str, GameModel]


class MemoryStorage(IDataStorage, Generic[T]):
    entities = MemoryStorageEntities(player={}, game={})
    FILENAME = "src/MemoryStorageDump.json"

    def __init__(self, field_id: str):
        super().__init__(field_id)
        self._load_state()

    @property
    def __get_entity_dict(self) -> Dict[str, T]:
        entity_dict: Dict[str, T]
        match self.field_id:
            case 'game_id':
                entity_dict = self.entities.game
            case 'player_id':
                entity_dict = self.entities.player
            case _:
                raise KeyError(f"Id of entity '{self.field_id} is not defined")
        return entity_dict

    @log_execution
    def insert(self, entity_name: str, entity: T) -> str:
        entity_id = getattr(entity, self.field_id)

        if entity_id in self.__get_entity_dict.keys():
            raise KeyError(f"id '{entity_id}' already exists")

        self.__get_entity_dict[entity_id] = entity
        self._save_state()
        return entity_id

    @log_execution
    def update(self, entity_name: str, entity: T) -> bool:
        entity_id = getattr(entity, self.field_id)
        if entity_id not in self.__get_entity_dict:
            raise KeyError(f"No such entity - {entity_name}.{entity_id}")

        self.__get_entity_dict[entity_id] = entity
        self._save_state()
        return True

    @log_execution
    def get_all(self, entity_name: str) -> List[T]:
        return [self.__get_entity_dict[entity] for entity in self.__get_entity_dict]

    @log_execution
    def get(self, entity_name: str, entity_id: str) -> T:
        return self.__get_entity_dict[entity_id]

    @log_execution
    def delete(self, entity_name: str, entity_id: str):
        del self.__get_entity_dict[entity_id]
        self._save_state()

    def _save_state(self):
        with open(self.FILENAME, "w") as file:
            data = self.entities.model_dump_json()
            file.write(data)

    def _load_state(self):
        try:
            file = open(self.FILENAME, "r")
        except OSError:
            return

        with file:
            data = file.read()
            self.entities = MemoryStorageEntities.model_validate_json(json_data=data)

