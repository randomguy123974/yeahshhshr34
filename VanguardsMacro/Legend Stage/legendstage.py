import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Tools import botTools as bt
from Tools import winTools as wt
from Tools import avControl as avC
from Tools import avMethods as avM
import webhook
from datetime import datetime
import keyboard
import time

# Failsafe key
g_toggle = False
key = 'l'
def toggle():
    print("toggled")
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
def choose_card():
    if g_toggle:
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

def pride_stage() -> None:
    start_of_run = datetime.now()
    num_runs = 0
    wins = 0
    loss = 0
    rewardsmin = 0
    rewardsmax = 0
    while True:
        if g_toggle:
            match_end = False
            check_victory = bt.does_exist("Victory.png",0.8,True)
            check_failure = bt.does_exist("Failed.png", 0.8, True)
            if check_victory or check_failure:
                bt.click(645, 703, abs=True)
            time.sleep(1)
            choose_card()
            check_place = bt.does_exist("Unit_Does_Exist.png", 0.8, True, (1058, 424, 1107, 468))
            if not check_place:
                wait_start() # Waits untill it starts
            time.sleep(1)
            bt.click(637,128) # Starts match
            unit_placed = False
            while not unit_placed and g_toggle:
                check_place = bt.does_exist("Unit_Does_Exist.png", 0.8, True, (1058, 424, 1107, 468))
                if check_place:
                    keyboard.press_and_release('q')
                    unit_placed = True
                else:
                    #775, 420
                    bt.click(x=775, y=420, delay=0.5, abs=True)
                    time.sleep(0.5)
                    keyboard.press_and_release('1')
                    bt.click(x=775, y=420, delay=0.2, abs=True)
                time.sleep(1)
            time.sleep(0.5)
            bt.click(382, 286)
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
            wave_11 = False
            while not wave_11 and g_toggle:
                check_wave = avM.get_wave()
                if check_wave >= 11:
                    bt.click(880,430) # Use ultimate
                    wave_11 = True
                time.sleep(1)
            while not match_end and g_toggle:
                check_victory = bt.does_exist("Victory.png",0.8,True)
                check_failure = bt.does_exist("Failed.png", 0.8, True)
                if check_victory or check_failure:
                    match_end = True
            num_runs+=1
            rewardsmin+=19
            rewardsmax+=24
            print(f"Victory, runs: {num_runs}")
            victory = wt.screen_shot_memory()
            runtime = f"{datetime.now()-start_of_run}"
            webhook.send_webhook(win=num_runs, lose=loss,run_time=f"{str(runtime).split('.')[0] }", rewards=0, task_name="Sukuna Boss Rush", img=victory, rewardsmin=rewardsmin, rewardsmax=rewardsmax)
            time.sleep(3)
            bt.click(645, 703, abs=True)
            time.sleep(2)
        else:   
            print(f"Bot is not on! Turn on bot by pressing {key}")
            time.sleep(1)
#pride_stage()
