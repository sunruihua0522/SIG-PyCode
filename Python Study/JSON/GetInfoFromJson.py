import json
import xlwt
import requests

def loadInfo():
    f = open('1.json', encoding='utf-8')
    infos = json.load(f)
    f.close()
    book = xlwt.Workbook()
    newSheet = book.add_sheet('Sheet1')
    row = 0
    for x in infos['data'][0]['v']['data']:
        for machine in x['machines']:
            if(str(machine['machine']).__contains__('COMBISMILE')):
                newSheet.write(row, 0, x['site'])
                newSheet.write(row, 1, machine['machine'])
                newSheet.write(row, 2, machine['variables']['Machine number'])
                newSheet.write(row, 3, machine['variables']['PLC project revision'])
                row = row +1
    book.save('MachineInfo.xlsx')



if __name__ == '__main__':
    loadInfo()
    # r = requests.get('http://10.1.68.225:8002/api/v2/execfunction?lib=SIG.Information.System.lib&func=getVersionInformation&ctx=%2FSystem%2FCMS-Core')
    # print(r.content)
    pass