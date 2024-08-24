from src.black_jack.table import Table
from src.io.communicator import Communicator
from src.black_jack.player import Player, Dealer
from src.statistics import Statistics


class Game:
    stats: Statistics

    def __init__(self, player_name, communicator: Communicator, table: Table):
        self.rounds_passed = 0
        self.score = {"dealer": 0, "player": 0}
        self.communicator = communicator
        self.table = table
        self.player = Player(player_name, self.table, self.communicator, 0)
        self.stats = Statistics(self.player)
        self.dealer = Dealer(self.table, self.communicator, 2)

    def round_init(self):
        self.player.hit(0)
        self.dealer.hit()
        self.player.hit(0)
        self.dealer.hit()

        self.communicator.display_card(self.dealer.name, self.dealer.get_first_card())

    def round_start_messages(self):
        self.communicator.clear()
        self.communicator.send_message(f"There are {len(self.table.shuffle)} cards left in the deck")
        self.communicator.send_message(f"Game No: {self.rounds_passed + 1}")

    def make_bet(self, hand_number: int) -> int:
        bet_amount = self.communicator.get_bet_amount("Please enter bet amount: ")
        if bet_amount < self.table.min_bet or bet_amount > self.table.max_bet:
            self.communicator.send_message(f"Min bet - {self.table.min_bet}, Max bet - {self.table.max_bet}")
            return 0

        return self.player.make_bet(bet_amount, hand_number)

    def run(self):
        bet_amount = self.make_bet(0)
        self.communicator.send_message(self.stats)
        while bet_amount > 0:
            if self.rounds_passed > 0:
                self.round_start_messages()

            self.round_init()

            if self.dealer.has_blackjack() and not self.player.has_blackjack(0):
                user_value = self.player.get_value(0)
                self.communicator.display_hand(self.player.name, self.player.hands[0])
            else:
                user_value = self.player.make_hand(0)
                bet_amount = self.player.hands[0].bet

            self.rounds_passed += 1
            if user_value > 21:
                self.communicator.send_message("Bust!")
                self.stats.loose()
            else:
                if not self.player.has_blackjack(0):
                    dealer_value = self.dealer.make_hand()
                else:
                    dealer_value = self.dealer.get_value()
                    self.communicator.display_hand(self.dealer.name, self.dealer.hands[0])

                if dealer_value < user_value or dealer_value > 21:
                    self.communicator.send_message("You win!")
                    if self.player.has_blackjack():
                        win_amount = bet_amount + bet_amount * 1.5
                    else:
                        win_amount = bet_amount * 2
                    self.player.receive_win(win_amount)
                    self.stats.win()

                elif dealer_value == user_value:
                    self.communicator.send_message("Push.")
                    self.player.receive_win(bet_amount)
                    self.stats.push()
                else:
                    self.communicator.send_message("You loose.")
                    self.stats.loose()

            self.dealer.flush()
            self.player.flush()
            self.communicator.send_message(self.stats)
            bet_amount = self.make_bet(0)
