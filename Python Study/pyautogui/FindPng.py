import pyautogui as gui

Pt = gui.locateCenterOnScreen('halcon.png')
#print(Pt.x,Pt.y)
gui.doubleClick(x=Pt.x, y=Pt.y)

#gui.doubleClick()

exit()