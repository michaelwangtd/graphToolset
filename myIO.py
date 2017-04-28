# -*- encoding:utf-8 -*-
"""
    输入输出流
"""

import os
import index
import json
import xlrd
import xlwt
from xlutils import copy


def getSourceFilePath(fileName):
    '''
    默认的路径为：'rootPath/data/source/'
    :param fileName:
    :return:完整的文件路径
    '''
    if fileName:
        filePath = os.path.join(index.ROOTPATH,index.DATA,index.SOURCE,fileName)
        return filePath


def getProcessedFilePath(fileName):
    '''
    默认的路径为：'rootPath/data/processed/'
    :param fileName:
    :return:完整的文件路径
    '''
    if fileName:
        filePath = os.path.join(index.ROOTPATH,index.DATA,index.PROCESSED,fileName)
        return filePath


def getUnprocessedFilePath(fileName):
    '''
    默认的路径为：'rootPath/data/unprocessed/'
    :param fileName:
    :return:完整的文件路径
    '''
    if fileName:
        filePath = os.path.join(index.ROOTPATH,index.DATA,index.UNPROCESSED,fileName)
        if os.path.exists(filePath):
            return filePath






def loadData2Json(filePath):
    '''

    '''
    jsonList = []
    if os.path.exists(filePath):
        # fr = open(filePath,'r',encoding='utf-8')
        fr = open(filePath,'r')
        i = 1
        while True:
            line = fr.readline()
            if line:
                try:
                    temp = line.strip()
                    lineJson = json.loads(temp,encoding='utf-8')
                    # print(i,type(lineJson),str(lineJson))
                    i += 1
                    jsonList.append(lineJson)
                except Exception as ex:
                    print(ex)
            else:
                break
    return jsonList


def getListFromExcel(prePath,fileName):
    tempList = []
    filePath = os.path.join(prePath,fileName)
    if os.path.exists(filePath):
        xls_r = xlrd.open_workbook(filePath)
        sheet_r = xls_r.sheet_by_index(0)
        rows = sheet_r.nrows
        for i in range(rows):
            oneRecord = sheet_r.row_values(i)
            tempList.append(oneRecord)
    return tempList


def getListFromTxt(filePath):
    if os.path.exists(filePath):
        resultList = []
        fr = open(filePath,'r',encoding='utf-8')
        while True:
            line = fr.readline().strip()
            if line:
                result = line.strip()
                resultList.append(result)
            else:
                break
        fr.close()
        return resultList


def readListFromTxt(filePath):
    '''
        读取文本信息形成列表
        只是将整行内容存储到列表中
    '''
    infoList = []
    if os.path.exists(filePath):
        f = open(filePath,'r',encoding='utf-8')
        while True:
            line = f.readline()
            if line:
                temp = line.strip()
                infoList.append(temp)
            else:
                break
        f.close()
    return infoList


def readListFromCSV(filePath):
    '''
        读取整行信息形成列表
        整行信息用‘,’分割成小列表之后再存储到列表中
    '''
    infoList = []
    if os.path.exists(filePath):
        f = open(filePath,'r',encoding='utf-8')
        while True:
            line = f.readline()
            if line:
                line = line.strip()
                lineList = line.split(',')
                infoList.append(lineList)
            else:
                break
        f.close()
    return infoList


def writeList2Txt(filePath,infoList):
    if infoList:
        if os.path.exists(filePath):
            # f = open(filePath,'w',encoding='utf-8')
            f = open(filePath,'w')
            for i in range(len(infoList)):
                outputLine = str(infoList[i])
                f.write(outputLine + '\n')
            f.close()


def dic2json(dic):
    '''
        将字典格式转化为json格式
    '''
    return json.dumps(dic,ensure_ascii=False)


def appendContent2Excel(infoList,outputFilePath):
    """
        “追加”的方式写入数据
    """
    # 打开excel文件
    r_xls = xlrd.open_workbook(outputFilePath)
    # 找到excel文件的sheet表
    r_sheet = r_xls.sheet_by_index(0)
    # 获取sheet表的行数
    rows = r_sheet.nrows
    # 将excel文件复制一份
    w_xls = copy.copy(r_xls)
    # 获取复制后文件的sheet表
    sheet_write = w_xls.get_sheet(0)

    # 遍历infoList
    for i in range(len(infoList)):
        for j in range(len(infoList[i])):
            sheet_write.write(rows + i,j,infoList[i][j])
        print('第【' + str(i) + '】条数据已经写入...')
    # 保存文件
    w_xls.save(outputFilePath)

def writeContent2Excel(infoList, outputFilePath):
    """
        “覆盖”的方式写入数据
    """
    xls = xlwt.Workbook()
    sheet = xls.add_sheet('Sheet1')
    for i in range(len(infoList)):
        for j in range(len(infoList[i])):
            sheet.write(i, j, infoList[i][j])
        print('写入第【', str(i), '】条数据...')
    xls.save(outputFilePath)
    print('数据写入完成...')

def writeOrAppendContent2Excel(infoList, outputFilePath):
    """
        判断文件是否存在
        文件存在就用追加的方式写入信息
        文件不存在就新写入信息
    """
    if os.path.exists(outputFilePath):
        # “追加”方式写入文件
        xls_r = xlrd.open_workbook(outputFilePath)
        sheet_r = xls_r.sheet_by_index(0)
        rows = sheet_r.nrows
        xls_w = copy.copy(xls_r)
        sheet_w = xls_w.get_sheet(0)
        for i in range(len(infoList)):
            for j in range(len(infoList[i])):
                sheet_w.write(rows + i, j, infoList[i][j])
                print('第【' + str(i) + '】条数据已经写入...')
    else:
        xls_w = xlwt.Workbook()
        sheet_w = xls_w.add_sheet('Sheet1')
        for i in range(len(infoList)):
            for j in range(len(infoList[i])):
                sheet_w.write(i, j, infoList[i][j])
            print('写入第【', str(i), '】条数据...')
    xls_w.save(outputFilePath)


def list2str(cakeList,linkSymbol = ' '):
    '''
        使用指定的链接符号linkSymbol，将列表转换成字符串
        默认的链接符号linkSymbol为‘空格’
    '''
    if isinstance(cakeList,list):
        return linkSymbol.join(cakeList)