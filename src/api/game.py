from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.io.data_storage import MemoryStorage
from src.models.game_model import GameModel
from src.models.game_round_model import GameRoundModel
from src.models.player_model import PlayerModel
from src.repositories.game_repository import GameRepository
from src.repositories.player_repository import PlayerRepository
from src.services.game_service import GameService

router = APIRouter(prefix="/games", tags=["games"], responses={404: {"description": "Not found"}})
player_repo = PlayerRepository(MemoryStorage[PlayerModel]("player_id"))
game_repo = GameRepository(MemoryStorage[GameModel]("game_id"))


@router.post("/start/{player_id}")
def start(player_id: str) -> GameRoundModel:
    game_id = game_repo.create(player_id)
    game_service = GameService(game_id, game_repo, player_repo)
    return game_service.start_game()


@router.delete("/finish/{game_id}")
def finish(game_id: str):
    result = game_repo.delete(game_id)
    return result


@router.post("/bet/{game_id}/{bet_amount}")
def make_bet(game_id: str, bet_amount: int):
    game_service = GameService(game_id, game_repo, player_repo)
    try:
        game_service.make_bet(bet_amount)
    except ValueError:
        return JSONResponse(
            status_code=402,
            content={"status": "error", "err_message": "Not enough coins to make this bet"})


@router.post("/double/{game_id}")
def double(game_id: str):
    game_service = GameService(game_id, game_repo, player_repo)
    game_service.player_double()


@router.get("/{game_id}")
def get_game(game_id: str):
    game_service = GameService(game_id, game_repo, player_repo)
    return game_service.game_round_model


@router.post("/hit/{game_id}")
def hit(game_id: str):
    game_service = GameService(game_id, game_repo, player_repo)
    return game_service.player_hit()


@router.post("/pass/{game_id}")
def pass_(game_id: str):
    game_service = GameService(game_id, game_repo, player_repo)
    return game_service.player_pass()


@router.post("/surrender/{game_id}")
def surrender(game_id: str):
    game_service = GameService(game_id, game_repo, player_repo)
    return game_service.surrender()
