from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.io.data_storage import MemoryStorage
from src.repositories.game_repository import GameRepository
from src.repositories.player_repository import PlayerRepository

router = APIRouter(prefix="/games", tags=["games"], responses={404: {"description": "Not found"}})
player_repo = PlayerRepository(MemoryStorage("player_id"))
game_repo = GameRepository(MemoryStorage("game_id"))


@router.get("/start/{player_id}")
def start(player_id: str) -> str:
    game_id = game_repo.create(player_id)
    return game_id


@router.delete("/finish/{game_id}")
def finish(game_id: str):
    result = game_repo.delete(game_id)
    return result


@router.get("/bet/{game_id}/{bet_amount}")
def make_bet(game_id: str, bet_amount: int):
    game = game_repo.get(game_id)
    if player_repo.withdraw_bet(game.player_id, bet_amount):
        raise NotImplementedError("need to implement it")
    else:
        return JSONResponse(
            status_code=402,
            content={"status": "error", "err_message": "Not enough coins to make this bet"})


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
