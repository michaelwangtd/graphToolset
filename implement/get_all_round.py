# -*- encoding:utf-8 -*-

import index
import os
from utils import io,operateString,webpage
"""
    Target:找出投资事件中所有的轮次，生成轮次数据集set
    Source:investEvents_20161019121629.txt
    Instruction:
    1）修正词库中轮次的表示
    2）确定轮次的顺序
"""


if __name__ == '__main__':
    duringPath = 'data\\unprocessed'
    roundSet = set()

    filePath = os.path.join(index.rootPath,duringPath,'investEvents_20161019121629.txt')
    # 加载数据
    jsonList = io.loadData2Json(filePath)

    # # 显示所有的投资轮次
    # for i in range(len(jsonList)):
    #     if 'event' in jsonList[i].keys():
    #         roundSet.add(jsonList[i]['event']['investRound'])
    # print(type(roundSet),str(roundSet))

    # investTimeList = []
    j = 0
    for i in range(len(jsonList)):
        if 'event' in jsonList[i].keys():
            if not jsonList[i]['event']['investTime']:
                print(i,'investTime为空')
            if jsonList[i]['event']['investTime']:
                if len(jsonList[i]['event']['investTime']) == 10:
                    j += 1
                    # investTimeList.append((i,jsonList[i]['event']['investTime']))
    # print(str(investTimeList))
    print(j)

