from pynput import keyboard
import pyautogui
import threading
import time
import random

switch = True
h = "listener"

def on_activate_h():
    global click_thread, movement_thread, switch
    click_thread = threading.Thread(target=printer_loop)
    click_thread.daemon = True 
    click_thread.start()
# If you want to not get kicked for being afk, then delete the comment
    """movement_thread = threading.Thread(target=movement_loop) 
    movement_thread.daemon = True
    movement_thread.start()"""

"""def movement_loop():
    global switch
    print("Started AFK workaround!")
    while switch:
        pyautogui.press('space') 
        #Simulates random keys to prevent AFK timeouts.
        #You can change the keys and timing here.
        pyautogui.press(['b', 'x']) #you can add or change the keys for your favourite moves
        sleep_time = random.uniform(5, 10) # You can change the timing for this afk workaround
        time.sleep(sleep_time)"""

#  The autocliker
def printer_loop():
    global switch
    print("Started clicker")
    while switch:
        pyautogui.click(pyautogui.position()) 
    print("program has been stopped")

def on_activate_i():
    global switch, h
    switch = False
    time.sleep(0.5) 
    h.stop()

with keyboard.GlobalHotKeys({
    'h': on_activate_h,
    'i': on_activate_i
    }) as h: 
    h.join()
