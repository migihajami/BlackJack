from abc import ABC
from typing import List
from pydantic import BaseModel
from src.models.card_model import CardModel


class HandModel(ABC, BaseModel):
    cards: List[CardModel]
    history: [str]

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


class DealerHandModel(HandModel):

    def get_first_card(self):
        return self.cards[0]

