import logging

from fastapi import FastAPI
from src.api import player, game
import uvicorn

logging.basicConfig(level=logging.DEBUG)
app = FastAPI()
app.include_router(player.router)
app.include_router(game.router)


@app.get("/tables/open/{option}")
async def open_table(option: str):
    if option.lower() != "private":
        error_message = "only private tables allowed"
        return {"status": "err", "error_message": error_message}
    return {"message": "Welcome to BlackJack table", "table_id": 21}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8100)


'''
TODO

api requests we need:

authorize
get balance

game:
    open table
    get statistics
    buy chips
    make a bet
    hit
    double
    split
    add hand
    remove hand
    surrender
    give tips
    make a side bet
    

append wallet

bonuses:
    take daily bonus
    retrieve wallet bonus
    get daily quizz
    response daily quizz
    retrieve quizz bonus
    check invite friend bonuses
    retrieve invite friend bonus
    
'''
