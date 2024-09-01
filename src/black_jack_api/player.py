import uuid

from src.black_jack_api.savable import Savable, save_post_state


class Player(Savable):

    name: str
    balance: float

    def __init__(self, player_id: str):
        self.player_id = player_id
        self._load_player()

    def __str__(self):
        return self.name

    def _load_player(self):
        pass

    def save_state(self):
        pass

    @save_post_state
    def topup_balance(self, amount: float) -> float:
        self.balance += amount
        return self.balance

    @save_post_state
    def cash_out(self, amount: float) -> float:
        if amount < self.balance:
            raise ValueError("Not enough coins")

        self.balance -= amount
        return self.balance


def create_new_player(name: str, reference: str, balance: float) -> Player:
    player_id = uuid.uuid4().hex
    player = Player(player_id)
    player.name = name
    player.balance = balance
    player.save_state()
    return player

