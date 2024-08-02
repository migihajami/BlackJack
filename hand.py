import card
import time


class Dealer:

    def __init__(self):
        pass


class Hand:

    def __init__(self):
        pass

    def get_value(self, cards: list):
        result: int = 0
        item: card.Card

        # TODO need to rewrite aces calculation
        for item in cards:
            if item.Name == 'Ace':
                if result > 10:
                    result += 1
                else:
                    result += 11
            else:
                result += item.Value
        return result

    def show_cards(self, user_hand: list, is_dealer: bool = False):
        item: card.Card

        if is_dealer:
            print("Dealer has: ")
        else:
            print("Your cards:")

        for item in user_hand:
            print(f"[{item.Nick}] of {item.Suit}")

    def show_hand(self, hand: list, is_dealer: bool = False):
        self.show_cards(hand, is_dealer)
        if is_dealer:
            print(f"Dealer has {self.get_value(hand)}")
        else:
            print(f"Your hand has value of '{self.get_value(hand)}")

    def make_user_hand(self, decks: list, card1: card.Card, card2: card.Card):
        user_hand = []
        user_hand.append(card1)
        user_hand.append(card2)
        need_more: bool = True
        value: int = self.get_value(user_hand)

        print("----------------------------------------")
        self.show_hand(user_hand)

        while need_more and value < 21:
            need_more_str = input("Need more?")
            need_more = need_more_str.lower() == "y" or need_more_str.lower() == "yes"
            if need_more:
                user_hand.append(decks.pop(0))
                value = self.get_value(user_hand)
                print("------")
                self.show_hand(user_hand)

        return value

    def make_dealer_hand(self, decks: list, first_card: card.Card):
        dealer_hand = [first_card, decks.pop(0)]

        value: int = self.get_value(dealer_hand)
        print("----------------------------------------")
        self.show_hand(dealer_hand, True)
        while value < 17:
            time.sleep(1.5)
            dealer_hand.append(decks.pop(0))
            value = self.get_value(dealer_hand)
            self.show_hand(dealer_hand, True)
            print("------")

        return value
