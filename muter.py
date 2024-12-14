import pyautogui
import pyvolume

#mutes the TV when the annoying NFL network commercial screen show ups

def mute(commercial_screen):
    '''
    Mutes the volume on a Linux machine when it detects a certain image (commercial screen),
    unmutes when the image goes away. 
    
    Args: 
    commercial_screen (str): path to image that should trigger muting
    
    Returns:
    None
    '''
    while True:
        try:
            pyautogui.locateOnScreen(commercial_screen, confidence=.6)
            pyvolume.decrease()    
        except pyautogui.ImageNotFoundException:
            pyvolume.increase()


def main():
    mute('nfl_network_commercial_screen.jpeg')
    
if '__main__' == '__name__':
    main()
