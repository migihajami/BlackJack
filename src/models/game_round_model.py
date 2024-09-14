from enum import Enum
from typing import List
from pydantic import BaseModel
from src.models.card_model import CardModel
from src.models.game_model import GameStateEnum


class RoundResultEnum(Enum):
    NOT_FINISHED = 1
    PLAYER_WIN = 2
    DEALER_WIN = 3
    PUSH = 4


class GameRoundModel(BaseModel):
    player_cards: List[CardModel]
    dealer_cards: List[CardModel]
    player_value: int
    dealer_value: int
    round_state: GameStateEnum
    bet_amount: float
    round_result: RoundResultEnum
