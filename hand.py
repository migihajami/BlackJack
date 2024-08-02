from card import Card
import time


class Dealer:

    def __init__(self):
        self.hand = Hand()

    def show_hand(self):
        pass


class Hand:

    def __init__(self, deck: list, card1: Card, card2: Card, is_dealer: bool):
        self.cards = [card1, card2]
        self.deck = deck
        self.is_dealer = is_dealer

    def get_value(self):
        result: int = 0
        item: Card

        # TODO need to rewrite aces calculation
        for item in self.cards:
            if item.Name == 'Ace':
                if result > 10:
                    result += 1
                else:
                    result += 11
            else:
                result += item.Value
        return result

    def show_cards(self):
        item: Card

        if self.is_dealer:
            print("Dealer has: ")
        else:
            print("Your cards:")

        for item in self.cards:
            print(f"[{item.Nick}] of {item.Suit}")

    def show_hand(self):
        self.show_cards()
        if self.is_dealer:
            print(f"Dealer has {self.get_value()}")
        else:
            print(f"Your hand has value of '{self.get_value()}")

    def make_hand(self):
        if self.is_dealer:
            return self.make_dealer_hand()
        else:
            return self.make_user_hand()

    def make_user_hand(self):
        need_more: bool = True
        value: int = self.get_value()

        print("----------------------------------------")
        self.show_hand()

        while need_more and value < 21:
            need_more_str = input("Need more?")
            need_more = need_more_str.lower() == "y" or need_more_str.lower() == "yes"
            if need_more:
                self.cards.append(self.deck.pop(0))
                value = self.get_value()
                print("------")
                self.show_hand()

        return value

    def make_dealer_hand(self):

        value: int = self.get_value()
        print("----------------------------------------")
        self.show_hand()
        while value < 17:
            time.sleep(1.5)
            self.cards.append(self.deck.pop(0))
            value = self.get_value()
            self.show_hand()
            print("------")

        return value
