import art
import shuffle
import hand
from replit import clear 


decks = shuffle.stir(1)

print(art.logo)
print("Welcome to the table! Black Jack 21. Dealer must hit on 16 and stop on 17.")

print(len(decks))

continue_game: str = "y"
games_passed: int = 0

while continue_game == "y" or continue_game == "yes":
    if games_passed > 0:
        clear()
        print(f"There are {len(decks)} cards left in the deck")
        print(f"Game No: {games_passed + 1}")

    user_value = hand.make_user_hand(decks)
    games_passed += 1
    if user_value > 21:
        print("Bust!")
    
    continue_game = input("One more game? ")
    if len(decks) < 5:
        decks = shuffle.stir(1)
    