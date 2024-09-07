import uuid

from pydantic import BaseModel

from src.io.data_storage import IDataStorage
from src.models.card_model import CardModel
from src.models.game_model import GameModel, GameStateEnum
from src.models.hand_model import DealerHandModel, PlayerHandModel
from src.repositories.abstract_repository import IAbstractRepository
from src.services.shuffle_service import ShuffleService


class GameRepository(IAbstractRepository):
    _ENTITY_NAME = "game"

    def __init__(self,  storage: IDataStorage):
        super().__init__(storage)

    def insert(self, data):
        data.game_id = uuid.uuid4().hex
        self.storage.insert(self._ENTITY_NAME, data)

    def get(self, item_id: str) -> GameModel:
        return self.storage.get(self._ENTITY_NAME, item_id)

    def get_all(self, item_filter):
        return self.storage.get_all(self._ENTITY_NAME)

    def update(self, data):
        return self.storage.update(self._ENTITY_NAME, data)

    def delete(self, item_id: str):
        return self.storage.delete(self._ENTITY_NAME, item_id)

    def create(self, player_id: str):
        shuffle = ShuffleService(6)

        game = GameModel(game_id=uuid.uuid4().hex,
                         player_id=player_id,
                         player_hand=PlayerHandModel(bet_amount=0, cards=[], history=[], is_doubled=False),
                         dealer_hand=DealerHandModel(cards=[], history=[], is_hand_made=False),
                         state=GameStateEnum.WAITING_FOR_BET,
                         current_bet_amount=0,
                         deck=shuffle.deck)
        return self.storage.insert(self._ENTITY_NAME, game)

    def add_player_card(self, game_id: str, card: CardModel):
        game = self.get(game_id)
        game.player_hand.add_card(card)
        self.update(game)

    def add_dealer_card(self, game_id: str, card: CardModel):
        game = self.get(game_id)
        game.dealer_hand.add_card(card)
        self.update(game)


