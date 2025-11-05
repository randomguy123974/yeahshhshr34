import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # needed to get py tools

from pyautogui import *
import time
import pyautogui
import pydirectinput as pyi
import ctypes

from globalValues import global_values

# Methods

def does_exist(imageDirectory: str, confidence: float, grayscale: bool, region: tuple | None=None, ret_pos: bool | None = None) -> bool:
    try:
       
        name = imageDirectory
        imageDirectory = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "Resources",
        imageDirectory)
        if region is None:
            check = pyautogui.locateOnScreen(imageDirectory, grayscale=grayscale, confidence=confidence)
        else:
            check = pyautogui.locateOnScreen(imageDirectory, grayscale=grayscale, confidence=confidence, region=region)
        if check is not None:
            if ret_pos is not None and True:
                return pyautogui.center(check)
            else:
                return True
        return False
    except Exception as e:
        return False



def click_image(imageDirectory: str, confidence: float, grayscale: bool, region: tuple[int,int,int,int] | None = None) -> bool:
    try:
        
        imageDirectory = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"Resources", imageDirectory)
        if region is None:
            image_location = pyautogui.locateOnScreen(imageDirectory, grayscale=grayscale, confidence=confidence)
        else:
            image_location = pyautogui.locateOnScreen(imageDirectory, grayscale=grayscale, confidence=confidence, region=region)
        if  image_location is not None:
            image_center = pyautogui.center(image_location)
            click(image_center.x, image_center.y, abs=True)
            return True
    except Exception as e:
        return False


def click(x: int,y: int, delay: int | None=None, abs: bool | None=None, right: bool | None = None) -> None: # Set curser position and click
    '''
    Click at cordinate x,y
    If cordinate is abs pass in window_pos/topleft (x,y) of the active foregroundww
    '''
    dx = global_values.dx
    dy = global_values.dy
    if abs is not None:
        dx = 0
        dy = 0
    if delay is None:
        delay = 0.1 # Standard click delaya
    else:
        delay=delay
    pyautogui.moveTo(x+dx,y+dy)
    time.sleep(delay)
    ctypes.windll.user32.mouse_event(0x0001, 0, 1, 0, 0)
    if right is None:
        pyautogui.click()
    elif right is not None and True:
        pyautogui.rightClick()
    


if __name__ == "__main__":
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))