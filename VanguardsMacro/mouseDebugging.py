from pyautogui import *
import keyboard
import mouseinfo
import time
from Tools import botTools as bt
from Tools import winTools as wt
import pygetwindow as gw 
import pyautogui
import ctypes


mouse_info = []

window_size = (1100,800)
window_pos = (200,100)

#Togglables
BotOn = True

def relPos(cords):
    x,y = window_pos
    x = cords[0]-x
    y = cords[1]-y
    return  cords

keyboard.add_hotkey('z', lambda: mouse_info.append(relPos(mouseinfo._winPosition()))) 


def bot_toggle():
    global BotOn
    BotOn = not BotOn

keyboard.add_hotkey('n', bot_toggle)


def click(x,y) -> None:
    pyautogui.moveTo(x,y)
    ctypes.windll.user32.mouse_event(0x0001, 0, 1, 0, 0)
    pyautogui.click()

while BotOn:
    time.sleep(0.1)

print(mouse_info)

#off = []

#for i in mouse_info:
   #bt.click(i[0],i[1])
   #click(i[0],i[1])
   #time.sleep(1)
   #off.append(relPos(mouseinfo._winPosition()))
#print(off)

#print(f"offset found: dx = {off[0][0]-mouse_info[0][0]}, dy = {off[0][1]-mouse_info[0][1]}")
#


