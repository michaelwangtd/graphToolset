#!/usr/bin/env python
# -*- coding:utf-8 -*-

import index
from utils import io,util,webpage
from collections import *
import os
import re
"""
    Target:普聚类之后对数据集在进行分类
    Source:
    Instruction:
    Input Format:xx_cluster_tags.csv/xls    xx_nodes.csv/xls
    Output Format:xx分类标签，xx节点
"""
class Product():
    def __init__(self,id,label,timeset,productTags,fromSource,productBuildTime,productLink,productArea,productProvince,productCompanyState,\
                 investRound,investMoney,investTime,companyValue,investIntroduce,modularityClass,flag='0'):
        self.id = id,
        self.label = label,
        self.timeset = timeset,
        self.productTags = productTags,
        self.fromSource = fromSource,
        self.productBuildTime = productBuildTime,
        self.productLink = productLink,
        self.productArea = productArea,
        self.productProvine = productProvince,
        self.productCompanyState = productCompanyState,
        self.investRound = investRound,
        self.investMoney = investMoney,
        self.investTime = investTime,
        self.companyValue = companyValue,
        self.investIntroduce = investIntroduce,
        self.modularityClass = modularityClass,
        self.flag = flag


def getClusterTagList(filePath):
    '''
        由于聚类标签文件xx_cluster_tags.xxx的特殊格式不适用readListFromCSV()和getListFromExcel(),这里重写该方法
        xx_cluster_tags.xxx文件的特殊性：
            1）.csv格式
            2）元素里面有“,”分隔符
        该函数采取的方法：
            找到第一个“,”所在索引，以此作为分个标志
    '''
    if os.path.exists(filePath):
        # 存放结果
        resultList = []
        fr = open(filePath,'r',encoding='utf-8')
        while True:
            line = fr.readline().strip()
            if line:
                splitIndex = line.index(',')
                # print([line[:splitIndex],line[splitIndex+1:]])
                resultList.append([line[:splitIndex],line[splitIndex+1:]])
            else:
                break
        fr.close()
        return resultList






def getClassifyDic(filePath):
    # 初始化字典
    initDic = OrderedDict()
    # 获取xl数据
    # tempList = io.readListFromCSV(filePath)
    # tempList = io.getListFromExcel(filePath)
    tempList = getClusterTagList(filePath)
    for item in tempList:
        if item:
            initDic[int(item[0].replace('\ufeff',''))] = eval(eval(item[1]))
    return initDic


def getNodeObjList(filePath):
    nodeObjList = []
    tempList = io.readListFromCSV(filePath)
    # tempList = io.getListFromExcel(filePath)
    for item in tempList:
        company = Product(id=item[0],label=item[1],timeset=item[2],productTags=item[3],fromSource=item[4],productBuildTime=str(item[5]),\
                          productLink=item[6],productArea=item[7],productProvince=item[8],productCompanyState=item[9],\
                          investRound=item[10],investMoney=item[11],investTime=str(item[12]),companyValue=str(item[13]),\
                          investIntroduce=item[14],modularityClass=str(int(item[15])))
        nodeObjList.append(company)
    return nodeObjList


def getRelatedObj(key,nodeObjList):
    objList = []
    for item in nodeObjList:
        if item.modularityClass[0] == key:
            objList.append(item)
    return objList


def getClassifiedTupeList(classTagList,objList):
    classifiedTupleList = []
    # 初始化类标签字典
    classTagDic = OrderedDict()
    for item in classTagList:
        classTagDic[item] = []
    # classTagDicKeyList = list(classTagDic.keys())
    # 遍历

    # for item in objList:
    #     productTagList = item.productTags[0].split(' ')
    #     for i in range(len(classTagList)):
    #         if classTagList[i][0] in productTagList:
    #             classTagDic[classTagList[i]].append(item)
    #             break
    # print(classTagList)
    # exit(0)

    for tagTuple in classTagList:
        if objList:
            # for key,value in enumerate(objList):
            #     if value.flag[0] == '0' and tagTuple[0] in value.productTags[0].split(' '):
            #         classTagDic[tagTuple].append(value)
            #         value.flag[0] = '1'
            for companyObj in objList:
                if companyObj.flag == '0' and (tagTuple[0] in companyObj.productTags[0].split(' ')):
                    classTagDic[tagTuple].append(companyObj)
                    companyObj.flag = '1'
                    # objList.remove(companyObj)
        # if not objList:
        #     break
    # print(len(objList))
    # 将字典转换成列表
    for key,value in classTagDic.items():
        if classTagDic[key]:
            tempList = [key,value]
            print('分类后的列表:',tempList)
            classifiedTupleList.append(tempList)
    return classifiedTupleList


if __name__ == '__main__':
    # 领域
    field = 'ad'
    # 输入路径
    clusterInputTagFilePath = io.getUnprocessedFilePath(field + '_cluster_tags.csv')
    nodeInputFilePath = io.getUnprocessedFilePath(field + '_nodes.csv')
    # 输出路径
    classifiedTagFilePath = io.getProcessedFilePath(field + '_分类标签.csv')
    nodeFilePath = io.getProcessedFilePath(field + '_节点.csv')

    fw_classify = open(classifiedTagFilePath,'w',encoding='utf-8')
    fw_node = open(nodeFilePath,'w',encoding='utf-8')
    # 已分类元组列表
    classifiedTupleList = []
    # 获取分类标签字典
    classifyDic = getClassifyDic(clusterInputTagFilePath)
    # 获取节点对象列表
    nodeObjList = getNodeObjList(nodeInputFilePath)
    for key,value in classifyDic.items():
        # 选取key对应的对象
        objList = getRelatedObj(str(key),nodeObjList)
        # 根据value，objList
        itemClassifiedTupeList = getClassifiedTupeList(value,objList)
        classifiedTupleList.extend(itemClassifiedTupeList)
    # 这里已经获得分类的元租列表,将数据写出
    for i in range(len(classifiedTupleList)):
        classifyOutputLine = str(i) + ',' + classifiedTupleList[i][0][0] + ',' + str(classifiedTupleList[i][0][1])
        fw_classify.write(classifyOutputLine + '\n')
        outputClassifyList = classifiedTupleList[i][1]
        for obj in outputClassifyList:
            outputClassifyLine = str(i) + ',' + obj.id[0] + ',' + obj.label[0] + ',' + obj.timeset[0]+','+obj.productTags[0]+','+obj.fromSource[0]+','+\
                                 str(obj.productBuildTime[0])+','+obj.productLink[0]+','+\
                                 obj.productArea[0]+','+obj.productProvine[0]+','+obj.productCompanyState[0]+','+obj.investRound[0]+','+\
                                 obj.investMoney[0]+','+str(obj.investTime[0])+','+str(obj.companyValue[0])+','+\
                                 str(obj.investIntroduce[0])+','+str(obj.modularityClass[0])
            print(outputClassifyLine)
            fw_node.write(outputClassifyLine + '\n')

    fw_node.close()
    fw_classify.close()




