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


def choose_card():
    if True:
        card_priority = {
            "Champions": "Champions.png",
            "Quake": "Quake.png",
            "Immunity":"immunity.png",
            "Revitalize": "Revitalize.png",
            "Thrice": "Thrice.png"
        }
        found = False
        for i,e in enumerate(card_priority):
            # i is index, e is Element
            print(f"{i} | {e}")
            check = bt.does_exist(card_priority.get(e), 0.8, False)
            print(check)
            if check:
                print(f"found {e}")
                found = True
                bt.click_image(card_priority.get(e), 0.8, False)
                break
        if not found:
            pass
    
def path_to_spawn():
    pos = bt.does_exist("test_spawn.png",0.8,True,region=(200,100,1300,900), ret_pos=True)
   
    if pos is not None:
        bt.click(pos.x,pos.y,right=True)