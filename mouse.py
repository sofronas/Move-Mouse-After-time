import pyautogui
import time
import random

starttime = time.time()
width, height= pyautogui.size()

while True:
    positionx = random.randint(1,width)
    positiony = random.randint(1,height)
    pyautogui.moveTo(positionx, positiony)
    timestamp = time.strftime('%H:%M:%S')
    print("{}\tPosition: {} - {}" .format(timestamp,str(positionx),str(positiony)))
    #print(time.time())
    time.sleep(1200.0 - ((time.time() - starttime) % 60.0))
