# Main handler

#Tools
from Tools import avControl as ac
from Tools import botTools as bt
from Tools import winTools as wt
#States
from globalStates import global_state
#Input
import time
import keyboard
import threading

Initialized = False




#Toggles
def toggle_off() -> None:
    global Initialized
    Initialized = not Initialized
keyboard.add_hotkey('up', toggle_off)

#Listener
def state_update(value: bool):
    global Initialized
    Initialized = value
    if Initialized:
        threading.Thread(target=run).start()
global_state.watch("state", state_update)

def run() -> None:
    global Initialized
    while Initialized == True:

        print("im running")


        time.sleep(0.05)

Started = False
def start_bot(): # Start up sequence
    global Started
    if not Started:

        Started = True

        window = wt.get_window("Roblox") # Get roblox window
        global roblox_window
        roblox_window = window
        
        wt.resize_window(roblox_window, 1100, 800)  # Resize window
        wt.move_window(roblox_window, 200, 100)  # Move window to top left corner
       
        wt.activate_window(window=window) # Activate window

        bt.click(1100//2,800//2)

        time.sleep(0.5)
        bt.click(940, 186) # Exit out of any menu
start_bot()