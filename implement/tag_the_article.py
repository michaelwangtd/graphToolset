#!usr/bin/env python
#-*- coding:utf-8 -*-

from utils import io,operateString,webpage,cutWord
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


if __name__ == '__main__':
    # 路径
    outputKrFilePath = io.getSourceFilePath('topic_article_kr.txt')
    outputPwFilePath = io.getSourceFilePath('topic_article_pw.txt')
    krFilePath = io.getSourceFilePath('36kr_result_fetch.txt')
    pwFilePath = io.getSourceFilePath('sentiment_invest.txt')
    tagbaseFilePath = io.getSourceFilePath('tagbase.txt')
    # outputFilePath = io.getProcessedFilePath('fenci.xls')

    # analyse result
    # analyseTag()


    # 加载jieba
    jieba.load_userdict(tagbaseFilePath)

    # 字典列表
    dicList = []

    print(time.localtime())
    # kr持久化
    fw = open(outputKrFilePath, 'w', encoding='utf-8')
    # 品玩持久化
    fw = open(outputPwFilePath, 'w', encoding='utf-8')

    # 品玩文章
    pwInfoList = io.loadData2Json(pwFilePath)
    i = 1
    for report in pwInfoList:
        if report:
            try:
                content = report['sentimentInvestDesc']
                # 1 自定义停用词修正
                cutOne = cutWord.cutStopWord(content)
                # 2 过滤掉标签符号等
                cutTwo = cutWord.cutNoiseWord(cutOne)
                # 3 提取关键词
                tagList = jieba.analyse.extract_tags(cutTwo)
                # 4 合并规则
                # 5 提取标签
                themeList = extractTheme(tagList,tagbaseFilePath)
                # print(i,themeList,reportList[2])
                # 封装json格式字典
                initDic = OrderedDict()
                initDic['title'] = report['sentimentInvestTitle']
                initDic['time'] = report['sentimentInvestDate']
                initDic['url'] = ''
                initDic['tag'] = themeList
                initDic['originalTag'] = report['sentimentInvestTags']
                initDic['content'] = report['sentimentInvestDesc']

                # 存储到列表中
                # dicList.append(initDic)
                # temp = json.dumps(initDic,ensure_ascii=False)
                # print(i,type(temp),temp)

                # 直接写入文件
                jsonDic = json.dumps(initDic, ensure_ascii=False)
                fw.write(jsonDic + '\n')
                # print(i)
                i += 1
            except Exception as ex:
                print(ex)

    # # 36kr文章
    # krInfoList = io.readListFromTxt(krFilePath)
    # i = 1
    # for report in krInfoList:
    #     if report:
    #         reportList = report.split('\t')
    #         if len(reportList) == 4:
    #             try:
    #                 content = reportList[3].strip()
    #                 # 1 自定义停用词修正
    #                 cutOne = cutWord.cutStopWord(content)
    #                 # 2 过滤掉标签符号等
    #                 cutTwo = cutWord.cutNoiseWord(cutOne)
    #                 # 3 提取关键词
    #                 tagList = jieba.analyse.extract_tags(cutTwo)
    #                 # 4 合并规则
    #                 # 5 提取标签
    #                 themeList = extractTheme(tagList, tagbaseFilePath)
    #                 # print(i,themeList,reportList[2])
    #                 # 封装json格式字典
    #                 initDic = OrderedDict()
    #                 initDic['title'] = reportList[2]
    #                 initDic['time'] = reportList[1]
    #                 initDic['url'] = reportList[0]
    #                 initDic['tag'] = themeList
    #                 initDic['originalTag'] = []
    #                 initDic['content'] = reportList[3]
    #
    #                 # 存储到列表中
    #                 # dicList.append(initDic)
    #                 # temp = json.dumps(initDic,ensure_ascii=False)
    #                 # print(i,type(temp),temp)
    #
    #                 # 直接写入文件
    #                 jsonDic = json.dumps(initDic, ensure_ascii=False)
    #                 fw.write(jsonDic + '\n')
    #                 # print(i)
    #                 i += 1
    #             except Exception as ex:
    #                 print(ex)

    fw.close()
    print(time.localtime())


    # # dicList写入文件
    # fw = open(outputKrFilePath,'w',encoding='utf-8')
    # for item in dicList:
    #     jsonDic = json.dumps(item,ensure_ascii=False)
    #     fw.write(jsonDic + '\n')
    # fw.close()


