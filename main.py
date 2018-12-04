from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
import pyautogui




def healing():
    while 1:
        keyboard.press('z')
        keyboard.press(Key.up)
        time.sleep(1.3)
        keyboard.release(Key.up)
        keyboard.release('z')
        for i in range(0,19):
            print ('x')
            keyboard.press('x')
            time.sleep(0.12)
            keyboard.release('x')
            time.sleep(0.88)
        print ('Exits')
        keyboard.press('z')
        print ('z')
        keyboard.press(Key.down)
        time.sleep(1.6)
        keyboard.release(Key.down)
        keyboard.release('z')
        break


def goto():
    keyboard.press('z')
    keyboard.press(Key.left)
    time.sleep(1.2)
    keyboard.release(Key.left)
    time.sleep(0.8)

    keyboard.press(Key.up)
    time.sleep(0.3)
    keyboard.release(Key.up)
    time.sleep(0.8)

    keyboard.press(Key.left)
    time.sleep(0.75)
    keyboard.release(Key.left)
    time.sleep(0.8)


    keyboard.press(Key.up)
    time.sleep(2.1)
    keyboard.release(Key.up)
def returnfight():
    try:
        menu= pyautogui.locateOnScreen('greenmenu.png')
    except:
        pass
    if menu is None: 
        fighting()

def getback():
    keyboard.press('z')
    keyboard.press(Key.down)
    time.sleep(1.5)
    returnfight()
    time.sleep(1)
    keyboard.release(Key.down)
    time.sleep(0.8) 

    keyboard.press(Key.right)
    time.sleep(0.70)
    keyboard.release(Key.right)
    time.sleep(0.8)
    
    keyboard.press(Key.down)
    time.sleep(0.3)
    keyboard.release(Key.down)
    time.sleep(0.8)

    
    keyboard.press(Key.right)
    time.sleep(0.75)
    keyboard.release(Key.right)
    time.sleep(0.8)

    

    keyboard.press(Key.up)
    time.sleep(0.5)
    keyboard.release(Key.up)
    keyboard.release('z')


def fighting():

    exitpls = 0
    while 1:
        try:
            fight= pyautogui.locateOnScreen('redfight.png')
        except:
            pass
        if fight is None and exitpls == 0:
            print ('1Fight var= ',fight)
            time.sleep(1)
        elif fight is not None and exitpls == 0:
        
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
                            exitpls += 1
                            break
                        elif after is None:
                            keyboard.press('x')
                            time.sleep(0.12)
                            keyboard.release('x')
                            time.sleep(0.08)
                elif exitpls == 1:
                    break
        elif fight is None and exitpls == 1:
            break
            
        
        
                    


                

                         
            
                
    

def battle():
    count1 = 0
    keyboard.press('z')
    keyboard.press(Key.up)
    time.sleep(0.7)
    keyboard.release(Key.up)
    keyboard.release('z')
    
    print ('enter count 1')
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
                
            fighting()
            count1 += 1
            break
                 
def main():
    while 1:
        time.sleep(1.5)
        healing()
        time.sleep(2.5)
        goto()
        time.sleep(1)
        for i in range (0,2):
            battle()
            time.sleep(0.8)
        getback()
        
timeout1 = 21
timeout1_start = time.time()
count1=0


main()


