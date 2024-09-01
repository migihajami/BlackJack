import uuid
from src.io.data_storage import IDataStorage
from src.models.player_model import PlayerModel
from src.repositories.abstract_repository import IAbstractRepository


class PlayerRepository(IAbstractRepository):
    ENTITY_NAME = "player"

    def __init__(self,  storage: IDataStorage):
        super().__init__(storage)

    def insert(self, data):
        data.player_id = uuid.uuid4().hex
        return self.storage.insert(self.ENTITY_NAME, data)

    def get(self, item_id: str) -> PlayerModel:
        return self.storage.get(self.ENTITY_NAME, item_id)

    def get_all(self, item_filter):
        return self.storage.get_all(self.ENTITY_NAME)

    def update(self, data):
        return self.storage.update(self.ENTITY_NAME, data)

    def delete(self, item_id: str):
        return self.storage.delete(self.ENTITY_NAME, item_id)

