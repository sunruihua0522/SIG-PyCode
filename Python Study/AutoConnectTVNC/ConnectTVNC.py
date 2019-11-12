import pyautogui as gui
import sys
import xlrd
import os
import time
import win32gui
import win32api
import win32con

path=''
splitpath = str(__file__).split('/')
print(splitpath)
for i in range(0,len(splitpath)-1):
    path = os.path.join(path,splitpath[i])

print(path)
book = xlrd.open_workbook(os.path.join(path,'tvncDB.xlsx'))

sheet = book.sheet_by_index(0)
sheet1 = book.sheet_by_index(1)
class CustomerSiteInfo:
    def __init__(self,index,name,line,ip,machineid):
        self.Index = index
        self.Name = name
        self.Line = line
        self.IP =ip
        self.MachineID = machineid

def sefClick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
def sefFindWindow(classname=None,caption=None,timeout=3):
    handle =0
    for _ in range(1,timeout*10):
        time.sleep(0.1)
        handle = win32gui.FindWindow(classname,caption)
        if(handle!=0):
            return handle
    return None

def GetChildList(parent):
    hWndChildList = []
    win32gui.EnumChildWindows(parent, lambda hWnd, param: param.append(hWnd), hWndChildList)
    return hWndChildList

def SendMessageToWindow(window, msg, wparam, lparam):
    win32gui.SendMessage(window, msg, wparam, lparam)

def findInfo():
    customerName = str(input('Enter the customer site name you want to connect\r\n'))
    customerName = str(customerName).lower()
    customers = []
    i=1
    if((customerName =='all' or customerName =='' or customerName==None)):
        for row in range(1, sheet.nrows):
            print('%d\t%s\t%s\t%s\t%s'%(i,sheet.cell_value(row, 0),sheet.cell_value(row, 1),sheet.cell_value(row, 2),sheet.cell_value(row, 3)))
            customers.append(CustomerSiteInfo(i,sheet.cell_value(row, 0),sheet.cell_value(row, 1),sheet.cell_value(row, 2),sheet.cell_value(row, 3)))
            i+=1
        index = int(input('Enter index you want to connect\r\n'))
        if(int(index) <= len(customers)):
            return customers[index-1]

    else:
        #customerName = str(sys.argv[1]).lower()
        for row in range(1, sheet.nrows):
            if(str(sheet.cell_value(row, 0)).lower().find(customerName)!=-1):
                print('%d\t%s\t%s\t%s\t%s' % (i,sheet.cell_value(row, 0), sheet.cell_value(row, 1), sheet.cell_value(row, 2), sheet.cell_value(row, 3)))
                customers.append(CustomerSiteInfo(i, sheet.cell_value(row, 0), sheet.cell_value(row, 1), sheet.cell_value(row, 2),sheet.cell_value(row, 3)))
                i += 1
        index = int(input('Enter index you want to connect\r\n'))
        if (index <= len(customers)):
            return customers[index - 1]


if __name__=='__main__':
    #print(sys.argv)
    info=findInfo()
    win32api.ShellExecute(0, 'open', sheet1.cell_value(0,0), '', '', 1)
    sefFindWindow(None,'New TightVNC Connection')

    '''Input IP address automatically
    pt = None
    for _ in range(1,50):
        time.sleep(0.1)
        pt = gui.locateCenterOnScreen(os.path.join(path,'tvnc_icon.png'))
        if(pt!=None):
            sefClick(pt.x+96,pt.y-176)
            gui.hotkey('ctrl','A')
            gui.typewrite(info.IP)
            sefClick(pt.x+301, pt.y-178)
            break

    sefFindWindow(None,'Vnc Authentication')
    '''
   
    '''Typewrite psw automatically
    pt1 = None
    for _ in range(1,50):
        time.sleep(0.1)
        pt1 = gui.locateCenterOnScreen(os.path.join(path,'tvnc_icon1.png'))
        if(pt1!=None):
            sefClick(pt1.x + 114, pt1.y + 18)
            gui.hotkey('ctrl', 'A')
            pwd = str(info.MachineID)[::-1][0:8]
            gui.typewrite(pwd)
            sefClick(pt1.x+42, pt1.y+57)
            break
    '''

    ParentHandle0 = sefFindWindow(None, 'New TightVNC Connection')
    childList = GetChildList(ParentHandle0)

    SendMessageToWindow(childList[3], win32con.WM_SETTEXT, None, info.IP)
    SendMessageToWindow(childList[11], win32con.BM_CLICK, None, None)

    ParentHandle1 = sefFindWindow(None, 'Vnc Authentication')
    childList1 = GetChildList(ParentHandle1)

    SendMessageToWindow(childList1[3], win32con.WM_SETTEXT, None, str(info.MachineID)[::-1][0:8])
    SendMessageToWindow(childList1[4], win32con.BM_CLICK, None, None)