import art
import shuffle
import hand
import card



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

user_hand = []
user_hand.append(decks.pop(0))



needMore: bool = True
while needMore:
    user_hand.append(decks.pop(0))
    clear()
    show_cards(user_hand)
    print(f"Your hand has value of '{hand.get_value(user_hand)}")