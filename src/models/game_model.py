from enum import Enum
from typing import List

from pydantic import BaseModel

from src.models.card_model import CardModel
from src.models.hand_model import DealerHandModel, PlayerHandModel


class GameStateEnum(Enum):
    UNKNOWN = 1
    INITIALIZING = 2
    WAITING_PLAYER = 3
    WAITING_DEALER = 4
    WAITING_FOR_BET = 5
    ROUND_FINISHED = 6


class GameModel(BaseModel):
    game_id: str
    player_id: str
    player_hand: PlayerHandModel
    dealer_hand: DealerHandModel
    state: GameStateEnum
    current_bet_amount: float
    deck: List[CardModel]

    def hit(self) -> CardModel:
        card = self.deck.pop(0)
        return card

    def init_game(self):
        self.player_hand.flush()
        self.dealer_hand.flush()
        self.player_hand.add_card(self.hit())
        self.dealer_hand.add_card(self.hit())
        self.player_hand.add_card(self.hit())
        self.dealer_hand.add_card(self.hit())

    def finish_game(self):
        self.current_bet_amount = 0
        self.dealer_hand.flush()
        self.player_hand.flush()
        self.deck.clear()
