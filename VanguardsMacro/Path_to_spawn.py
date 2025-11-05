from Tools import botTools as bt
import pyautogui
import keyboard
import time
import os
import ctypes

# Failsafe key
g_toggle = True
key = 'l'
def toggle():
    global g_toggle
    g_toggle = not g_toggle

keyboard.add_hotkey(key, toggle)

#EE393c

def does_exist(imageDirectory: str, confidence: float, grayscale: bool, region: tuple | None=None) -> tuple | None:
    print("h")
    try:
        print("b")
        name = imageDirectory
        imageDirectory = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "Resources",
        imageDirectory)
        if region is None:
            check = pyautogui.locateOnScreen(imageDirectory, grayscale=grayscale, confidence=confidence)
        else:
            check = pyautogui.locateOnScreen(imageDirectory, grayscale=grayscale, confidence=confidence, region=region)

        print(check)
        image_center = pyautogui.center(check)
        
        if check is not None:
            return image_center
        return None
    except Exception as e:
        return None

def click(x: int,y: int, delay: int | None=None, abs: tuple[int, int] | None = None) -> None: # Set curser position and click
    '''
    Click at cordinate x,y
    If cordinate is abs pass in window_pos/topleft (x,y) of the active foregroundww
    '''
    global dx,dy
    if abs is not None:
        x-=abs[0]
        y-=abs[1]
    if delay is None:
        delay = 0.1 # Standard click delaya
    else:
        delay=delay
    pyautogui.moveTo(x+200,y+100)
    time.sleep(delay)
    ctypes.windll.user32.mouse_event(0x0001, 0, 1, 0, 0)
    pyautogui.rightClick()
    

pos = does_exist("test_spawn.png",0.8,True,region=(200,100,1300,900))

time.sleep(1)
if pos is not None:
    click(pos.x-200, pos.y-100)
    click(pos.x-200, pos.y-100)

