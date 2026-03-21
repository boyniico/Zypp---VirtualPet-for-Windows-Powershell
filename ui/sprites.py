from service import json_manage

def get_progress_bar(value: int) -> str:
    """value = 0–100 (por ejemplo hunger, cleanliness, etc.)"""
    PROGRESS = json_manage.load_json("game/ui_sprites.json")["progress_bar"]
    if value == 0:
        return PROGRESS["empty"]
    elif value <= 20:
        return PROGRESS["twenty"]
    elif value <= 40:
        return PROGRESS["forty"]
    elif value <= 60:
        return PROGRESS["sixty"]
    elif value <= 80:
        return PROGRESS["eighty"]
    else:
        return PROGRESS["full"]

def select_sprite() -> str:
    pet = json_manage.load_json("game/pet.json")
    zyppsprite = json_manage.load_json("game/zyppsprite.json")
    timecheck = json_manage.load_json("game/timecheck.json")
    
    stage = pet["stage"]
    health = pet["health"]
    hungry = pet["no_hungry"]
    dirt = pet["no_dirt"]
    happy = pet["happiness"]
    
    if stage == "egg":
        if timecheck["days"] < 3:
            return zyppsprite[stage]["normal"]
        else:
            return zyppsprite[stage]["broken"]
    elif health <= 30:
        return zyppsprite[stage]["sick"]
    if hungry <= 30:
        return zyppsprite[stage]["hungry"]
    elif dirt <= 30:
        return zyppsprite[stage]["dirt"]
    if happy >= 70:
        return zyppsprite[stage]["happy"]
    else:
        return zyppsprite[stage]["normal"]
    
# WHO THE FUCK IS GONNA PLAY THIS