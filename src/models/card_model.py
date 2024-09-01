from pydantic import BaseModel


class CardModel(BaseModel):
    name: str
    value: int
    suit: str
    nick: str
