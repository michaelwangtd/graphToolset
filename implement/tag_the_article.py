#!usr/bin/env python
#-*- coding:utf-8 -*-

from utils import io,util,webpage,cutWord
import jieba.analyse
from collections import *
import json
import time
import index
"""
    需求：给“品玩”，“36k”的数据打上标签，以json格式存储
"""


def extractTheme(tagList,tagbaseFilePath):
    themeList = []
    tagbaseList = io.readListFromTxt(tagbaseFilePath)
    for item in tagList:
        if item not in index.TAGBASE_STOP_WORD_LIST:
            if item in tagbaseList:
                themeList.append(item)
    return themeList


def initDic():
    initDic = OrderedDict()
    initDic['title'] = ''
    initDic['time'] = ''
    initDic['url'] = ''
    initDic['tag'] = []
    initDic['originalTag'] = []
    initDic['content'] = ''
    return initDic


def analyseTag():
    krTagFilePath = io.getSourceFilePath('topic_article_kr.txt')
    pwTagFilePath = io.getSourceFilePath('topic_article_pw.txt')

    krArticleList = io.loadData2Json(krTagFilePath)
    pwArticleList = io.loadData2Json(pwTagFilePath)

    i = 1
    for item in pwArticleList:
        if not item['tag']:
            i += 1
    print(i)


def getOriginTagList(originTagListString):
    '''
        本函数目的是从“36kr”接口数据的extraction_tags字段提取标签
    '''
    resultList = []
    if isinstance(originTagListString,str):
        originTagList = json.loads(originTagListString)
        for item in originTagList:
            resultList.append(item[0])

    return resultList



if __name__ == '__main__':

    # redis标签库key值
    tagbaseNameList = ['industry_tags','research_inst_tags','invs_cmy_tags','university_tags','product_cmy_tags','meeting_tags','person_tags','product_tags']
    #
    krOriginSourceFileName = 'origin_html_kr_201701171635.txt'
    pingwestOriginSourceFileName = 'origin_html_pingwest_201701181122.txt'

    # 扩展标tagbase路径
    extendTagbaseFilePath = io.getSourceFilePath('investEvents_20161227144154.txt')
    # 初始化tagbaseDic字典
    tagbaseDic = {}

    # 输出路径
    outputKrFilePath = io.getSourceFilePath('topic_article_kr_201701171635.txt')
    outputPwFilePath = io.getSourceFilePath('topic_article_pw_201701181122.txt')
    # 输入路径
    krFilePath = io.getSourceFilePath(krOriginSourceFileName)
    pwFilePath = io.getSourceFilePath(pingwestOriginSourceFileName)
    # 标签库路径
    tagbaseFilePath = io.getSourceFilePath('topic_tagbase.txt')
    # outputFilePath = io.getProcessedFilePath('fenci.xls')

    # 持久化tagbase
    # 从redis读取的标签
    tagbaseDic = util.getTagbaseDicFromRedis(tagbaseDic,tagbaseNameList)
    # 从“itjz，newseed”investEvents最新的文本获取的标签
    tagbaseDic = util.getTagbaseDicFromFilePath(tagbaseDic,extendTagbaseFilePath)
    util.persistentTagbase(tagbaseDic, tagbaseFilePath)

    # analyse result
    # analyseTag()

    # 加载jieba
    jieba.load_userdict(tagbaseFilePath)

    # 统计开始时间
    print(time.localtime())

    # kr持久化
    fw = open(outputKrFilePath, 'w', encoding='utf-8')
    # 品玩持久化
    # fw = open(outputPwFilePath, 'w', encoding='utf-8')



    # # 品玩文章
    # pwInfoList = io.loadData2Json(pwFilePath)
    #
    # # print(type(pwInfoList[0][0]),pwInfoList[0][0])
    #
    # i = 1
    # for report in pwInfoList:
    #     if report:
    #         try:
    #             content = report[0]['contenthtml']
    #             # 0 去掉html标签
    #             content = webpage.extractContentBetweenTags(content)
    #             # 1 自定义停用词修正
    #             cutOne = cutWord.cutStopWord(content)
    #             # 2 过滤掉标签符号等
    #             cutTwo = cutWord.cutNoiseWord(cutOne)
    #             # 3 提取关键词
    #             tagList = jieba.analyse.extract_tags(cutTwo)
    #             # 4 合并规则
    #             # 5 提取标签
    #             themeList = extractTheme(tagList,tagbaseFilePath)
    #
    #             # print(i,themeList,reportList[2])
    #             # 封装json格式字典
    #             initDic = OrderedDict()
    #             initDic['title'] = report[0]['title']
    #             initDic['time'] = report[0]['gtime']
    #             initDic['url'] = report[0]['posturl']
    #             initDic['originTag'] = []
    #             initDic['tag'] = themeList
    #             initDic['content'] = content
    #             initDic['author'] = report[0]['name']
    #
    #             # 直接写入文件
    #             jsonDic = json.dumps(initDic, ensure_ascii=False)
    #             fw.write(jsonDic + '\n')
    #             print(i)
    #             i += 1
    #         except Exception as ex:
    #             print(ex)



    # 36kr文章

    # krInfoList = io.readListFromTxt(krFilePath)
    krInfoList = io.loadData2Json(krFilePath)

    i = 1
    for report in krInfoList:
        if report:
            # reportList = report.split('\t')
            # if len(reportList) == 4:
                try:
                    # content = reportList[3].strip()
                    content = report['data']['content']
                    # 0 去掉html标签
                    content = webpage.extractContentBetweenTags(content)
                    # 1 自定义停用词修正
                    cutOne = cutWord.cutStopWord(content)
                    # 2 过滤掉标签符号等
                    cutTwo = cutWord.cutNoiseWord(cutOne)
                    # 3 提取关键词
                    tagList = jieba.analyse.extract_tags(cutTwo)
                    # 4 合并规则
                    # 5 提取标签
                    themeList = extractTheme(tagList, tagbaseFilePath)
                    # print(i,themeList,reportList[2])
                    # 封装json格式字典
                    initDic = OrderedDict()
                    initDic['title'] = report['data']['title']
                    initDic['time'] = report['data']['published_at']
                    initDic['url'] = ''
                    initDic['originTag'] = getOriginTagList(report['data']['extraction_tags'])
                    initDic['tag'] = themeList
                    initDic['content'] = content
                    initDic['author'] = report['data']['user']['name']

                    # 直接写入文件
                    jsonDic = json.dumps(initDic, ensure_ascii=False)
                    fw.write(jsonDic + '\n')
                    print(i)
                    i += 1
                except Exception as ex:
                    print(ex)

    fw.close()
    print(time.localtime())




    # # dicList写入文件
    # fw = open(outputKrFilePath,'w',encoding='utf-8')
    # for item in dicList:
    #     jsonDic = json.dumps(item,ensure_ascii=False)
    #     fw.write(jsonDic + '\n')
    # fw.close()


