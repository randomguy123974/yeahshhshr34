import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # needed to get py tools

from pyautogui import *
import time
import keyboard
import pyautogui
import random
import pydirectinput as pyi
import mouseinfo
import ctypes



# Variables
GameStarted = False # Variable to track if the game has started
BotOn = False # Variable to control the bot state

# Methods

def does_exist(imageDirectory: str, confidence: float, grayscale: bool, region: tuple | None=None) -> bool:
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
            return True
        return False
    except Exception as e:
        return False



def click_image(imageDirectory: str, confidence: float, grayscale: bool) -> bool:
    try:
        imageDirectory = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"Resources", imageDirectory)
        image_location = pyautogui.locateOnScreen(imageDirectory, grayscale=grayscale, confidence=confidence)
        if  image_location is not None:
            image_center = pyautogui.center(image_location)
            click(image_center.x-200, image_center.y-100)
            return True
    except Exception as e:
        return False


def click(x: int,y: int, delay: int | None=None, abs: bool | None=None) -> None: # Set curser position and click
    '''
    Click at cordinate x,y
    If cordinate is abs pass in window_pos/topleft (x,y) of the active foregroundww
    '''
    global dx,dy
    dx = 200
    dy= 100
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
    pyautogui.click()
    


if __name__ == "__main__":
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))