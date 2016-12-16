# -*- encoding:utf-8 -*-
import index
import os
from utils import webpage
import json
"""
    Target：从html爬取数据中提取内容
    Source:news report txt
    Instruction:extract article reported from html
"""


def divideArticle():
    '''
        因为article_html.txt文章未归类，本函数将文章归类为“新浪”，“腾讯”两篇报道形成txt文件
    '''
    # 变量定义
    duringPath = 'data\\unprocessed'
    # I/O操作
    fr = open(os.path.join(index.ROOTPATH, duringPath, 'article_html.txt'), 'r', encoding='utf-8')
    fw_sina = open(os.path.join(index.ROOTPATH, duringPath, 'sina_report.txt'), 'w', encoding='utf-8')
    fw_tencent = open(os.path.join(index.ROOTPATH, duringPath, 'tencent_report.txt'), 'w', encoding='utf-8')
    # 读取文件
    i = 0
    while True:
        line = fr.readline()
        if line:
            i += 1
            if i <= 62267:
                fw_tencent.writelines(line)
            else:
                fw_sina.writelines(line)
        else:
            break
    fr.close()
    fw_sina.close()
    fw_tencent.close()


def divideTencentArticle2Line():
    '''
        将文章分割开来，每篇文章形成一条记录
    '''
    # 定义变量
    duringPath = 'data\\unprocessed'
    # I/O
    fr = open(os.path.join(index.ROOTPATH, duringPath, 'tencent_report.txt'), 'r', encoding='utf-8')
    fw = open(os.path.join(index.ROOTPATH, duringPath, 'tencent_record.txt'), 'w', encoding='utf-8')
    outputLine = ''
    while True:
        line = fr.readline()
        if line:
            if '<div id=\\"Cnt-Main-Article-QQ\\" bosszone=\\"content\\">' in line or '<div class=\\"left-b article\\" id=\\"articleContent\\">' in line or\
                '<div class=\\"main-content article\\" id=\\"articleContent\\">' in line or \
                            '<div id=\\"Cnt-Main-Article-QQ\\" class=\\"Cnt-Main-Article-QQ\\" bosszone=\\"content\\">' in line:
                # 去掉outputLine中的换行
                outputLine = outputLine.replace('\r','').replace('\n','').replace('\t','').replace(' ','').strip()
                # 将outputLine写入文件
                fw.writelines(outputLine + '\n')
                # 清空outputLine
                outputLine = ''
            outputLine = outputLine + line
        else:
            break
    fr.close()
    fw.close()


def divideSinaArticle2Line():
    '''
        将文章分割开来，每篇文章形成一条记录
    '''
    # 定义变量
    duringPath = 'data\\unprocessed'
    # I/O
    fr = open(os.path.join(index.ROOTPATH, duringPath, 'sina_report.txt'), 'r', encoding='utf-8')
    fw = open(os.path.join(index.ROOTPATH, duringPath, 'sina_record.txt'), 'w', encoding='utf-8')
    outputLine = ''
    i = 1
    while True:
        line = fr.readline()
        if line:
            if '"<div><div ' in line:
                # 去掉outputLine中的换行
                outputLine = outputLine.replace('\r','').replace('\n','').replace('\t','').replace(' ','').strip()
                # 将outputLine写入文件
                fw.writelines(outputLine + '\n')
                print('生成第【',i,'】条记录')
                i += 1
                # 清空outputLine
                outputLine = ''
            outputLine = outputLine + line
        else:
            break
    fr.close()
    fw.close()



def cleanHtmlTag():
    '''
        清楚html标记
    '''
    # 定义变量
    duringPath = 'data\\unprocessed'
    # 这里可以进行修改
    # fr = open(os.path.join(input.rootPath,duringPath,'sina_record.txt'),'r',encoding='utf-8')
    fr = open(os.path.join(index.ROOTPATH, duringPath, 'tencent_record.txt'), 'r', encoding='utf-8')
    fw = open(os.path.join(index.ROOTPATH, duringPath, 'structured.txt'), 'a', encoding='utf-8')
    i = 1
    while True:
        line = fr.readline()
        if line:
            lineList = line.strip().split('""')
            title = lineList[0].replace('"','').strip()
            # 清洗文章
            content = webpage.extractContentBetweenTags(lineList[1])
            outputLine = title + '$$' + content
            fw.writelines(outputLine + '\n')
            print('输出第[',i,']条')
            i += 1
        else:
            break
    fr.close()
    fw.close()



def structured2json():
    # 定义变量
    during = 'data\\unprocessed'
    outputFilePath = index.ROOTPATH + '\\' + during + '\\' + 'final_report.txt'
    # I/O
    fr = open(os.path.join(index.ROOTPATH, during, 'structured.txt'), 'r', encoding='utf-8')
    fw = open(outputFilePath,'w',encoding='utf-8')
    #
    i = 1
    while True:
        line = fr.readline().strip()
        if line:
            if '$$' in line:
                lineList = line.split('$$')
                if len(lineList) == 2:
                    try:
                        # 使用这里的数据生成dict格式
                        dic = {'title':lineList[0],'content':lineList[1]}
                        jsonLine = json.dumps(dic,ensure_ascii=False)
                        print(jsonLine)
                        fw.writelines(jsonLine + '\n')
                        print(i)
                        i += 1
                    except Exception as ex:
                        print(str(dic))
        else:
            break
    fr.close()
    fw.close()



if __name__ == '__main__':

    # # 将原始文章报道分成两部分
    # divideArticle()

    # 将“腾讯”报道文章分开成一条记录
    # divideTencentArticle2Line()
    # divideSinaArticle2Line()

    # 将record去除html标记，形成“标题”，“内容”配对的记录
    # cleanHtmlTag()

    # 将结构化的数据转换成json格式
    structured2json()