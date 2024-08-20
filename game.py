from communicator import Communicator
from dealer import Dealer
from player import Player
from shuffle import Shuffle
from stattistics import Statistics


class Game:
    stats: Statistics

    def __init__(self, player_name, shuffle: Shuffle, communication: Communicator):
        self.shuffle = shuffle
        self.rounds_passed = 0
        self.score = {"dealer": 0, "player": 0}
        self.stats = Statistics()
        self.communication = communication
        self.player = Player(player_name, self.shuffle, self.communication, 1)
        self.dealer = Dealer(self.shuffle, self.communication, 2)
        self.continue_game = "y"

    def get_stats(self) -> Statistics:
        return self.stats

    def round_init(self):
        self.player.hit(0)
        self.dealer.hit()
        self.player.hit(0)
        self.dealer.hit()

        self.communication.display_card(self.dealer.name, self.dealer.get_first_card())
        self.communication.send_message("----------------------------------------")

    def round_start_messages(self):
        self.communication.clear()
        self.communication.send_message(f"There are {len(self.shuffle)} cards left in the deck")
        self.communication.send_message(f"Game No: {self.rounds_passed + 1}")
        self.communication.send_message(self.stats)
        self.communication.send_message("========================================")

    def run(self):
        while self.continue_game == "y" or self.continue_game == "yes":
            if self.rounds_passed > 0:
                self.round_start_messages()

            self.round_init()

            if self.dealer.has_blackjack() and not self.player.has_blackjack(0):
                user_value = self.player.get_value(0)
                self.communication.display_hand(self.player.name, self.player.hands[0])
            else:
                user_value = self.player.make_hand(0)

            self.rounds_passed += 1
            if user_value > 21:
                self.communication.send_message("Bust!")
            else:
                if not self.player.has_blackjack(0):
                    dealer_value = self.dealer.make_hand()
                else:
                    dealer_value = self.dealer.get_value()
                    self.communication.display_hand(self.dealer.name, self.dealer.hands[0])

                if dealer_value < user_value or dealer_value > 21:
                    self.communication.send_message("You win!")
                    self.stats.win()
                elif dealer_value == user_value:
                    self.communication.send_message("Push.")
                    self.stats.push()
                else:
                    self.communication.send_message("You loose.")
                    self.stats.loose()

            self.dealer.flush()
            self.player.flush()
            self.continue_game = self.communication.get_response("One more game? ")
