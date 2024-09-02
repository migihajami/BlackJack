from fastapi import APIRouter
from src.black_jack.game import Game
from src.io.data_storage import MemoryStorage
from src.repositories.game_repository import GameRepository
from src.repositories.player_repository import PlayerRepository

router = APIRouter(prefix="/games", tags=["games"], responses={404: {"description": "Not found"}})
player_repo = PlayerRepository(MemoryStorage("player_id"))
game_repo = GameRepository(MemoryStorage("game_id"))

@router.get("/start/{player_id}")
def start(player_id: str) -> str:
    player = player_repo.get(player_id)
    game = game_repo.insert()


def finish(game_id: str):
    pass


def make_bet(game_id: str, amount: int):
    pass


def double(game_id: str):
    pass


def get_hand(game_id: str):
    pass


def get_dealer_hand(game_id: str):
    pass


def hit(game_id: str):
    pass


def pass_(game_id: str):
    pass


def surrender(game_id: str):
    pass
