from src import art
from src.io.communicator import Communicator
from src.black_jack.game import Game
from src.io.hand_display import ConsoleHandDisplay
from src.io.message_sender import ConsoleMessageSender
from src.io.response_provider import ConsoleResponseProvider
from src.black_jack.shuffle import Shuffle

message_sender = ConsoleMessageSender()
hand_displayer = ConsoleHandDisplay(message_sender)
shuffle = Shuffle(2)
response_provider = ConsoleResponseProvider()


message_sender.send_message(art.logo)
message_sender.send_message("Welcome to the table! Black Jack 21. Dealer must hit on 16 and stop on 17.")
name = response_provider.get_response("What is your name?")
communicator = Communicator(message_sender, hand_displayer, response_provider)
game = Game(name, shuffle, communicator)
message_sender.send_message(game.stats)

game.run()
message_sender.send_message("Bye!")
message_sender.send_message(game.stats)








    