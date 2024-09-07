from typing import List
from pydantic import BaseModel
from src.models.card_model import CardModel
from src.models.game_model import GameStateEnum


class GameRoundModel(BaseModel):
    player_cards: List[CardModel]
    dealer_cards: List[CardModel]
    player_value: int
    dealer_value: int
    round_state: GameStateEnum
    bet_amount: float
