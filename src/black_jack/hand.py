from src.black_jack.card import Card


class Hand:
    def __init__(self, min_bet: int, max_bet: int):
        self.cards = []
        self.bet = 0
        self.min_bet = min_bet
        self.max_bet = max_bet
        self.is_doubled = False

    def get_value(self):
        result: int = 0
        item: Card
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

    def has_blackjack(self):
        return len(self.cards) == 2 and self.get_value() == 21

    def add_card(self, card: Card):
        self.cards.append(card)

    def make_bet(self, amount: int) -> bool:
        if amount < self.min_bet or amount > self.max_bet:
            return False

        self.bet = amount
        return True

    def double(self):
        self.bet *= 2
        self.is_doubled = True

    def flush(self):
        self.cards.clear()
        self.is_doubled = False


class DealerHand(Hand):

    def __init__(self):
        super().__init__(0,0)

    def get_first_card(self):
        return self.cards[0]
