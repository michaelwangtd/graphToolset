# -*- coding:utf-8 -*-

import myIO


"""
将json格式数据转换成excel表格形式
"""
def dic2list(lineDic):
    resultList = []
    for line in lineDic:
        if line:
            simId = ''
            rateClickRec = ''
            tj_clickNum = ''
            tj_recNum = ''
            uv = ''
            shareNum = ''
            storeNum = ''
            joinCommentNum = ''
            articleId = ''
            articleTitle = ''
            if line['simId']:simId = line['simId']
            if line['rateClickRec']:rateClickRec = line['rateClickRec']
            if line['tj_clickNum']:tj_clickNum = line['tj_clickNum']
            if line['tj_recNum']:tj_recNum = line['tj_recNum']
            if line['uv']:uv = line['uv']
            if line['shareNum']:shareNum = line['shareNum']
            if line['storeNum']:storeNum = line['storeNum']
            if line['joinCommentNum']:joinCommentNum = line['joinCommentNum']
            if line['articles']:
                articleStr = line['articles']
                articleStrList = articleStr.split(':')
                if len(articleStrList) == 2:
                    articleId = articleStrList[0]
                    articleTitle = articleStrList[1]
                elif len(articleStrList) ==1:
                    articleId = articleStrList[0]
            # if line['article']:
            #     articleList = line['article']
            #     articleStr = myIO.list2str(articleList, '|')
            resultList.append([simId,rateClickRec,tj_clickNum,tj_recNum,uv,shareNum,storeNum,joinCommentNum,articleId,articleTitle])
    return resultList


if __name__ == '__main__':

    inputFilePath = 'D:\\longTime_small1000_2.txt'
    outputFilePath = 'D:\\longTime_lt_1000.xls'

    lineDic = myIO.loadData2Json(inputFilePath)

    resultList = dic2list(lineDic)
    print len(resultList)

    myIO.writeContent2Excel(resultList, outputFilePath)



