import xlrd,time

book = xlrd.open_workbook('NewBook.xlsx')
sheet = book.sheet_by_name('NameSheet')
for row in range(0,sheet.nrows):
    for col in range(0,sheet.ncols):
        print(sheet.cell_value(row,col))

time.sleep(20)