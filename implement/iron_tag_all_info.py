#!/usr/bin/env python
# -*- coding:utf-8 -*-

from utils import io,util,cutWord,webpage
import jieba
"""
    target：产品公司实体打标签
    data source：investEvents_20161227144154.txt（it桔子+新芽）
"""

def getCleanedDesc(content):
    """
        按照4个字符，分别在两边过滤信息
    """
    flagList = []
    contentList = []
    # cakeList = list(jieba.cut(content))
    # 标记flag索引位置
    for i in range(len(content)):
        # if cakeList[i] in ['、','和','以及']:  # 找到符号索引
        if content[i] in ['、','以及']:  # 找到符号索引
            # 符号左半部分
            if i > 3:
                flagList.extend([i,i-1,i-2,i-3,i-4])
            else:
                while i >= 0:
                    flagList.append(i)
                    i -= 1
            # 符号右半部分
            if i < len(content)-4-1:
                flagList.extend([i,i+1,i+2,i+3,i+4])
            else:
                while i < len(content):
                    flagList.append(i)
                    i += 1
    # 获取过滤结果
    flagList = list(set(flagList))
    for i in range(len(content)):
        if i not in flagList:
            contentList.append(content[i])
    return ''.join(contentList)


def getCutWordList(content):
    '''
        利用jieba进行分词
    '''
    return list(jieba.cut(content))


def extractTag(cutWordList,tagbaseList):
    '''
        筛选标签库中已有的标签
    '''
    ironTagList = []
    for item in cutWordList:
        if item in tagbaseList:
            ironTagList.append(item)

    return list(set(ironTagList))


def mergeTag(ironTagList,originTagList):
    '''
        合并标签
    '''
    finalTagList = []
    finalTagList.extend(ironTagList)
    finalTagList.extend(originTagList)
    return list(set(finalTagList))




if __name__ == '__main__':

    tagbaseNameList = ['industry_tags']
    # newseed taged info list
    newseedInfoDic = {}
    # file path
    inputFilePath = io.getSourceFilePath('investEvents_20161227144154.txt')
    outputFilePath = io.getSourceFilePath('investEvents_taged_20161227144154.txt')
    tagbaseFilePath = io.getSourceFilePath('tagbase_iron_tag_all_product_company.txt')
    newseedInfoOutputFilePath = io.getProcessedFilePath('newseed_taged_info.csv')
    # get infoList
    infoList = io.loadData2Json(inputFilePath)
    # persist tagbase from redis
    tagbaseDic = util.getTagbaseDic(tagbaseNameList)
    util.persistentTagbase(tagbaseDic,tagbaseFilePath)
    # load cut word user dict
    jieba.load_userdict(tagbaseFilePath)
    # get tagbaseList
    tagbaseList = io.readListFromTxt(tagbaseFilePath)
    # prepare for output
    fw = open(outputFilePath,'w',encoding='utf-8')
    i = 1
    j = 0
    # traverse infoList
    for item in infoList:
        if item['startup']['productDesc']:
            productDesc = item['startup']['productDesc']
            # get cleaned desc
            cleanedDesc = getCleanedDesc(productDesc)
            # get cut word list
            cutWordList = getCutWordList(cleanedDesc)
            # extract tag
            ironTagList = extractTag(cutWordList,tagbaseList)
            print(i,'extracted tag:',ironTagList)
            # get product company entity final tag
            if item['startup']['productTags']:
                finalTagList = mergeTag(ironTagList,item['startup']['productTags'])
            else:
                finalTagList = ironTagList
            # results assigned to item
            item['startup']['productTags'] = finalTagList
        # write item
        outputLine = io.dic2json(item)
        fw.write(outputLine + '\n')
        print(i)
        i += 1
        # filter newseed info
        if item['event']['investInfoFromSrc'] in ['新芽NewSeed']:
            if item['startup']['name'] not in newseedInfoDic.keys():
                newseedInfoDic[item['startup']['name']] = item['startup']
    fw.close()
    # persist newseed info
    fw = open(newseedInfoOutputFilePath,'w',encoding='utf-8')
    for key,value in newseedInfoDic.items():
        outputLine = value['name'] + ',' + ' '.join(value['productTags']) + ',' + value['productDesc'].replace(',','，')
        fw.write(outputLine + '\n')
    fw.close()
    print('程序完成...')
