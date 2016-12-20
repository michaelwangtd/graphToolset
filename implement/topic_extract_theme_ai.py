#!/usr/bin/env/ python
# -*- coding:utf-8 -*-

from utils import io,webpage,operateString
import jieba.analyse
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


def isThemeInFieldTagList(themeList):
    # 领域标签
    fieldTagList = ['人工智能', '机器学习', '自然语言处理', '语义网', '语义分析', '文本分析', '无人驾驶', '自动驾驶', '机器视觉', '机器人', '智能问答', '深度学习','知识图谱']
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


if __name__ == '__main__':
    blackwordList = ['节点','我觉得','Do','Mo','Cor']
    # 获取路径
    titleFilePath = io.getUnprocessedFilePath('topic_ai_title_name.csv')
    sentimentFilePath = io.getSourceFilePath('sentiment_invest.txt')
    outputFilePath = io.getProcessedFilePath('topic_ai_theme.csv')
    wordListFilePath = io.getSourceFilePath('tagbase.txt')
    # io
    fw = open(outputFilePath,'w',encoding='utf-8')
    fw.write('title,theme,originTag' + '\n')

    # 1 对tagbase进行修改的代码
    # updateTagbase()

    # 2 加载自定义词库
    jieba.load_userdict(wordListFilePath)

    # 3 获取领域文章
    # 获取AI文章名称列表
    titleList = getAiArticleTitleList(titleFilePath)
    # 从语料库中获取AI相关文档
    infoList = io.loadData2Json(sentimentFilePath)
    for i in range(len(infoList)):
        if infoList[i]['sentimentInvestTitle']:
            if infoList[i]['sentimentInvestTitle'] in titleList:
                # 4 文章打标签
                content = infoList[i]['sentimentInvestDesc']
                # 提取文档对应主题
                themeList = jieba.analyse.extract_tags(content,topK=20)
                print('原始提取的标签:',themeList)
                # 过滤标签
                tempThemeList = cleanTheme(themeList)

                # 剔除黑名单标签
                cleanedThemeList = filterBlackwordList(tempThemeList,blackwordList)
                print('筛选后的标签：',cleanedThemeList,'文章标题：',infoList[i]['sentimentInvestTitle'])

                if cleanedThemeList:
                    # 5 根据领域列表筛选文章
                    if isThemeInFieldTagList(cleanedThemeList):
                        title = infoList[i]['sentimentInvestTitle']
                        originTags = ' '.join(infoList[i]['sentimentInvestTags'])
                        # 有空格的标签用‘-’连接起来
                        finalThemeList = joinTag(cleanedThemeList)
                        # 持久化
                        outputLine = title.replace(',','，') + ',' + ' '.join(finalThemeList) + ',' + originTags
                        fw.write(outputLine + '\n')
    fw.close()