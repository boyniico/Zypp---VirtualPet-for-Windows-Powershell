from ui import interaction
from ui.screen import cls
from ui import sprites
from service import json_manage
from datetime import datetime, date
from service import checks

checks.check_and_reset()

time = json_manage.load_json("game/timecheck.json")
zypp = json_manage.load_json("game/pet.json")
food = json_manage.load_json("game/food.json")
player = json_manage.load_json("game/player.json")
zyppsprites = json_manage.load_json("game/zyppsprite.json")