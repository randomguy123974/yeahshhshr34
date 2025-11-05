from Tools import botTools as bt
from Tools import winTools as wt
from Tools import avControl as avC
from Tools import avMethods as avM
import webhook
import keyboard
import time
import cv2
from datetime import datetime
# Failsafe key
g_toggle = False
key = 'l'
def toggle():
    global g_toggle
    g_toggle = not g_toggle

keyboard.add_hotkey(key, toggle)

# Wait for start screen
def wait_start(delay: int | None = None):
    if delay is None:
        delay = 1
    else:
        delay = delay
    found = False
    while found == False:
        if bt.does_exist('VoteStart.png',0.8,grayscale=True):
            found = True
        time.sleep(delay)

def sbr_raid() -> None:
    start_of_run = datetime.now()
    num_runs = 0
    wins = 0
    loss = 0
    while True:
        if g_toggle:
            print("started")
            wait_start() # Waits untill it starts
            avM.PrideBurn()
            time.sleep(1)
            bt.click(637,128) # Starts match
            unit_placed = False
            while not unit_placed and g_toggle:
                check_place = bt.does_exist("Unit_Does_Exist.png", 0.8, True, (1058, 424, 1107, 468))
                if check_place:
                    keyboard.press_and_release('q')
                    unit_placed = True
                else:
                    bt.click(x=357, y=418, delay=0.5)
                    time.sleep(0.5)
                    keyboard.press_and_release('1')
                    bt.click(x=357, y=418, delay=0.2) # 357, 418), (382, 286)
                time.sleep(1)
            time.sleep(0.5)
            bt.click(382, 286)
            print("Placed")
            max_upgrade = False
            while not max_upgrade and g_toggle:
                upg_region = (946,368,1138,431)
                check_upgrade = bt.does_exist("max.png",0.8,True,upg_region)
                if check_upgrade:
                    max_upgrade = True
                else:
                    bt.click(792,343)
                time.sleep(1)
            print("Max upgrade")
            wave_16 = False
            while not wave_16 and g_toggle:
                check_wave = avM.get_wave()
                if check_wave >= 16:
                    bt.click(880,430) # Use ultimate
                    wave_16 = True
                time.sleep(1)
            nuke_boss = False
            match_end = False
            while not nuke_boss and g_toggle:
                check_boss = bt.does_exist("Diogo.png",0.8,True)
                check_victory = bt.does_exist("Victory.png",0.8,True)
                check_failure = bt.does_exist("Failed.png", 0.8, True)
                if check_boss:
                    nuke_boss = True
                    bt.click(798,431) # Nuke sukuna
                if check_victory:
                    wins+=1
                    match_end = True
                elif check_failure:
                    loss+=1
                    match_end = True
            while not match_end and g_toggle:
                check_victory = bt.does_exist("Victory.png",0.8,True)
                check_failure = bt.does_exist("Failed.png", 0.8, True)
                if check_victory:
                    wins+=1
                    match_end = True
                elif check_failure:
                    loss+=1
                    match_end = True
            num_runs+=1
            print(f"Victory, runs: {num_runs}")
            victory = wt.screen_shot_memory()
            runtime = f"{datetime.now()-start_of_run}"
            webhook.send_webhook(win=num_runs, lose=loss,run_time=f"{str(runtime).split('.')[0] }", rewards=0, task_name="SBR Raid", img=victory)
            time.sleep(3)
            bt.click(377, 600)
            time.sleep(2)
        else:   
            print(f"Bot is not on! Turn on bot by pressing {key}")
        time.sleep(1)
sbr_raid()

