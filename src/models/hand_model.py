from abc import ABC
from typing import List
from pydantic import BaseModel
from src.models.card_model import CardModel


class HandModel(ABC, BaseModel):
    cards: List[CardModel]
    history: List[str]

    def add_card(self, card: CardModel):
        self.cards.append(card)

    def has_blackjack(self):
        return len(self.cards) == 2 and self.get_value() == 21

    def get_value(self):
        result: int = 0
        item: CardModel
        is_soft: bool = False

        for item in self.cards:
            if item.name == 'Ace':
                if result > 10:
                    result += 1
                else:
                    result += 11
                    is_soft = True
            else:
                result += item.value
                if result > 21 and is_soft:
                    result -= 10
                    is_soft = False

        return result

    def flush(self):
        self.cards.clear()


class PlayerHandModel(HandModel):
    bet_amount: float
    is_doubled: bool

    def double(self):
        self.bet_amount *= 2
        self.is_doubled = True

    def flush(self):
        super().flush()
        self.is_doubled = False

    def make_bet(self, bet_amount: float):
        self.bet_amount = bet_amount


class DealerHandModel(HandModel):
    is_hand_made: bool

    def get_first_card(self):
        return self.cards[0]

    def make_hand(self, hit):
        self.is_hand_made = True
        while self.get_value() < 17:
            self.add_card(hit())

    def get_value(self):
        if self.is_hand_made:
            return super().get_value()
        else:
            return self.cards[0].value

    def flush(self):
        self.is_hand_made = False
        super().flush()
