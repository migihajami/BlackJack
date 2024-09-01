import uuid


class Game:

    def __init__(self, table_type: str):
        self.game_id = uuid.uuid4()
        self.current_round_id = 0

    def __str__(self):
        pass

    def _save_state(self):
        pass

    def _start_round(self):
        self.current_round_id += 1

    def give_out(self):
        pass

    def make_action(self, hand_id: int, action_type: str):
        pass

    def _make_dealer_hand(self):
        pass

    def get_hand_info(self, hand_id: int):
        pass

    def get_round_info(self, round_id: str):
        pass

