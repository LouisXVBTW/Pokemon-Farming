import time
import pyautogui
from pynput.keyboard import Key, Controller
keyboard = Controller()

def fighting():
    while 1:
        try:
            fight= pyautogui.locateOnScreen('redfight.png')
        except:
            pass
        if fight is None:
            print ('1Fight var= ',fight)
            time.sleep(1)
        elif fight is not None:
        
            print ('1Fight var= ',fight)
            keyboard.release('z')
            keyboard.press(Key.down)
            time.sleep(0.12)
            keyboard.release(Key.down)
            time.sleep(0.5)


            keyboard.press(Key.down)
            time.sleep(0.12)
            keyboard.release(Key.down)
            time.sleep(0.5)


            keyboard.press(Key.right)
            time.sleep(0.12)
            keyboard.release(Key.right)
            time.sleep(0.5)


            keyboard.press(Key.right)
            time.sleep(0.12)
            keyboard.release(Key.right)
            time.sleep(0.5)


            keyboard.press('x')
            time.sleep(0.12)
            keyboard.release('x')
            time.sleep(1)
            


            keyboard.press(Key.down)
            time.sleep(0.12)
            keyboard.release(Key.down)
            time.sleep(0.5)


            keyboard.press('x')
            time.sleep(0.12)
            keyboard.release('x')
            time.sleep(0.5)


            keyboard.press('x')
            time.sleep(0.12)
            keyboard.release('x')
            time.sleep(0.5)

            while 1:
                try:
                    fight2= pyautogui.locateOnScreen('redfight.png')
                    print ('2Fight var= ',fight)
                except:
                    pass
                if fight2 is not None:
                    keyboard.press('x')
                    time.sleep(0.12)
                    keyboard.release('x')
                    time.sleep(0.5)

                    time.sleep(0.5)
                    keyboard.press(Key.right)
                    time.sleep(0.12)
                    keyboard.release(Key.right)
                    time.sleep(0.5)
                    keyboard.press('x')
                    time.sleep(0.12)
                    keyboard.release('x')
                    time.sleep(0.5)
                    while 1:
                        try:
                            after= pyautogui.locateOnScreen('greenmenu.png')
                            time.sleep(0.3)
                            print ('1After var= ',after)
                        except:
                            pass
                        if after is not None:
                            break
                        elif after is None:
                            keyboard.press('x')
                            time.sleep(0.12)
                            keyboard.release('x')
                            time.sleep(0.5)
                break


                

                         
            
                
    

def battle():
    count1 = 0
    keyboard.press('z')
    keyboard.press(Key.up)
    time.sleep(0.7)
    keyboard.release(Key.up)
    keyboard.release('z')
    if count1 > 3:
        
        while 1:
            
            try: 
                menu= pyautogui.locateOnScreen('greenmenu.png')
            except:
                pass
            if menu is not None:
                print ('Menu var= ',menu)
                keyboard.press('z')
                time.sleep(0.12)
                keyboard.press(Key.up)
                time.sleep(0.7)
                keyboard.release(Key.up)
                time.sleep(0.5)
                keyboard.press(Key.down)
                time.sleep(0.7)
                keyboard.release(Key.down)
                keyboard.release('z')
            elif menu is None:
                print ('Menu var= ',menu)
                while 1:
                    
                    fighting()
                    count1 += 1
                    break
                    
    else:
        count2 = 0
        while count2 > 3:
            try: 
                menu= pyautogui.locateOnScreen('greenmenu.png')
            except:
                pass
            if menu is not None:
                keyboard.press('z')
                keyboard.press(Key.down)
                time.sleep(0.5)
                count2 += 1
                keyboard.release('z')
            elif menu is None:
                while 1:
                    fighting()
                


battle()