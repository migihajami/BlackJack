from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.io.data_storage import MemoryStorage
from src.models.game_model import GameModel
from src.models.player_model import PlayerModel
from src.repositories.game_repository import GameRepository
from src.repositories.player_repository import PlayerRepository

router = APIRouter(prefix="/players", tags=["players"], responses={404: {"description": "Not found"}})
player_repo = PlayerRepository(MemoryStorage[PlayerModel]("player_id"))
game_repo = GameRepository(MemoryStorage[GameModel]("game_id"))


@router.get("/{player_id}")
def get_player(player_id: str):
    try:
        return player_repo.get(player_id)
    except KeyError:
        return JSONResponse(status_code=404, content="")


@router.post("", description="Add new player")
def add_player(player: PlayerModel):
    result = player_repo.insert(player)
    return result


@router.get("", description="Get all players")
def get_all():
    return player_repo.get_all("")


@router.patch("/{player_id}", description="Update player's fields")
def update_player(player_id: str, player: PlayerModel):
    player_repo.update(player)


@router.put("/{player_id}/topup_balance", description="Topup player's balance")
def topup_balance(player_id: str, amount: float):
    player = player_repo.get(player_id)
    player.balance += amount
    player_repo.update(player)


@router.get("/{player_id}/games", description="Get player's games")
def get_games(player_id: str):
    games = game_repo.get_player_games(player_id)
    return games

