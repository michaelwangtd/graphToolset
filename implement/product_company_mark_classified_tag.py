#!/usr/bin/env python
# -*- coding:utf-8 -*-

from utils import io,cutWord,util,webpage
import json
from collections import *
"""
    Source: ad.json , ad_分类标签.csv , ad_节点.csv
    Target: ad_final.json
    Instruction:
                前端用于可视化展示的ad.json文件的node字段中缺少一个该节点分类标签的字段clusterTags
                从xx_classifyTag.csv文件和xx_node.csv中获取“节点与分类标签映射”的关系
                将该映射关系添加进xx.json文件的node字段中
"""


def getClassifyTagDic(classifyTagList):
    '''
        将分类标签的列表形式转化成字典形式
    '''
    classifyTagDic = OrderedDict()
    for item in classifyTagList:
        if item[0] not in classifyTagDic.keys():
            classifyTagDic[item[0]] = item[1]
    return classifyTagDic


def getNodeTagMappingDic(classifyTagDic,nodeList):
    '''
        形成节点与分类标签的映射字典
    '''
    # 映射字典
    mappingDic = OrderedDict()
    for item in nodeList:
        if item[0] and item[1]:
            if classifyTagDic[item[0]]:
                mappingDic[item[1].replace('\ufeff','')] = classifyTagDic[item[0]]
    return mappingDic


def initFrontFinalDic(frontDicList):
    '''
        初始化最终要输出的字典
    '''
    finalFrontDic = {}

    edgeList = frontDicList[0]['edges']
    finalFrontDic['edges'] = edgeList
    finalFrontDic['nodes'] = []
    return finalFrontDic


def markClassifyTag(mappingDic,nodeDicList):
    '''
        mappingDic:
            key:    productCompanyName
            value:  classifyTag
        nodeDicList: 封装好的“点”文件字典列表
        Target: 给nodeDicList中的每一个dit封装一个额外的“clusterTags”字段
    '''
    resultDicList = []
    for dic in nodeDicList:
        if dic['label']:
            # print(dic['label'])
            if mappingDic[dic['label']]:
                dic['clusterTags'] = mappingDic[dic['label']]
                resultDicList.append(dic)
    return resultDicList



if __name__ == '__main__':
    # 输入路径
    classifyTagInputFilePath = io.getProcessedFilePath('ad_分类标签.csv')
    nodeInputFilePath = io.getProcessedFilePath('ad_节点.csv')
    frontJsonInputFilePath = io.getUnprocessedFilePath('ad.json')

    # 输出路径
    adOutputFilePath = io.getProcessedFilePath('ad_final.json')

    classifyTagList = io.readListFromCSV(classifyTagInputFilePath)
    nodeList = io.readListFromCSV(nodeInputFilePath)
    frontDicList = io.loadData2Json(frontJsonInputFilePath)

    # 生成分类标签字典
    classifyTagDic = getClassifyTagDic(classifyTagList)
    # 生成产品公司与分类标签映射字典
    mappingDic = getNodeTagMappingDic(classifyTagDic,nodeList)
    # 初始化frontFinalDic
    finalFrontDic = initFrontFinalDic(frontDicList)
    # 节点标记分类标签
    markedNodeDicList = markClassifyTag(mappingDic,frontDicList[0]['nodes'])
    # 封装node
    finalFrontDic['nodes'] = markedNodeDicList

    # 生成json文件并输出
    fw = open(adOutputFilePath,'w',encoding='utf-8')
    fw.write(json.dumps(finalFrontDic,ensure_ascii=False))
    fw.close()


