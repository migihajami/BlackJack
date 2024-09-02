from pydantic import BaseModel

from src.models.hand_model import DealerHandModel, PlayerHandModel


class GameModel(BaseModel):
    game_id: str
    player_id: str
    player_hand: PlayerHandModel
    dealer_hand: DealerHandModel
    state: str



