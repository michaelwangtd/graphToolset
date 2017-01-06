# -*- encoding:utf-8 -*-

import redis
import index
import os
from utils import io
"""
    普通的处理类
"""

def double2one(doubleList):
    return list(set(doubleList))


def getCompanyNameList(filePath):
    '''
        dataSource:investEvents_20161227144154.txt（最新的“新芽”，“it桔子”合并之后的数据）
        CompanyName指“vc_company”，“product_company”两部分公司名称
        为什么要注明dataSource？因为文件改变后，结构可能改变了，函数不一定能适应
    '''
    companyNameList = []
    infoList = io.loadData2Json(filePath)
    for info in infoList:
        if info['startup']['name']:
            companyNameList.append(info['startup']['name'])
        if info['vc']['name']:
            companyNameList.append(info['vc']['name'])
    return list(set(companyNameList))


def dic2list(dic):
    '''
        目前dic字典的value值要求是list
        后续可以继续添加由dic转换到list时dic中value的类型
    '''
    resultList = []
    if isinstance(dic,dict):
        for key,value in dic.items():
            if isinstance(value,list):
                resultList.extend(value)
    # resultList = list(set(resultList))
    return resultList


def splitEquivalentTag(tagList):
    '''
        分解同义标签
        列表中的元素如果是同义标签（'xxx||xxx||xxx'），进行分割
        input:list  output:list
    '''
    resultList = []
    for item in tagList:
        if '||' in item:
            resultList.extend(item.split('||'))
        else:
            resultList.append(item)
    return resultList


def getListFromRedis(keyName,r):
    '''
        从redis获取列表
    '''
    resultList = []
    for item in r.lrange(keyName,0,r.llen(keyName)):
        resultList.append(item.decode('utf-8'))
    return resultList


def getTagbaseDicFromRedis(initDic,tagbaseNameList):
    '''
        从redis获取标签库字典
        需要提供redis库key值列表：redisKeyList
        不需要提供redis配置信息，配置信息直接从config配置文件读取
    '''
    if isinstance(tagbaseNameList,list):
        if tagbaseNameList:
            #initDic = {}
            r = redis.Redis(host=index.REDIS_HOST,port=index.REDIS_PORT,password=index.REDIS_PASSWORD,db=index.REDIS_DB)
            # 遍历tagbaseNameList
            for tagbaseName in tagbaseNameList:
                # 获取tagbase列表
                tagbaseList = getListFromRedis(tagbaseName,r)
                if tagbaseName not in initDic.keys():
                    initDic[tagbaseName] = tagbaseList
            return initDic


def getTagbaseDicFromFilePath(initDic,filePath):
    '''
        从filePath获取标签库字典
        明确这个函数设计的目的：补充从redis已读取的标签
        补充的情况下不能很好的确定新补充记录的key值，不能开放一个参数由用户定义，也不能直接写具体的key值
        这里提供一个“具体而又模糊”的key名称：other_tags
    '''
    keyName = 'other_tags'
    companyNameList = getCompanyNameList(filePath)
    initDic[keyName] = companyNameList
    return initDic


def persistentTagbase(tagbase,filePath):
    '''
        为什么是persistent tagbase，因为持久化的文件生成的格式是特定的
        tagbase可以是字典也可以是列表，如果是字典就转化成列表
        将tagbase的列表以“覆盖”写的方式写入filePath文件
    '''
    tagbaseList = []
    # 准备数据格式
    if isinstance(tagbase,dict):
        tagbaseList = dic2list(tagbase)
    if isinstance(tagbase,list):
        tagbaseList = tagbase
    # 分解标签列表中的同义标签
    tagbaseList = splitEquivalentTag(tagbaseList)
    # 去重
    tagbaseList = double2one(tagbaseList)
    # 数据持久化准备
    fw = open(filePath,'w',encoding='utf-8')
    for tag in tagbaseList:
        fw.write(tag + '\n')
    fw.close()



