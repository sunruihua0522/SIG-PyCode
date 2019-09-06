import xlrd, xlwt
book = xlwt.Workbook()
newSheet = book.add_sheet('NameSheet')
for row in range(0,10):
    for col in range(0,20):
        newSheet.write(row,col,'(%d,%d)'%(row,col))
book.save('NewBook.xlsx')

