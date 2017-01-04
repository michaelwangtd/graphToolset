#!/usr/bin/env python
# -*- coding:utf-8 -*-

from utils import io,cutWord,util,webpage
from collections import *
import re
import jieba.analyse
"""
    公司相似度it桔子标签提取
    it橘子已经有自己的标签，这段代码的目的是：验证顿号规则合理性，在it橘子文本中使用过滤规则，提取关键词
    根据提取的关键词与原有的标签对比，验证规则
"""


def getProductCompanyList(itjzInfoList):
    '''
        从it橘子文本中获取产品公司字典列表
    '''
    productCompanyDicList = OrderedDict()
    for item in itjzInfoList:
        if item['startup']['name']:
            if item['startup']['name'] not in productCompanyDicList.keys():
                #
                productCompanyDicList[item['startup']['name']] = item['startup']
    return productCompanyDicList


def getCleanedContentJieBa(content):
    """
        分词之后获取符号两边的2个词
    """
    flagList = []
    contentList = []
    cakeList = list(jieba.cut(content,cut_all=True))
    # 标记flag索引位置
    for i in range(len(cakeList)):
        # if cakeList[i] in ['、','和','以及']:  # 找到符号索引
        if cakeList[i] in ['、','以及']:  # 找到符号索引
            # 符号左半部分
            if i > 1:
                flagList.extend([i,i-1,i-2])
            else:
                while i >= 0:
                    flagList.append(i)
                    i -= 1
            # 符号右半部分
            if i < len(cakeList)-2-1:
                flagList.extend([i,i+1,i+2])
            else:
                while i < len(cakeList):
                    flagList.append(i)
                    i += 1
    # 获取过滤结果
    flagList = list(set(flagList))
    for i in range(len(cakeList)):
        if i not in flagList:
            contentList.append(cakeList[i])
    return ''.join(contentList)


def getCleanedContentString(content):
    """
        按照4个字符，分别在两边过滤信息
    """
    flagList = []
    contentList = []
    # cakeList = list(jieba.cut(content))
    # 标记flag索引位置
    for i in range(len(content)):
        # if cakeList[i] in ['、','和','以及']:  # 找到符号索引
        if content[i] in ['、']:  # 找到符号索引
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


def extractTag(content,tagbaseFilePath):
    '''
        在内容描述中提取标签
    '''
    # tfidf生成主题
    tfidfThemeList = gettfidfThemeList(content)
    # 筛选主题生成标签
    tagList = scanTheme2Tag(tfidfThemeList,tagbaseFilePath)
    return tagList


def gettfidfThemeList(content):
    '''
        利用tfidf提取文本主题
    '''
    return jieba.analyse.extract_tags(content,topK=20)



def scanTheme2Tag(themeList,tagbaseFilePath):
    '''
        从标签库中筛选标签
    '''
    tagList = []
    tagbaseList = io.readListFromTxt(tagbaseFilePath)
    for item in themeList:
        if item in tagbaseList:
            tagList.append(item)
    return tagList


def getDescAverageLen(dicList):
    '''
        统计description的长度
    '''
    sumNum = 0
    recordNum = 0
    for key,value in dicList.items():
        if key:
            recordNum += 1
            sumNum = sumNum + len(value['productDesc'])
    print('总记录数：',recordNum)
    print('desc总长度：',sumNum)
    print('平均长度：',sumNum/recordNum)


def filterTagFromTagbase(content,tagbaseFilePath):
    resultList = []
    # 获取标签库列表
    tagbaseList = io.readListFromTxt(tagbaseFilePath)
    for item in tagbaseList:
        if item in content:
            resultList.append(item)
    return resultList




if __name__ == '__main__':

    tagbaseNameList = ['industry_tags']

    # 获取路径
    itjzFilePath = io.getSourceFilePath('investEvents_20161019121629.txt')
    itjzOutputFilePath = io.getProcessedFilePath('itjz_trial_company_tag.txt')
    itjzTagbaseFilePath = io.getProcessedFilePath('itjz_extract_theme_tagbase.txt')
    # 加载数据
    itjzInfoList = io.loadData2Json(itjzFilePath)

    fw = open(itjzOutputFilePath,'w',encoding='utf-8')
    fw.write('name,desc,originalTag,cutWordTag,stringTag,scanTagCutword,scanTagString' + '\n')

    # 1 获取公司实体
    productCompanyDicList = getProductCompanyList(itjzInfoList)
    print('productCompany字典长度：',len(productCompanyDicList))

    # 计算productDesc的平均长度
    # length = getDescAverageLen(productCompanyDicList)

    # 2 获取标签库标签，生成标签文本
    tagbaseDic = util.getTagbaseDic(tagbaseNameList)
    # 生成标签库文本
    util.persistentTagbase(tagbaseDic,itjzTagbaseFilePath)
    # 3 加载标签库为分词做准备
    jieba.load_userdict(itjzTagbaseFilePath)
    i = 1
    j = 0
    k = 0
    m = 0
    n = 0
    # 4 遍历公司实体
    for key,value in productCompanyDicList.items():
        # 5 获取干净的描述
        cleanedDescJieba = getCleanedContentJieBa(value['productDesc'])
        cleanedDescStr = getCleanedContentString(value['productDesc'])
        # 6 tf-idf提取关键词，获取关键词列表
        cutWordTagList = extractTag(cleanedDescJieba,itjzTagbaseFilePath)
        if cutWordTagList:
            j += 1
        stringTagList = extractTag(cleanedDescStr,itjzTagbaseFilePath)
        if stringTagList:
            k += 1
        # 6.5 直接从标签库中筛选标签
        cutWordFilterTagList = filterTagFromTagbase(cleanedDescJieba,itjzTagbaseFilePath)
        if cutWordFilterTagList:
            m += 1
        stringFilterTagList = filterTagFromTagbase(cleanedDescStr,itjzTagbaseFilePath)
        if stringFilterTagList:
            n += 1
        # 7 构建输出信息并输出
        companyName = value['name']
        desc = value['productDesc']
        originalTag = value['productTags']
        outputLine = companyName + ',' + desc.replace(',','，') + ',' + ' '.join(originalTag) + ',' + ' '.join(cutWordTagList) + ',' + ' '.join(stringTagList) + ',' +\
                    ' '.join(cutWordFilterTagList) + ',' + ' '.join(stringFilterTagList)
        fw.write(outputLine + '\n')
        print(i,cutWordTagList)
        i += 1
    print('分词获取标签的记录数：',j)
    print('字符串获取标签的记录数：',k)
    print('分词直接匹配的记录数：',m)
    print('字符串直接匹配的记录数：',n)
    fw.close()




