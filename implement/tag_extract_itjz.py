#!/usr/bin/env python
# -*- coding:utf-8 -*-

from utils import io,cutWord,operateString,webpage
from collections import *
import re
"""
    公司相似度it桔子标签提取
"""


def getProductCompanyList(itjzInfoList):
    productCompanyDicList = OrderedDict()
    for item in itjzInfoList:
        if item['startup']['name']:
            if item['startup']['name'] not in productCompanyDicList.keys():
                #
                productCompanyDicList[item['startup']['name']] = item['startup']
    return productCompanyDicList



if __name__ == '__main__':
    itjzFilePath = io.getSourceFilePath('investEvents_20161019121629.txt')
    itjzPCSignal2FilePath = io.getProcessedFilePath('itjzProductCompany_signal_2.txt')
    itjzPCSignal1FilePath = io.getProcessedFilePath('itjzProductCompany_signal_1.txt')
    itjzPCSignaldy2FilePath = io.getProcessedFilePath('itjzProductCompany_signal_dy2.txt')

    itjzInfoList = io.loadData2Json(itjzFilePath)

    # fw = open(itjzPCSignal2FilePath,'w',encoding='utf-8')
    # fw = open(itjzPCSignal1FilePath,'w',encoding='utf-8')
    fw = open(itjzPCSignaldy2FilePath,'w',encoding='utf-8')

    # 获取productCompany信息列表
    productCompanyDicList = getProductCompanyList(itjzInfoList)
    print('productCompany字典长度：',len(productCompanyDicList))

    i = 0
    for key,value in productCompanyDicList.items():
        if value['productDesc']:
            targetIndexList = [target.start() for target in re.finditer('、', value['productDesc'])]
            # if targetIndexList:
            if len(targetIndexList) > 2 :
                outputLine = value['name'] + ',' + value['productDesc'].replace(',','，')
                fw.write(outputLine + '\n')
                i += 1
    print('i:',i)
    fw.close()