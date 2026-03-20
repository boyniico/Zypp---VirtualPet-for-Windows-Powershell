from service import json_manage as jm
def check_and_reset() -> bool:
    time = jm.load_json("game/timecheck.json")
    if not time["game_start"]:
        DEFAULT_TIME = {
            "game_start": None,
            "newborn": None,
            "last_visit": None,
            "last_food": None,
            "last_bath": None,
            "days": 0
        }
        DEFAULT_PET = {
            "name": None,
            "age": 0,
            "stage": "egg",
            "health": 100,
            "no_hungry": 50,
            "no_dirt": 60,
            "happiness": 90
        }
        DEFAULT_PLAYER = {
            "exp": 0,
            "money": 0,
            "inventory": []
        }
        jm.save_json("game/timecheck.json",DEFAULT_TIME)
        jm.save_json("game/player.json",DEFAULT_PLAYER)
        jm.save_json("game/pet.json",DEFAULT_PET)
        
        return True
    return False
