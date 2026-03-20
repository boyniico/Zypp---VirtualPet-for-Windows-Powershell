import os
import time
def cls() -> None:
    os.system('cls')
def cls_print(text: str) -> None:
    cls()
    print(text)
def wait(seconds: float) -> None:
    time.sleep(seconds)