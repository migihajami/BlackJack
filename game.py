from HandDisplayBase import HandDisplay
from dealer import Dealer
from palyer_response_provider import PlayerResponseProvider
from player import Player
from shuffle import Shuffle
from stattistics import Statistics
from replit import clear


class Game:
    stats: Statistics

    def __init__(self, player_name, hand_displayer: HandDisplay, shuffle: Shuffle, response_provider: PlayerResponseProvider):
        self.shuffle = shuffle
        self.rounds_passed = 0
        self.score = {"dealer": 0, "player": 0}
        self.stats = Statistics()
        self.hand_displayer = hand_displayer
        self.response_provider = response_provider
        self.player = Player(player_name, self.shuffle, self.hand_displayer, self.response_provider,1)
        self.dealer = Dealer(self.shuffle, self.hand_displayer, 2)
        self.continue_game = "y"

    def get_stats(self) -> Statistics:
        return self.stats

    def run(self):
        while self.continue_game == "y" or self.continue_game == "yes":
            if self.rounds_passed > 0:
                clear()
                print(f"There are {len(self.shuffle)} cards left in the deck")
                print(f"Game No: {self.rounds_passed + 1}")
                print(self.stats)
                print("========================================")

            self.player.hit(0)
            self.dealer.hit()
            self.player.hit(0)
            self.dealer.hit()

            self.hand_displayer.display_card(self.dealer.name, self.dealer.get_first_card())
            print("----------------------------------------")

            if self.dealer.has_blackjack() and not self.player.has_blackjack(0):
                user_value = self.player.get_value(0)
                self.hand_displayer.display_hand(self.player.name, self.player.hands[0])
            else:
                user_value = self.player.make_hand(0)

            self.rounds_passed += 1
            if user_value > 21:
                print("Bust!")
            else:
                if not self.player.has_blackjack(0):
                    dealer_value = self.dealer.make_hand()
                else:
                    dealer_value = self.dealer.get_value()
                    self.hand_displayer.display_hand(self.dealer.name, self.dealer.hands[0])

                if dealer_value < user_value or dealer_value > 21:
                    print("You win!")
                    self.stats.win()
                elif dealer_value == user_value:
                    print("Push.")
                    self.stats.push()
                else:
                    print("You loose.")
                    self.stats.loose()

            self.dealer.flush()
            self.player.flush()
            self.continue_game = self.response_provider.get_response("One more game? ")
