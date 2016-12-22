# -*- encoding:utf-8 -*-
"""
    author:CaptWang
    target:zhizhugraph data process toolset
    date:2016/07/01
"""
import os

# 根目录
ROOTPATH = os.path.dirname(__file__)

DATA = 'data'
PROCESSED = 'processed'
UNPROCESSED = 'unprocessed'
SOURCE = 'source'

# 自定义停用词列表
CUSTOMSTOPWORDLIST = ['我们','两款','一款','一些','玩票','一个','这些','这一','这个','一边','一段','选择','目前','可以','这一步','获得','觉得','我觉得','一步','运作','巩固','沉淀','此番','一名','这三人','你们','他们']

# Tags
ARTIFICIAL_INTELLIGENCE_TAG_LIST = ['人工智能', '机器学习', '自然语言处理', '语义网', '语义分析', '文本分析', '无人驾驶', '自动驾驶', '机器视觉', '机器人', '智能问答', '深度学习', '知识图谱']
TRANSIT_TAG_LIST = ['物流','快递']