#!/usr/bin/env python
# -*- coding:utf-8 -*-
from utils import io,util

"""
    topic graph的最后一个环节，将“点”文件中的标签进行分类
"""

def getInitDic():
    initDic = {}
    initDic['title'] = ''
    initDic['tags'] = []

    initDic['product_tags'] = []
    initDic['person_tags'] = []
    initDic['meeting_tags'] = []
    initDic['product_cmy_tags'] = []
    initDic['university_tags'] = []
    initDic['invs_cmy_tags'] = []
    initDic['research_inst_tags'] = []
    initDic['industry_tags'] = []
    return initDic


def classifyTag(initDic,tagbaseDic,allTagList):
    for tag in allTagList:
        for key,value in tagbaseDic.items():
            if tag in value:
                # 将标签存储到initDic中
                initDic[key].append(tag)
                break
    return initDic


if __name__ == '__main__':
    tagbaseNameList = ['industry_tags', 'research_inst_tags', 'invs_cmy_tags', 'university_tags', 'product_cmy_tags',
                       'meeting_tags', 'person_tags', 'product_tags']
    tagbaseDic = {}

    inputFilePath = io.getUnprocessedFilePath('AI_Node.csv')
    outputFilePath = io.getProcessedFilePath('ai_node_classified.csv')
    # 获取标签库
    tagbaseDic = util.getTagbaseDicFromRedis(tagbaseDic, tagbaseNameList)
    # 获取node文件
    infoList = io.readListFromCSV(inputFilePath)

    fw = open(outputFilePath,'w',encoding='utf-8')
    fw.write('title,allTag,productTag,personTag,mettingTag,productCompanyTag,universityTag,investCompanyTag,researchInstituteTag,industryTag' + '\n')

    i = 1
    for lineList in infoList:
        # 初始化字典
        initDic = getInitDic()
        initDic['title'] = lineList[0]
        initDic['tags'] = lineList[2].split(' ')
        # 标签分类
        initDic = classifyTag(initDic,tagbaseDic,lineList[2].split(' '))
        # 构建输出
        outputLine = initDic['title'] + ',' + util.list2str(initDic['tags']) + ',' + util.list2str(initDic['product_tags']) + ','\
                     + util.list2str(initDic['person_tags']) + ',' + util.list2str(initDic['meeting_tags']) + ',' \
                     + util.list2str(initDic['product_cmy_tags']) + ',' + util.list2str(initDic['university_tags']) + ',' \
                     + util.list2str(initDic['invs_cmy_tags']) + ',' + util.list2str(initDic['research_inst_tags']) + ',' \
                     + util.list2str(initDic['industry_tags'])
        print(i,outputLine)
        i += 1
        fw.write(outputLine + '\n')
    fw.close()


