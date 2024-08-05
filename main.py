import art
from shuffle import Shuffle
from hand import Hand
from dealer_hand import DealerHand
from card import Card
from replit import clear
from stattistics import  Statistics

shuffle = Shuffle(2)

continue_game: str = "y"
games_passed: int = 0
score = {"dealer": 0, "player": 0}

print("Spade - \u2660")

print(art.logo)
print("Welcome to the table! Black Jack 21. Dealer must hit on 16 and stop on 17.")

statistics = Statistics()
print(statistics)

while continue_game == "y" or continue_game == "yes":
    if games_passed > 0:
        clear()
        print(f"There are {len(shuffle)} cards left in the deck")
        print(f"Game No: {games_passed + 1}")
        print(statistics)
        print("========================================")

    user_card1 = shuffle.hit()
    dealer_card1: Card = shuffle.hit()
    user_card2 = shuffle.hit()
    dealer_card2: Card = shuffle.hit()

    user_hand = Hand(shuffle, user_card1, user_card2, )
    dealer_hand = DealerHand(shuffle, dealer_card1, dealer_card2)

    print(f"Dealer has {dealer_card1}")
    print("----------------------------------------")

    if dealer_hand.has_blackjack() and not user_hand.has_blackjack():
        user_value = user_hand.get_value()
        user_hand.show_hand()
    else:
        user_value = user_hand.make_hand()

    games_passed += 1
    if user_value > 21:
        print("Bust!")
    else:
        if not user_hand.has_blackjack():
            dealer_value = dealer_hand.make_hand()
        else:
            dealer_value = dealer_hand.get_value()
            dealer_hand.show_hand()

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

    