#!usr/bin/env python
#-*- coding:utf-8 -*-

import index
"""
    分词相关的工具函数
"""

def cutStopWord(content):
    # 自定义停词列表
    stopWordList = index.CUSTOM_STOP_WORD_LIST
    for item in stopWordList:
        content = content.replace(item,'')
    return content


def cutNoiseWord(content):
    return content.replace('&nbsp;','')
