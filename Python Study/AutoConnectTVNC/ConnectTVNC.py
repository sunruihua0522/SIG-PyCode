import pyautogui as gui
import sys
import xlrd
import os
import time

book = xlrd.open_workbook(os.getcwd()+'/tvncDB.xlsx')
sheet = book.sheet_by_index(0)
class CustomerSiteInfo:
    def __init__(self,index,name,line,ip,machineid):
        self.Index = index
        self.Name = name
        self.Line = line
        self.IP =ip
        self.MachineID = machineid

def findInfo():
    customers = []
    i=1
    if(len(sys.argv) ==1):
        for row in range(1, sheet.nrows):
            print('序号%d\t客户:%s\t产线:%s\tIP地址:%s\t机器编号:%s'%(i,sheet.cell_value(row, 0),sheet.cell_value(row, 1),sheet.cell_value(row, 2),sheet.cell_value(row, 3)))
            customers.append(CustomerSiteInfo(i,sheet.cell_value(row, 0),sheet.cell_value(row, 1),sheet.cell_value(row, 2),sheet.cell_value(row, 3)))
            i+=1
        index = int(input('Please enter customer index you want to connect'))
        if(int(index) <= len(customers)):
            return customers[index-1]

    else:
        customerName = str(sys.argv[1]).lower()
        for row in range(1, sheet.nrows):
            if(str(sheet.cell_value(row, 0)).lower().find(customerName)!=-1):
                print('Index:%d\tCustomer Site:%s\tLine:%s\tIP:%s\tMachineID:%s' % (i,sheet.cell_value(row, 0), sheet.cell_value(row, 1), sheet.cell_value(row, 2), sheet.cell_value(row, 3)))
                customers.append(CustomerSiteInfo(i, sheet.cell_value(row, 0), sheet.cell_value(row, 1), sheet.cell_value(row, 2),sheet.cell_value(row, 3)))
                i += 1
        index = int(input('Please enter customer index you want to connect\r\n'))
        if (index <= len(customers)):
            return customers[index - 1]


if __name__=='__main__':
    print(sys.argv)
    info=findInfo()
    #if(len(info)==1):
    os.system('start "D:/SoftwareCenter/TightVNC/tvnviewer.exe"')
    time.sleep(2)
    Pt = gui.locateCenterOnScreen('tvnc_icon.png')

    #gui.doubleClick(Pt)
