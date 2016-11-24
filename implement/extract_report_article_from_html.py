# -*- encoding:utf-8 -*-
"""
    Instruction:extract article reported from html
"""
import input
import os


def divideArticle():
    '''
        因为article_html.txt文章未归类，本函数将文章归类为“新浪”，“腾讯”两篇报道形成txt文件
    '''
    # 变量定义
    duringPath = 'data\\unprocessed'
    # I/O操作
    fr = open(os.path.join(input.rootPath,duringPath,'article_html.txt'),'r',encoding='utf-8')
    fw_sina = open(os.path.join(input.rootPath,duringPath,'sina_report.txt'),'w',encoding='utf-8')
    fw_tencent = open(os.path.join(input.rootPath,duringPath,'tencent_report.txt'),'w',encoding='utf-8')
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
    fr = open(os.path.join(input.rootPath,duringPath,'tencent_report.txt'),'r',encoding='utf-8')
    fw = open(os.path.join(input.rootPath,duringPath,'tencent_record.txt'),'w',encoding='utf-8')
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
    fr = open(os.path.join(input.rootPath,duringPath,'sina_report.txt'),'r',encoding='utf-8')
    fw = open(os.path.join(input.rootPath,duringPath,'sina_record.txt'),'w',encoding='utf-8')
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
    duringPath = 'data\\unprocessed'
    fr = open(os.path.join(input.rootPath,duringPath,'sina_record.txt'),'r',encoding='utf-8')
    fw = open(os.path.join(input.rootPath,duringPath,'structed_1.txt'),'w',encoding='utf-8')
    while True:
        line = fr.readline()
        if line:
            lineList = line.strip().split('""')
            title = lineList[0].replace('"','').strip()
            # 清洗文章
            content = cleanTags(lineList[1])
            outputLine = title + '$$' + content
            fw.writelines(outputLine + '\n')
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
    cleanHtmlTag()