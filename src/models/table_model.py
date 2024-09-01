from typing import List
from pydantic import BaseModel


class TableModel(BaseModel):

    min_bet: int
    max_bet: int
    max_hands: int
    occupied_hands: List[int]

