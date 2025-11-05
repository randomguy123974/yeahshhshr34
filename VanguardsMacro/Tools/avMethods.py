# AV Methods are methods that are commonly used throught the entire program.


# Tools for click / img detection
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # needed to get py tools
from Tools import botTools as bt
from Tools import winTools as wt

# Inputs
from pyautogui import *
import keyboard
import random
import pydirectinput
import time
import ctypes

# Text Detection
import cv2
import numpy as np
import pytesseract

#Extra
from typing import Literal

window_size = (1100,800)
window_pos = (200,100)

def PrideBurn() -> None:
    '''
    Burns cards for Escanor's Pride (The One) set up.
    '''
    bt.click(551,573)
    for i in range(5):
        bt.click(435+i*75, 720)
        time.sleep(0.25)

def go_to_spawn(delay: float | None=None) -> None:
    '''
    Returns to spawn
    '''
    if delay is None:
        delay = 0.25
    print("Hello")
    time.sleep(delay)
    bt.click(27,769)
    time.sleep(delay)
    bt.click(951,399)
    time.sleep(delay)
    bt.click(948,356)
    time.sleep(delay)
    bt.click(474,455)
    time.sleep(delay)
    bt.click(558,453)
    time.sleep(delay)
    bt.click(1017,166)
    time.sleep(delay*2)

def get_upgrade(region: tuple | None=None, tHold: tuple | None=None) -> str: # Gets the current wave of the match
    '''
    NEED TO BE IN MATCH 
    Returns the wave the player is on.
    '''
    try:
        regionArea = ()
        if region is None:
            x, y, w, h =  401, 407, 560, 429 # [(401, 407), (560, 429)]
            regionArea = (x,y,w,h)
        else:
            regionArea = region
        screenshot = wt.screenshot_region(region=regionArea) # Get image of num
        if tHold is None:
            t1,t2 = 10, 240
        else:
            t1 = tHold[0]
            t2 = tHold[1]
        gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY) # Grayscale for speed
        _, threshold = cv2.threshold(gray, t1, t2, cv2.THRESH_BINARY) # Threshold so only the num is there
        thresh = cv2.resize(threshold, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC) # resize for accuracy
        upg = pytesseract.image_to_string(thresh, config='--psm 7 -c tessedit_char_whitelist=0123456789MAX') # Number detector [0,9] no char
        if not upg.strip():
            return -1
        return upg # Returns the wave that was found
        
    except Exception as e:
        print(f"Error in get_wave: {e}")

def get_wave(new_region: tuple[int, int, int, int] | None = None) -> int: # Gets the current wave of the match
    '''
    NEED TO BE IN MATCH 
    Returns the wave the player is on.
    '''
    try:
        
        x, y, w, h =  477,154,605,179 # Wave num location
        regionArea = (x,y,w,h)
        if new_region is not None:
            regionArea=new_region
        screenshot = wt.screenshot_region(region=regionArea) # Get image of num
    
        gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY) # Grayscale for speed
        _, threshold = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY) # Threshold so only the num is there
        thresh = cv2.resize(threshold, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC) # resize for accuracy
        wave = pytesseract.image_to_string(thresh, config='--psm 7 -c tessedit_char_whitelist=0123456789') # Number detector [0,9] no char
        if not wave.strip():
            return -1
        return int(wave) # Returns the wave that was found
        
    except Exception as e:
        print(f"Error in get_wave: {e}")

def read_stage_challenge() -> str: # Gets the stage before entry
    '''
    Returns what stage the challenge your doing is on
    '''
    try:
        x, y, w, h =  746, 409, 970, 435 # Stage location
        regionArea = (x,y,w,h)
        screenshot = wt.screenshot_region(region=regionArea) # Get image of num
    
        gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY) # Grayscale for speed
        _, threshold = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY) # Threshold so only the num is there
        thresh = cv2.resize(threshold, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC) # resize for accuracy
        stage = pytesseract.image_to_string(thresh, config='--psm 7 -c tessedit_char_whitelist=StorygeAac1234567890') # 
        if not stage.strip():
            return -1
        return stage # Returns the stage that was found
        
    except Exception as e:
        print(f"Error in stage: {e}")

def go_to_upg(Upgrade: int, Delay: int | None=None) -> bool:
    if Delay is None:
        Delay=0.7
    CurUpgrade = 0
    while CurUpgrade < Upgrade:

        def cancel_place(): # Manual cancel
            nonlocal CurUpgrade
            CurUpgrade = Upgrade+1
            return False
            
        keyboard.add_hotkey(';',cancel_place)
        if get_upgrade() == -1:
            continue
        elif get_upgrade() > CurUpgrade or get_upgrade() == "MAX":
            CurUpgrade+=1
        else:
            keyboard.press_and_release('t')
        
        time.sleep(Delay)
    return True
         

def random_place(UnitIndex: int, NumPlacement: int) -> list:
    UnitPositions = []
    Mouse = [546, 422]
    Placed = 0
    while Placed < NumPlacement:

        def cancel_place(): # Manual cancel
            nonlocal Placed
            Placed = NumPlacement
            
        keyboard.add_hotkey(';',cancel_place)

        if bt.does_exist('UnitOpen.png',0.8,grayscale=True):
            Placed+=1
            UnitPositions.append(Mouse.copy())
            print(f"Units Plcaed: {Placed}")
            time.sleep(0.5)
            if NumPlacement!=1:
                bt.click(*(375, 290))
            time.sleep(1.5)
        else:
            keyboard.press_and_release(f'{UnitIndex}')
            bt.click(Mouse[0],Mouse[1])
            # bounding box: (14, 159), (890, 690)
            # Get random x or y offset
            dx = int(random.random()*100) if int(random.random()*2) == 1 else int(random.random()*-100)
            dy = int(random.random()*100) if int(random.random()*2) == 1 else int(random.random()*-100)
            if Mouse[0]+dx <= 14 or Mouse[0]+dx >= 890:
                Mouse[0] = 750
            else:
                Mouse[0]+=dx
            if Mouse[1]+dy <= 159 or Mouse[1]+dy >= 690:
                Mouse[1] = 550
            else:
                Mouse[1]+=dy
            if Mouse in UnitPositions:
                Mouse[1]+=20
                Mouse[0]+=20
            time.sleep(1.5)
    return UnitPositions

def abs_place(UnitIndex: int, NumPlacement: int, Positions: tuple[tuple[int, int],...], Attempts: int | None=None) -> list:
    UnitPositions = []
    Placed = 0
    Attempts = Attempts
    if Attempts is None:
        Attempts = 180
    while Placed < NumPlacement:
        x,y = Positions[Placed]
        
        if Attempts==0:
            return UnitPositions # Fail condition
        
        def cancel_place(): # Manual cancel
            nonlocal Placed
            Placed = NumPlacement

        keyboard.add_hotkey(';',cancel_place)
        
        Attempts-=1
        if bt.does_exist('UnitOpen.png',0.8,grayscale=True):
            UnitPositions.append((x,y))
            Placed+=1
            print("Unit Found")
            time.sleep(0.5)
            bt.click(*(375, 290))
        else:
            keyboard.press_and_release(f'{UnitIndex}')
            time.sleep(0.5)
            bt.click(x,y)
            time.sleep(1.5)
def restart_match():
    '''sybau'''
    #(227, 868), (1150, 454), (681, 565), (726, 570), (1212, 264)
    bt.click(227, 868, abs=True)
    time.sleep(1)
    bt.click(1150, 454, abs=True)
    time.sleep(1)
    bt.click(681, 565, abs=True)
    time.sleep(1)
    bt.click(726, 570, abs=True)
    time.sleep(1)
    bt.click(1212, 264, abs=True)
    time.sleep(1)