from src.models.game_round_model import GameRoundModel
from src.repositories.game_repository import GameRepository
from src.repositories.player_repository import PlayerRepository


class GameService:

    def __init__(self, game_id: str, game_repo: GameRepository, player_repo: PlayerRepository):
        self.game_repo = game_repo
        self.game_id = game_id
        self.player_repo = player_repo

    def __game_model__(self):
        return self.game_repo.get(self.game_id)

    @property
    def game_round_model(self):
        game_model = self.game_repo.get(self.game_id)
        round_model = GameRoundModel(
            round_state=game_model.state,
            dealer_cards=[game_model.dealer_hand.get_first_card()],
            dealer_value=game_model.dealer_hand.get_value(),
            player_cards=game_model.player_hand.cards,
            player_value=game_model.player_hand.get_value(),
            bet_amount=game_model.player_hand.bet_amount
        )
        return round_model

    def get_game_model(self):
        game_model = self.__game_model__()
        return game_model

    def player_hit(self):
        game_model = self.__game_model__()
        card = game_model.hit()
        game_model.player_hand.add_card(card)
        self.game_repo.update(game_model)
        return self.game_round_model

    def player_double(self):
        game_model = self.__game_model__()
        if self.player_repo.withdraw_coins(game_model.player_id, game_model.current_bet_amount):
            game_model.current_bet_amount *= 2
            game_model.player_hand.double()

    def player_pass(self):
        return self.__dealer_make_hand()

    def __dealer_make_hand(self):
        game_model = self.__game_model__()
        game_model.dealer_hand.make_hand(game_model.hit)
        self.game_repo.update(game_model)
        return self.game_round_model

    def start_game(self):
        game_model = self.__game_model__()
        game_model.init_game()
        self.game_repo.update(game_model)
        return self.game_round_model

    def make_bet(self, bet_amount: float):
        game_model = self.__game_model__()
        if not self.player_repo.withdraw_coins(game_model.player_id, bet_amount):
            raise ValueError("Not enough coins")

        game_model.player_hand.make_bet(bet_amount)
        game_model.init_game()
        game_model.state = "bet_is_made"
        self.game_repo.update(game_model)
        return self.game_round_model

    def finish_game(self):
        game_model = self.__game_model__()
        if game_model.current_bet_amount > 0:
            #TODO: transfer amount to casino balance
            pass

        game_model.finish_game()
        self.game_repo.update(game_model)
        return game_model

    def tips(self, tips_amount):
        game_model = self.__game_model__()
        player = self.player_repo.withdraw_coins(game_model.player_id, tips_amount)

        #TODO transfer tips to casino

    def surrender(self):
        game_model = self.__game_model__()
        if game_model.dealer_hand.get_first_card().name == 'Ace':
            raise ValueError("Can't surrender against Ace")

        self.player_repo.surrender(game_model.player_id, game_model.current_bet_amount/2)
        return self.finish_game()
