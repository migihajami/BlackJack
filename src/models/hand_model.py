from typing import List
from pydantic import BaseModel
from src.models.card_model import CardModel


class HandModel(BaseModel):
    bet_amount: int
    cards: List[CardModel]

