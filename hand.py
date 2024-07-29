import card

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

def show_cards(user_hand: list):
    item: card.Card

    print("Your cards:")
    for item in user_hand:
        print(f"{item.Name} of {item.Suit}")

def show_user_hand(user_hand: list):
    show_cards(user_hand)
    print(f"Your hand has value of '{get_value(user_hand)}")

def make_user_hand(decks: list):
    user_hand = []
    user_hand.append(decks.pop(0))
    user_hand.append(decks.pop(0))
    needMore: bool = True
    value: int = get_value(user_hand)

    show_user_hand(user_hand)

    while needMore and value < 21:
        need_more_str = input("Need more?")
        needMore = need_more_str.lower() == "y" or need_more_str.lower() == "yes"
        if needMore:
            user_hand.append(decks.pop(0))
            value = get_value(user_hand)
            show_user_hand(user_hand)

    return value
