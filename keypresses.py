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

def getback():
    keyboard.press('z')
    keyboard.press(Key.down)
    time.sleep(2.1)
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

def battle():
    keyboard.press(Key.up)
    time.sleep(0.12)
    keyboard.release(Key.up)
    while 1:
        fight= pyautogui.locateOnScreen('redfight.png')
        print (fight)
        if fight == None:

            keyboard.press('z')
            keyboard.press(Key.up)
            time.sleep(0.12)
            keyboard.release(Key.up)
            keyboard.press(Key.down)
            time.sleep(0.12)
            keyboard.release(Key.down)
        else:
            keyboard.press(Key.down)
            time.sleep(0.12)
            keyboard.release(Key.down)
            keyboard.press(Key.down)
            time.sleep(0.12)
            keyboard.release(Key.down)
            keyboard.press(Key.right)
            time.sleep(0.12)
            keyboard.release(Key.right)
            keyboard.press(Key.right)
            time.sleep(0.12)
            keyboard.release(Key.right)
            keyboard.press('x')
            time.sleep(0.12)
            keyboard.release('x')
            keyboard.press(Key.down)
            time.sleep(0.12)
            keyboard.release(Key.down)
            keyboard.press('x')
            time.sleep(0.12)
            keyboard.release('x')
            keyboard.press('x')
            time.sleep(0.12)
            keyboard.release('x')
            break
            





     
def main():
    for i in range(0,2):
        time.sleep(1.5)
        healing()
        time.sleep(2.5)
        goto()
        time.sleep(1)
        getback()
        
timeout1 = 21
timeout1_start = time.time()
count1=0


main()




    #keyboard.press(Key.left)
    #keyboard.release(Key.left)
    #time.sleep(0.30)
    #keyboard.press(Key.up)
    #keyboard.release(Key.up)
    #time.sleep(0.30)
    #keyboard.press(Key.right)
    #keyboard.release(Key.right)
    #time.sleep(0.30)
    #keyboard.press(Key.down)
    #keyboard.release(Key.down)
    #time.sleep(0.30)