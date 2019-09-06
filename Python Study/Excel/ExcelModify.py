import xlwt,xlrd
from xlutils import copy
fileName = 'NewBook.xls'

book = xlrd.open_workbook(fileName)

new_book = copy.copy(book)

sheet = new_book.get_sheet(0)

sheet.write(2,3,'hello')

new_book.save(fileName)


