from Tools import botTools as bt
from Tools import winTools as wt
from Tools import avControl as avC
from Tools import avMethods as avM
import webhook
import keyboard
import time
import cv2
import pyautogui
import ctypes
from threading import Thread
from datetime import datetime
# Failsafe key
g_toggle = False
key = 'l'
def toggle():
    global g_toggle
    g_toggle = not g_toggle
4
keyboard.add_hotkey(key, toggle)
def click(x,y, delay: int | None=None) -> None:
    if delay is not None:
        delay=delay
    else:
        delay = 0.65
    pyautogui.moveTo(x,y)
    ctypes.windll.user32.mouse_event(0x0001, 0, 1, 0, 0)
    time.sleep(delay)
    pyautogui.click()


# Wait for start screen
def wait_start(delay: int | None = None):
    i = 0
    if delay is None:
        delay = 1
    else:
        delay = delay
    found = False
    while found == False and i<90: # 1 and a half minute
        try: 
            i+=1
            if bt.does_exist('VoteStart.png',0.8,grayscale=True):
                found = True
        except Exception as e:
            print(f"e {e}")
        time.sleep(delay)

def wait_start_two(delay: int | None = None):
    i=0
    if delay is None:
        delay = 1
    else:
        delay = delay
    found = False
    while found == False and i<(90/delay):
        try:
            i+=1
            if not bt.does_exist('VoteStart.png',0.8,grayscale=True):
                found = True
        except Exception as e:
            print(f"erro {e}")
        time.sleep(delay)


# (281, 820), (289, 862), (363, 850), (352, 804)]  - Main shield breakers
# Sell cords: 


def ani_event() -> None:
    start_of_run = datetime.now()
    num_runs = 0
    wins = 0t
    loss = 0
    rewards = 0
    unit_pos=[(962, 768), (995, 729), (1034, 838), (1076, 767), (534, 159), (542, 199), (562, 157), (572, 192), (464, 166), (475, 193), (479, 220), (474, 155)]
    try:
        while True:
            if g_toggle:
                print("started")
                wait_start() # Waits untill it starts
                click(835, 226, delay=0.2)
                click(835, 226, delay=0.2)
                print("clicked start")
                print("waiting for rest to start")
                wait_start_two(0.3)
                time.sleep(0.5)
                print("start")
                keyboard.press_and_release('1')
                keyboard.press("shift")
                click(*unit_pos[0])
                click(*unit_pos[1])
                keyboard.press_and_release('2')
                time.sleep(0.5)
                click(*unit_pos[2])
                click(*unit_pos[3])
                time.sleep(1)
                keyboard.release("shift")
                time.sleep(0.5)
                keyboard.press_and_release("q")
                print("wave")
                wave_2 = False
                while not wave_2 and g_toggle:
                    try:
                        check_wave = avM.get_wave()
                        print(check_wave)
                        if check_wave >= 2:
                            wave_2 = True
                        time.sleep(1)
                    except Exception as e:
                        print(f"Error {e}")
                print("wave found")
                print("start")
                keyboard.press_and_release('1')
                keyboard.press("shift")
                click(*unit_pos[4])
                click(*unit_pos[5])
                keyboard.press_and_release('2')
                time.sleep(0.5)
                click(*unit_pos[6])#[(692, 458), (622, 460)]
                click(*unit_pos[7])
                time.sleep(1)
                keyboard.release("shift")
                keyboard.press_and_release('6')
                time.sleep(0.5)
                click(*unit_pos[8])
                time.sleep(0.5)
                click(621, 458)
                time.sleep(0.5)
                keyboard.press("shift")
                time.sleep(0.5)
                keyboard.press_and_release('3')
                time.sleep(4)
                click(*unit_pos[9])
                keyboard.press_and_release("q")
                time.sleep(1)
                keyboard.release("shift")               
                time.sleep(4.5)
                keyboard.press_and_release('4')
                click(*unit_pos[10])
                time.sleep(1)
                keyboard.press_and_release("q")#[(625, 463), (1015, 670), (1101, 310)]
                click(625, 463)
                click(1015, 670)
                click(1101, 310)
                time.sleep(0.5)
                keyboard.press_and_release('5')
                click(*unit_pos[11])
                time.sleep(0.6)
                match_end = False
                loss = False
                while not match_end and g_toggle:
                    try:
                        regions = (315, 237, 797, 321)
                        check_victory = bt.does_exist("Victory.png",0.8,True, region=regions)
                        check_failure = bt.does_exist("Failed.png", 0.8, True, region=regions)
                        if check_victory:
                            wins+=1
                            match_end = True
                        elif check_failure:
                            loss = True
                            loss+=1
                            match_end = True
                        else:
                            keyboard.press_and_release('t')
                        time.sleep(0.8)
                    
                    except Exception as e:
                        print(f"error {e}" )

                num_runs+=1
                print(f"Victory, runs: {num_runs}")
                try:
                    victory = wt.screen_shot_memory()
                    runtime = f"{datetime.now()-start_of_run}"
                    if not loss:
                        rewards+=5000
                    g = Thread(target=webhook.send_webhook,
                        kwargs={
                                "win": num_runs,
                                "lose": loss,
                                "run_time": f"{str(runtime).split('.')[0]}",
                                "rewards": rewards,
                                "task_name": "Ani Event",
                                "img": victory,
                            },
                        )            
                    g.start()
                except Exception as e:
                    print(f" error {e}")
                time.sleep(1)
                click(709, 703, delay=0.2) 
                click(709, 703, delay=0.2)
            else:   
                print(f"Bot is not on! Turn on bot by pressing {key}")
            time.sleep(1)
    except Exception as e:
        print(f"error {e}")
ani_event()
