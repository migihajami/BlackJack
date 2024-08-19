import art
from game import Game
from HandDisplayBase import ConsoleHandDisplay
from palyer_response_provider import ConsoleResponseProvider
from shuffle import Shuffle

print(art.logo)
print("Welcome to the table! Black Jack 21. Dealer must hit on 16 and stop on 17.")

hand_displayer = ConsoleHandDisplay()
shuffle = Shuffle(2)
response_provider = ConsoleResponseProvider()
name = response_provider.get_response("What is your name?")
game = Game(name, hand_displayer, shuffle, response_provider)
print(game.stats)

game.run()
print("Bye!")
print(game.stats)








    