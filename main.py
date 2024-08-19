import art
from game import Game
from hand_display import ConsoleHandDisplay
from message_sender import ConsoleMessageSender
from response_provider import ConsoleResponseProvider
from shuffle import Shuffle

message_sender = ConsoleMessageSender()
hand_displayer = ConsoleHandDisplay(message_sender)
shuffle = Shuffle(2)
response_provider = ConsoleResponseProvider()


message_sender.send_message(art.logo)
message_sender.send_message("Welcome to the table! Black Jack 21. Dealer must hit on 16 and stop on 17.")
name = response_provider.get_response("What is your name?")
game = Game(name, hand_displayer, shuffle, response_provider, message_sender)
message_sender.send_message(game.stats)

game.run()
message_sender.send_message("Bye!")
message_sender.send_message(game.stats)








    