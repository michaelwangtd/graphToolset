# -*- encoding:utf-8 -*-
"""
    输入输出流
"""

import os
import index
import json
import xlrd
import xlwt


def writeContent2Excel(infoList,outputFilePath):
    """
        “覆盖”的方式写入数据
    """
    xls = xlwt.Workbook()
    sheet = xls.add_sheet('Sheet1')
    for i in range(len(infoList)):
        for j in range(len(infoList[i])):
            sheet.write(i,j,infoList[i][j])
        print('写入第【',str(i),'】条数据...')
    xls.save(outputFilePath)
    print('数据写入完成...')


def getListFromExcel(filePath):
    '''
        输入路径
        以列表形式返回单条列表数据
    '''
    tempList = []
    if os.path.exists(filePath):
        xls_r = xlrd.open_workbook(filePath)
        sheet_r = xls_r.sheet_by_index(0)
        rows = sheet_r.nrows
        for i in range(rows):
            oneRecord = sheet_r.row_values(i)
            tempList.append(oneRecord)
    return tempList


def loadData2Json(filePath):
    '''

    '''
    jsonList = []
    if os.path.exists(filePath):
        fr = open(filePath,'r',encoding='utf-8')
        i = 1
        while True:
            line = fr.readline()
            if line:
                try:
                    temp = line.strip()
                    lineJson = json.loads(temp,encoding='utf-8')
                    print(i,type(lineJson),str(lineJson))
                    i += 1
                    jsonList.append(lineJson)
                except Exception as ex:
                    print(ex)
            else:
                break
    return jsonList