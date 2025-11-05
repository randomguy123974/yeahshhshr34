# AV Control servers to be the main controller for the macro.

# Tools
from Tools import botTools as bt
from Tools import winTools as wt

# Inputs
import pyautogui
import keyboard
import time

def go_to(Area: str) -> None:
    '''
    Goes to a certain option, uses offsets from the arrea_offsets {} dictionary
    '''

    # Dict
    area_offsets = {
        "Story": (121, 514),
        "Raid": (290, 513),
        "Challenges": (456, 523),
        "Dungeon": (624, 512),
        "Worldlines": (289, 673),
        "Odyssey": (117, 668)
    }

    bt.click_image("Areas.png", confidence=0.8, grayscale=True)
    time.sleep(1)
    bt.click(area_offsets[Area][0],area_offsets[Area][1]) 
    time.sleep(3)

    if Area == "Story":
        keyboard.press('w')
        time.sleep(0.8)
        keyboard.release('w')
        keyboard.press('d')
        time.sleep(5)
        keyboard.release('d')
    elif Area == "Raid":
        keyboard.press('w')
        time.sleep(2.6)
        keyboard.release('w')
        keyboard.press('d')
        time.sleep(5)
        keyboard.release('d')
    elif Area == "Challenges":
        keyboard.press('d')
        time.sleep(0.1)
        keyboard.press('shift')
        time.sleep(2)
        keyboard.release('d')
        keyboard.release('shift')
    elif Area == "Dungeon":
        keyboard.press('w')
        keyboard.press('d')
        time.sleep(0.1)
        keyboard.press('shift')
        time.sleep(3)
        keyboard.release('w')
        keyboard.release('d')
        keyboard.release('shift') 
    elif Area == "Worldlines":
        keyboard.press('w')
        time.sleep(0.5)
        keyboard.release('w')
        keyboard.press_and_release('e')
        time.sleep(1)
    elif Area == "Odyssey":
        keyboard.press('w')
        time.sleep(0.1)
        keyboard.press('shift')
        time.sleep(4.5)
        keyboard.release('w')
        keyboard.release('shift') 
        keyboard.press_and_release('e')
        time.sleep(3)
        keyboard.press_and_release('q')
