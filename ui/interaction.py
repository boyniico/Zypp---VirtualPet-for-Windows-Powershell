import getpass
from ui.screen import cls
from ui.sprites import get_progress_bar

# These three functions below present the game interactive interface.
# They're complete shit for how simple they are, but they work.

def press_enter(prompt: str = "[Press Enter]",
                cls_before: bool = False) -> None:
    if cls_before:
        cls()
    getpass.getpass(prompt)
    cls()
    return None

def insert_answer(title: str = "", question: str = "",
        cls_after: bool = False) -> str:
    if title:
        width = len(max([title]+[question], key=len))+2
        sep = "-"*width
        print(sep)
        print(title.center(width))
        print(sep)
    if question:
        print(question)
    answer = input("[> ")
    if cls_after:
        cls()
    return answer

def show_menu(
        options: list,
        title: str = "",
        optionzero: str = "",
        cls_after: bool = False
) -> str:
    # you have NO IDEA what writing this took, for real
    enum_options = []
    for i, option in enumerate(options,1):
        enum_options.append(f" {i}. {option} ")
    if optionzero:
        enum_options.append(f" 0. {optionzero} ")
    width = len(max(enum_options+[title], key=len))
    if width % 2 != 0:
        width += 3
    else:
        width += 2
    sep = "-"*width
    if title:
        print(sep)
        print(title.center(width))
    print(sep)
    for i in enum_options:
        print(i)
    print(sep)
    return insert_answer(cls_after=cls_after)

# This is where you feel like a mother watching your kid's needs
# Stupid Zypp, wish it could buy and eat its own Electric Pizza
def show_zypp_menu(zypp: dict, zypp_sprite: str, days: int) -> str:
    
    # Real Attributes of the Zypp
    name = zypp.get("name")
    stage = zypp.get("stage")
    age = zypp.get("age")
    health = zypp.get("health")
    hungry = zypp.get("no_hungry")
    dirt = zypp.get("no_dirt")
    happy = zypp.get("happiness")

    if not name:
        zname = "your Zypp"

    WIDTH = 5*9
    sep = "*"*WIDTH
    print(sep)
    print(f"Here is {zname}".center(WIDTH))
    print()
    print(zypp_sprite.center(WIDTH))
    print()
    print(f"Age: {age} | Stage of {zname}: {stage}".center(WIDTH))
    if stage != "egg":
        print()
        print(f"Health: {health}/100           Hungry: {hungry}/100")
        print(f"{get_progress_bar(health)}           {get_progress_bar(hungry)}")
        print()
        print(f"Dirt: {dirt}/100              Happiness: {happy}/100")
        print(f"{get_progress_bar(dirt)}          {get_progress_bar(happy)}")
        print()
        print(sep)
        print("1. BATH TIME")
        print("2. FOOD TIME")
        print("3. SHOPPING")
    if stage == "egg":
        print(f"Days to hatch: {3 - days}".center(WIDTH))
    print(sep)

# I need three cups of coffee now