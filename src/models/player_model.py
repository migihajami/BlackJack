from pydantic import BaseModel


class PlayerModel(BaseModel):
    name: str
    player_id: str
    balance: float
    wins: int
    looses: int
    pushes: int
    surrenders: int

    def __str__(self):
        return self.name
