from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.io.data_storage import MemoryStorage
from src.models.player_model import PlayerModel
from src.repositories.player_repository import PlayerRepository

router = APIRouter(prefix="/players", tags=["players"], responses={404: {"description": "Not found"}})
storage = MemoryStorage[PlayerModel]("player_id")
repo = PlayerRepository(storage)


@router.get("/{player_id}")
def get_player(player_id: str):
    try:
        return repo.get(player_id)
    except KeyError:
        return JSONResponse(status_code=404, content="")


@router.post("", description="Add new player")
def add_player(player: PlayerModel):
    result = repo.insert(player)
    return result


@router.get("", description="Get all players")
def get_all():
    return repo.get_all("")


@router.patch("/{player_id}", description="Update player's fields")
def update_player(player_id: str, player: PlayerModel):
    repo.update(player)


@router.put("/{player_id}/topup_balance", description="Topup player's balance")
def topup_balance(player_id: str, amount: float):
    player = repo.get(player_id)
    player.balance += amount
    repo.update(player)
