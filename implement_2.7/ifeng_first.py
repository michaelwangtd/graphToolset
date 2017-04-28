# -*- coding:utf-8 -*-

import myIO
from collections import OrderedDict

def getLongTimeDic():
    dic = OrderedDict()
    dic['simId'] = ''
    dic['rateClickRec'] = 0.0
    dic['tj_clickNum'] = 0.0
    dic['tj_recNum'] = 0.0
    dic['uv'] = 0
    dic['shareNum'] = 0
    dic['storeNum'] = 0
    dic['joinCommentNum'] = 0
    return dic

def getRate(clickNum,recNum):
    if recNum != 0.0:
        if recNum > 40.0 and recNum > clickNum:
            # rateNum = round(clickNum / recNum)
            rateNum = clickNum / recNum
            if rateNum > 0.0 and rateNum < 0.5:
                return rateNum

# recNum > 1000
def getRate2(clickNum,recNum):
    if recNum != 0.0 and recNum > clickNum:
            rateNum = clickNum / recNum
            if rateNum > 0.08:
                # 这个地方可以动态变动
                if recNum > 1000:
                    return rateNum

# recNum < 1000
def getRate3(clickNum,recNum):
    if recNum != 0.0 and recNum > clickNum:
            rateNum = clickNum / recNum
            if rateNum > 0.08:
                # 这个地方可以动态变动
                if recNum < 1000:
                    return rateNum

if __name__ == '__main__':

    inputFilePath = 'D:\workstation\\repositories\graphToolset\data\longTime.txt'
    outputFilePath = 'D:\workstation\\repositories\graphToolset\data\longTime_shaped_small1000.txt'

    # problemoutputFilePath = 'D:\workstation\\repositories\graphToolset\data\longTime_problem.txt'

    fw = open(outputFilePath,'a')

    orderList = []
    finalList = []

    jsonList = myIO.loadData2Json(inputFilePath)
    print 'jsonList:  '
    print len(jsonList)

    # 生成orderList
    # i = 0
    for line in jsonList:
        orderItemList = []

        rate = getRate3(line['tj_clickNum'],line['tj_recNum'])

        if rate:
            orderItemList.extend([line['simId'], rate ,line['tj_clickNum'],line['tj_recNum'],line['uv'],line['shareNum']\
                                 ,line['storeNum'],line['joinCommentNum']])
            orderList.append(orderItemList)

    # print "i最后的数："
    # print i

    # for item in testList:
    #     print item

    # io.writeList2Txt(problemoutputFilePath,testList)


    # exit(0)

    # orderList排序
    finalList = sorted(orderList,key=lambda item:item[1],reverse=True)
    print "linalList:"
    print len(finalList)

    # 写出文件
    i = 0
    for item in finalList:
        dic = getLongTimeDic()
        dic['simId'] = item[0]
        dic['rateClickRec'] = item[1]
        dic['tj_clickNum'] = item[2]
        dic['tj_recNum'] = item[3]
        dic['uv'] = item[4]
        dic['shareNum'] = item[5]
        dic['storeNum'] = item[6]
        dic['joinCommentNum'] = item[7]

        result = myIO.dic2json(dic)
        fw.write(result + '\n')
        print i
        i = i + 1
    fw.close()

