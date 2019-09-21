import pyautogui as gui
import time
import random as rd
i=10
#time.sleep(5)

#print(gui.position())

#exit()
while(i>0):
    #time.sleep(5)
    time.sleep(rd.choice(range(5,30)))
    gui.click(90,10)
    time.sleep(8)
    Pt = gui.locateCenterOnScreen('Name.png')
    gui.click(Pt.x, Pt.y-20)
    i=i-1
    time.sleep(3)
    gui.hotkey('ctrl','w')



exit()
