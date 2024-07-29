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

