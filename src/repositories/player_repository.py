import uuid
from src.io.data_storage import IDataStorage
from src.models.player_model import PlayerModel
from src.repositories.abstract_repository import IAbstractRepository


class PlayerRepository(IAbstractRepository):
    _ENTITY_NAME = "player"

    def __init__(self,  storage: IDataStorage):
        super().__init__(storage)

    def insert(self, data):
        data.player_id = uuid.uuid4().hex
        return self.storage.insert(self._ENTITY_NAME, data)

    def get(self, item_id: str) -> PlayerModel:
        return self.storage.get(self._ENTITY_NAME, item_id)

    def get_all(self, item_filter):
        return self.storage.get_all(self._ENTITY_NAME)

    def update(self, data):
        return self.storage.update(self._ENTITY_NAME, data)

    def delete(self, item_id: str):
        return self.storage.delete(self._ENTITY_NAME, item_id)

    def topup_balance(self, player_id: str, amount: float):
        player = self.storage.get(self._ENTITY_NAME, player_id)
        player.balance += amount
        self.storage.update(self._ENTITY_NAME, player)

    def withdraw_coins(self, player_id: str, amount: float):
        player = self.storage.get(self._ENTITY_NAME, player_id)
        if player.balance < amount:
            return False

        player.balance -= amount
        self.storage.update(self._ENTITY_NAME, player)
        return True

    def win(self, player_id: str, amount: float):
        player = self.storage.get(self._ENTITY_NAME, player_id)
        player.wins += 1
        player.balance += amount
        self.storage.update(self._ENTITY_NAME, player)

    def push(self, player_id: str, returned_amount: float):
        player = self.storage.get(self._ENTITY_NAME, player_id)
        player.pushes += 1
        player.balance += returned_amount
        self.storage.update(self._ENTITY_NAME, player)

    def loose(self, player_id: str):
        player = self.storage.get(self._ENTITY_NAME, player_id)
        player.looses += 1
        self.storage.update(self._ENTITY_NAME, player)

    def surrender(self, player_id: str, returned_amount: float):
        player = self.storage.get(self._ENTITY_NAME, player_id)
        player.looses += 1
        player.balance += returned_amount
        self.storage.update(self._ENTITY_NAME, player)