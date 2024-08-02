import art
from shuffle import Shuffle
from hand import Hand, DealerHand
from card import Card
from replit import clear
from stattistics import  Statistics

shuffle = Shuffle(1)
decks = shuffle.stir()

continue_game: str = "y"
games_passed: int = 0
score = {"dealer": 0, "player": 0}

print(art.logo)
print("Welcome to the table! Black Jack 21. Dealer must hit on 16 and stop on 17.")

statistics = Statistics()
print(statistics)

while continue_game == "y" or continue_game == "yes":
    if games_passed > 0:
        clear()
        print(f"There are {len(decks)} cards left in the deck")
        print(f"Game No: {games_passed + 1}")
        print(statistics)
        print("========================================")

    user_card1 = decks.pop(0)
    dealer_card1: Card = decks.pop(0)
    user_card2 = decks.pop(0)
    dealer_card2: Card = decks.pop(0)

    user_hand = Hand(decks, user_card1, user_card2, )
    dealer_hand = DealerHand(decks, dealer_card1, dealer_card2)

    print(f"Dealer has [{dealer_card1.Nick}] of {dealer_card1.Suit}")
    print("----------------------------------------")

    user_value = user_hand.make_hand()
    games_passed += 1
    if user_value > 21:
        print("Bust!")
    else:
        dealer_value = dealer_hand.make_hand()
        if dealer_value < user_value or dealer_value > 21:
            print("You win!")
            statistics.win()
        elif dealer_value == user_value:
            print("Push.")
            statistics.push()
        else:
            print("You loose.")
            statistics.loose()

    continue_game = input("One more game? ")
    if len(decks) < 5:
        decks = shuffle.stir()
    