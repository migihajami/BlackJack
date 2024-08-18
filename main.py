import art
from game import Game
from HandDisplayBase import ConsoleHandDisplay

print(art.logo)
print("Welcome to the table! Black Jack 21. Dealer must hit on 16 and stop on 17.")

hand_displayer = ConsoleHandDisplay()
name = input("What is your name?")
game = Game(name, hand_displayer, 2)
print(game.stats)

game.run()
print("Bye!")
print(game.stats)








    