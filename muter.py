import pyautogui
import pyvolume

#pyvolume.custom(percent=50)
#pyvolume.increase()

#pyvolume.decrease()

#x = pyautogui.locateOnScreen('commercial.jpeg', confidence=.6)
#print(x)
#pyautogui.screenshot('shot.png')

while True:
    try:
        pyautogui.locateOnScreen('commercial.jpeg', confidence=.6)
        pyvolume.decrease()    
    except pyautogui.ImageNotFoundException:
        pyvolume.increase()