import pyautogui
import time
pyautogui.FAILSAFE = False
while True:
    print("CLICK")
    time.sleep (118)
    for i in range(0, 3):
        pyautogui.press( 'p')
        #pyautogui.click()