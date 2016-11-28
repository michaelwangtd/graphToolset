# -*- encoding:utf-8 -*-
"""
    输入输出流
"""

import os
import index
import json


def loadData2Json(filePath):
    '''

    '''
    jsonList = []
    if os.path.exists(filePath):
        fr = open(filePath,'r',encoding='utf-8')
        i = 1
        while True:
            line = fr.readline()
            if line:
                try:
                    temp = line.strip()
                    lineJson = json.loads(temp,encoding='utf-8')
                    print(i,type(lineJson),str(lineJson))
                    i += 1
                    jsonList.append(lineJson)
                except Exception as ex:
                    print(ex)
            else:
                break
    return jsonList