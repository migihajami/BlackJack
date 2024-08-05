from card import Card
from shuffle import Shuffle

class Hand:
    def __init__(self, shuffle: Shuffle, card1: Card, card2: Card):
        self.cards = [card1, card2]
        self.shuffle = shuffle

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

    def show_cards(self):
        item: Card
        result: list = []
        for item in self.cards:
            result.append(f"{item}")

        return str.join("\n", result)

    def show_hand(self):
        cards = self.show_cards()
        print(f"Your cards: {cards}")
        if self.has_blackjack():
            print(f"You have BlackJack!")
        else:
            print(f"Your hand has value of '{self.get_value()}")

    def has_blackjack(self):
        return len(self.cards) == 2 and self.get_value() == 21

    def make_hand(self):
        need_more: bool = True
        value: int = self.get_value()

        print("----------------------------------------")
        self.show_hand()

        while need_more and value < 21:
            need_more_str = input("Need more?")
            need_more = need_more_str.lower() == "y" or need_more_str.lower() == "yes"
            if need_more:
                self.cards.append(self.shuffle.hit())
                value = self.get_value()
                print("------")
                self.show_hand()

        return value


