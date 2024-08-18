import art
from dealer import Dealer
from player import Player
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

print(art.logo)
print("Welcome to the table! Black Jack 21. Dealer must hit on 16 and stop on 17.")

statistics = Statistics()
print(statistics)

name = input("What is your name?")
player = Player(name, shuffle, 1)
dealer = Dealer(shuffle, 2)

while continue_game == "y" or continue_game == "yes":
    if games_passed > 0:
        clear()
        print(f"There are {len(shuffle)} cards left in the deck")
        print(f"Game No: {games_passed + 1}")
        print(statistics)
        print("========================================")

    player.hit(0)
    dealer.hit()
    player.hit(0)
    dealer.hit()

    print(f"Dealer has {dealer.get_first_card()}")
    print("----------------------------------------")

    if dealer.has_blackjack() and not player.has_blackjack(0):
        user_value = player.get_value(0)
        player.show_hand(0)
    else:
        user_value = player.make_hand(0)

    games_passed += 1
    if user_value > 21:
        print("Bust!")
    else:
        if not player.has_blackjack(0):
            dealer_value = dealer.make_hand()
        else:
            dealer_value = dealer.get_value()
            dealer.show_hand()

        if dealer_value < user_value or dealer_value > 21:
            print("You win!")
            statistics.win()
        elif dealer_value == user_value:
            print("Push.")
            statistics.push()
        else:
            print("You loose.")
            statistics.loose()

    dealer.flush()
    player.flush()
    continue_game = input("One more game? ")

    