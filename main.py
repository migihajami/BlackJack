import art
import shuffle
import hand
from card import Card
from replit import clear 

decks = shuffle.stir(1)
continue_game: str = "y"
games_passed: int = 0
score = {"dealer": 0, "player": 0}

print(art.logo)
print("Welcome to the table! Black Jack 21. Dealer must hit on 16 and stop on 17.")

while continue_game == "y" or continue_game == "yes":
    if games_passed > 0:
        clear()
        print(f"There are {len(decks)} cards left in the deck")
        print(f"Game No: {games_passed + 1}")
        print(f"{score['player']} wins, {score['dealer']} looses, {games_passed - score['player'] - score['dealer']} pushes.")
        print("========================================")

    user_card1 = decks.pop(0)
    dealer_card1: Card = decks.pop(0)
    user_card2 = decks.pop(0)

    print(f"Dealer has [{dealer_card1.Nick}] of {dealer_card1.Suit}")
    print("----------------------------------------")

    user_value = hand.make_user_hand(decks, user_card1, user_card2)
    games_passed += 1
    if user_value > 21:
        print("Bust!")
    else:
        dealer_value = hand.make_dealer_hand(decks, dealer_card1)
        if dealer_value < user_value or dealer_value > 21:
            print("You win!")
            score["player"] += 1
        elif dealer_value == user_value:
            print("Push.")
        else:
            print("You loose.")
            score["dealer"] += 1

    continue_game = input("One more game? ")
    if len(decks) < 5:
        decks = shuffle.stir(1)
    