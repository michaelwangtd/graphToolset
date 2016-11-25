# -*- encoding:utf-8 -*-
"""
    处理网页内容相关的工具
"""
import re

def extractContentBetweenTags(cake):
    '''
        从标记之间提取内容，形成字符串
    '''
    if cake:
        cake = cake.strip()
        contentList = re.findall('>\s*(.*?)\s*<',cake,re.S)
        content = ''.join(contentList)
        return content