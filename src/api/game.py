from fastapi import APIRouter

from src.black_jack.game import Game
from src.black_jack.shuffle import Shuffle
from src.black_jack.table import Table
from src.models.table_model import TableModel

router = APIRouter(prefix="/games", tags=["games"], responses={404: {"description": "Not found"}})


@router.get("/{game_id}/table_info")
def get_table_info(game_id: str) -> TableModel:
    pass


@router.get("/start/{table_type}")
def start(table_type: int, player_name: str) -> str:
    table = Table(Shuffle(6), 5, 200)
    game = Game(player_name, None, table)


def finish(game_id: str):
    pass


def make_bet(game_id: str, amount: int):
    pass


def double(game_id: str):
    pass


def get_hand(game_id: str):
    pass


def hit(game_id: str):
    pass


def pass_(game_id: str):
    pass


def surrender(game_id: str):
    pass
