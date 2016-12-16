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



if __name__ == '__main__':
    # 获取路径
    titleFilePath = io.getUnprocessedFilePath('topic_ai_title_name.csv')
    # 获取AI文章名称列表
    titleList = getAiArticleTitleList(titleFilePath)
    # 加载自定义词库

    # 从语料库中获取AI相关文档
    # 提取文档对应主题
    # 持久化
    print(len(titleList))