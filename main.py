import art
import shuffle
import hand
import card
from replit import clear 


decks = shuffle.stir(1)

print(art.logo)
print("Welcome to the table! Black Jack 21. Dealer must hit on 16 and stop on 17.")

print(len(decks))
#print(decks)

def show_cards(user_hand: list):
    item: card.Card

    print("Your cards:")
    for item in user_hand:
        print(f"{item.Name} of {item.Suit}")

def show_user_hand(user_hand: list):
    show_cards(user_hand)
    print(f"Your hand has value of '{hand.get_value(user_hand)}")

def make_user_hand():
    user_hand = []
    user_hand.append(decks.pop(0))
    user_hand.append(decks.pop(0))
    needMore: bool = True
    value: int = 0

    show_user_hand(user_hand)

    while needMore and value < 21:
        need_more_str = input("Need more?")
        needMore = need_more_str.lower() == "y" or need_more_str.lower() == "yes"
        if needMore:
            user_hand.append(decks.pop(0))
            value = hand.get_value(user_hand)
            show_user_hand(user_hand)

    return value


continue_game: str = "y"
games_passed: int = 0

while continue_game == "y" or continue_game == "yes":
    if games_passed > 0:
        clear()
        print(f"Game No: {games_passed + 1}")

    user_value = make_user_hand()
    games_passed += 1
    if user_value > 21:
        print("Bust!")
    
    continue_game = input("One more game? ")
    