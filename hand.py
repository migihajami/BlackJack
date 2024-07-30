import card
import time

def get_value(cards: list):
    result: int = 0
    item: card.Card

    #TODO need to rewrite aces calculation
    for item in cards:
        if item.Name == 'Ace':
            if result > 10:
                result += 1
            else:
                result += 11
        else:
            result += item.Value
    return result

def show_cards(user_hand: list, is_dealer: bool = False):
    item: card.Card

    if is_dealer:
        print("Dealer has: ")
    else:
        print("Your cards:")

    for item in user_hand:
        print(f"[{item.Nick}] of {item.Suit}")

def show_hand(hand: list, is_dealer: bool = False):
    show_cards(hand, is_dealer)
    if is_dealer:
        print(f"Dealer has {get_value(hand)}")
    else:
        print(f"Your hand has value of '{get_value(hand)}")

def make_user_hand(decks: list, card1: card.Card, card2: card.Card):
    user_hand = []
    user_hand.append(card1)
    user_hand.append(card2)
    needMore: bool = True
    value: int = get_value(user_hand)

    print("----------------------------------------")
    show_hand(user_hand)

    while needMore and value < 21:
        need_more_str = input("Need more?")
        needMore = need_more_str.lower() == "y" or need_more_str.lower() == "yes"
        if needMore:
            user_hand.append(decks.pop(0))
            value = get_value(user_hand)
            print("------")
            show_hand(user_hand)

    return value

def make_dealer_hand(decks: list, first_card: card.Card):
    dealer_hand = []
    dealer_hand.append(first_card)
    dealer_hand.append(decks.pop(0))
    
    value: int = get_value(dealer_hand)
    print("----------------------------------------")
    show_hand(dealer_hand, True)
    while value < 17:
        time.sleep(1.5)
        dealer_hand.append(decks.pop(0))
        value = get_value(dealer_hand)
        show_hand(dealer_hand, True)
        print("------")
    
    return value
        

