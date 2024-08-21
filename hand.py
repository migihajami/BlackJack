from card import Card


class Hand:
    def __init__(self):
        self.cards = []

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

    def flush(self):
        self.cards.clear()


class DealerHand(Hand):

    def __init__(self):
        super().__init__()

    def get_first_card(self):
        return self.cards[0]
