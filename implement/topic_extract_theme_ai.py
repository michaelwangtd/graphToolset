#!/usr/bin/env/ python
# -*- coding:utf-8 -*-

from utils import io,webpage,util,cutWord
import jieba.analyse
import index
"""
    extract theme from artificial intelligence document using jieba
"""

def getAiArticleTitleList(filePath):
    # title list
    titleList = []
    fr = open(filePath,'r',encoding='utf-8')
    while True:
        line = fr.readline().strip()
        if line:
            lineList = line.split(',')
            if len(lineList) == 4:
                title = lineList[0].strip()
                titleList.append(title)
        else:
            break
    fr.close()
    return titleList


def updateTagbase():
    '''
        作为一个单独模块，对tagbase.txt进行调整
    '''
    # 对标签库进行了去重操作
    tagbaseFilePath = io.getSourceFilePath('tagbase.txt')

    tagbaseList = io.readListFromTxt(tagbaseFilePath)   # 68638
    cleanTagbaseList = list(set(tagbaseList))   # 67523
    io.writeList2Txt('tagbase.txt',cleanTagbaseList)


def cleanTheme(tagList):
    themeList = []
    # 获取标签库中标签
    filePath = io.getSourceFilePath('tagbase.txt')
    tagbaseList = io.readListFromTxt(filePath)
    for item in tagList:
        if item in tagbaseList:
            themeList.append(item)
    return themeList


def isThemeInFieldTagList(themeList,fieldTagList):
    # 领域标签
    # fieldTagList = ['人工智能', '机器学习', '自然语言处理', '语义网', '语义分析', '文本分析', '无人驾驶', '自动驾驶', '机器视觉', '机器人', '智能问答', '深度学习','知识图谱']
    for item in themeList:
        if item in fieldTagList:
            return True
    return False


def filterBlackwordList(themeList,blackwordList):
    resultList = []
    for item in themeList:
        if item not in blackwordList:
            resultList.append(item)
    return resultList


def joinTag(cleanedThemeList):
    resultList = []
    for item in cleanedThemeList:
        resultList.append(item.replace(' ','-'))
    return resultList


def extractTheme(tagList,tagbaseFilePath):
    themeList = []
    tagbaseList = io.readListFromTxt(tagbaseFilePath)
    for item in tagList:
        if item in tagbaseList:
            themeList.append(item)
    return themeList


if __name__ == '__main__':

    """
        之前实验的一个流程
        流程中包含了提取文章，对文章打标签，封装格式等步骤

    """
    # # 获取路径
    # titleFilePath = io.getUnprocessedFilePath('topic_ai_title_name.csv')
    # sentimentFilePath = io.getSourceFilePath('sentiment_invest.txt')
    # outputFilePath = io.getProcessedFilePath('topic_ai_theme.csv')
    # wordListFilePath = io.getSourceFilePath('tagbase.txt')
    # # io
    # fw = open(outputFilePath,'w',encoding='utf-8')
    # fw.write('title,theme,originTag' + '\n')
    #
    # # 1 对tagbase进行修改的代码
    # # updateTagbase()
    #
    # # 2 加载自定义词库
    # jieba.load_userdict(wordListFilePath)
    #
    # # 3 获取领域文章
    # # 获取AI文章名称列表
    # titleList = getAiArticleTitleList(titleFilePath)
    # # 从语料库中获取AI相关文档
    # infoList = io.loadData2Json(sentimentFilePath)
    # for i in range(len(infoList)):
    #     if infoList[i]['sentimentInvestTitle']:
    #         if infoList[i]['sentimentInvestTitle'] in titleList:
    #             # 4 文章打标签
    #             content = infoList[i]['sentimentInvestDesc']
    #             # 提取文档对应主题
    #             themeList = jieba.analyse.extract_tags(content,topK=20)
    #             print('原始提取的标签:',themeList)
    #             # 过滤标签
    #             tempThemeList = cleanTheme(themeList)
    #
    #             # 剔除黑名单标签
    #             cleanedThemeList = filterBlackwordList(tempThemeList,blackwordList)
    #             print('筛选后的标签：',cleanedThemeList,'文章标题：',infoList[i]['sentimentInvestTitle'])
    #
    #             if cleanedThemeList:
    #                 # 5 根据领域列表筛选文章
    #                 if isThemeInFieldTagList(cleanedThemeList):
    #                     title = infoList[i]['sentimentInvestTitle']
    #                     originTags = ' '.join(infoList[i]['sentimentInvestTags'])
    #                     # 有空格的标签用‘-’连接起来
    #                     finalThemeList = joinTag(cleanedThemeList)
    #                     # 持久化
    #                     outputLine = title.replace(',','，') + ',' + ' '.join(finalThemeList) + ',' + originTags
    #                     fw.write(outputLine + '\n')
    # fw.close()



    """
        注意：这段代码可以流程化下来：只需要修改fieldTagList和outputFilePath

        这段代码是在给“品玩”，“36kr”全文打完标签之后执行的
        直接读取文章，根据输入标签筛选出目标文章
        封装目标文章格式，并持久化
    """
    # fieldTagList = index.TRANSIT_TAG_LIST
    #
    # # outputFilePath = io.getProcessedFilePath('topic_ai_theme.csv')
    # outputFilePath = io.getProcessedFilePath('topic_transit_theme.csv')
    #
    # # 路径
    # krTagFilePath = io.getSourceFilePath('topic_article_kr.txt')
    # pwTagFilePath = io.getSourceFilePath('topic_article_pw.txt')
    #
    # # 读取信息
    # krArticleList = io.loadData2Json(krTagFilePath)
    # pwArticleList = io.loadData2Json(pwTagFilePath)
    # infoList = krArticleList + pwArticleList
    #
    # fw = open(outputFilePath,'w',encoding='utf-8')
    # # fw.write('title,theme,originTag' + '\n')
    #
    # for item in infoList:
    #     if item['tag']:
    #         if isThemeInFieldTagList(item['tag'],fieldTagList):
    #             title = item['title']
    #             tagList = item['tag']
    #             originalTagList = item['originalTag']
    #             outputLine = title.replace(',','') + ',' + ' '.join(tagList) + ',' + ' '.join(originalTagList)
    #             fw.write(outputLine + '\n')
    # fw.close()


    """
        导出固定格式文件
        AI领域：title,idf tag,theme
    """
    aiThemeFilePath = io.getProcessedFilePath('topic_ai_theme.csv')
    wordListFilePath = io.getSourceFilePath('tagbase.txt')

    jieba.load_userdict(wordListFilePath)

    # 获取ai文章列表
    aiArticleList = []
    fr = open(aiThemeFilePath,'r',encoding='utf-8')
    while True:
        line = fr.readline().strip()
        if line:
            lineList = line.split(',')
            aiArticleList.append(lineList[0].replace('\ufeff',''))
        else:
            break
    # print(len(aiArticleList),aiArticleList)

    krTagFilePath = io.getSourceFilePath('topic_article_kr.txt')
    pwTagFilePath = io.getSourceFilePath('topic_article_pw.txt')
    scan_ai_article = io.getProcessedFilePath('scan_ai_article.csv')

    # 读取信息
    krArticleList = io.loadData2Json(krTagFilePath)
    pwArticleList = io.loadData2Json(pwTagFilePath)
    infoList = krArticleList + pwArticleList

    fw = open(scan_ai_article,'w',encoding='utf-8')
    fw.write('title,tag,tfidf' + '\n')

    i = 1
    for item in infoList:
        if item['title'] in aiArticleList:
            content = item['content']
            cutOne = cutWord.cutStopWord(content)
            cutTwo = cutWord.cutNoiseWord(cutOne)
            tagList = jieba.analyse.extract_tags(cutTwo)
            themeList = extractTheme(tagList,wordListFilePath)
            print(i,themeList,tagList)
            i += 1
            outputLine = item['title'] + ',' + ' '.join(themeList) + ',' + ' '.join(tagList)
            fw.write(outputLine + '\n')
    fw.close()


