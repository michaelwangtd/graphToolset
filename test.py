# -*- encoding:utf-8 -*-
import re
import json
import index

# print(input.rootPath)


# testList = []
# if testList:
#     print('j')


# testDic = {('d','a'):'sss'}
# test = 3.4
# print(type(test))
# print(str(test))


# test = ('A',['1','2','3'])
# print(type(test[1]))


# print(type(xlList))
# print(xlList[0])
# print(type(xlList[0][0]))
# tagList = eval(xlList[0][1])
# print(tagList)
# for item in tagList:
#     print(item,item[0],type(item[1]))



# testDic = {1:4,'a':'b','marianne':'michael'}
# testDic2 = {'c':'d','m':'l'}
# reDic = json.dumps(testDic)
# reDic2 = json.dumps(testDic2)
# testList = []
# # testList.append(reDic)
# # testList.append(reDic2)
# fw = open('test_josn.txt','w')
# # json.dump(reDic,fw)     # "{\"marianne\": \"michael\", \"1\": 4, \"a\": \"b\"}"
# # fw.writelines
# # for item in testList:
# #     print(item)
# #     fw.writelines(item + '\n')
# fw.writelines(reDic + '\n')
# fw.writelines(reDic2 + '\n')
# fw.close()




# testTxt = """v><divclass=\"cp-content\"><divclass=\"cp-right\"><divclass=\"cp-right-A\"><divclass=\"cp-rA-right\"><ul><li><pclass=\"PBR-yy\"/><span>影音效果：</span><pclass=\"li-img\"></p></li><li><pclass=\"PBR-xs\"/><span>新手引导：</span><pclass=\"li-img\"></p></li><li><pclass=\"PBR-cz\"/><span>操作手感：</span><pclass=\"li-img\"></p></li><li><pclass=\"PBR-sd\"/><span>难易设定：</span><pclass=\"li-img\"></p></li><li><pclass=\"PBR-ts\"/><span>游戏特色：</span><pclass=\"li-img\"></p></li></ul></div></div><pclass=\"cp-right-navf14\">基本信息"""
# testTxt = """p><divclass=\"img_wrapper\"><imgsrc=\"http://n.sinaimg.cn/97973/transform/20160321/zVRz-fxqnski7777692.png\"alt=\"\"data-link=\"\"/><spanclass=\"img_descr\"/></div><divclass=\"img_wrapper\"><imgsrc=\"http://n.sinaimg.cn/97973/transform/20160321/D_vl-fxqpchx6384259.png\"alt=\"\"data-link=\"\"/><spanclass=\"img_descr\"/></div><p>　　作为一名肉盾英雄，在宝石选择上，更多的应该侧重于增强自身血量抗性能力，能够在前排吸引更多的伤害。因此对于肉盾英雄来讲，为了增加自身血量及抗性，首先推荐如下宝石搭配，生命宝石，护甲宝石及法抗宝石，既增加了血量又增强了护甲和魔抗。</p><p>　　之后宝石选择上，由于寒冬之心的技能全部为法术加成伤害，因此可以选择增强自己的法术输出能力，以提高技能伤害，推荐法强宝石，法术穿透宝石以及法术吸血宝石，用来增强寒冬之心的输出能力及续航能力。</p><p>　　<span>"""
# testTxt = """<p>　　1、樱在最近几个版本的普攻越发难用，无限连偶尔会因为对手浮空高度过低以及自身出手前摇变慢而落地失败。因此在墙边无限连的时候要慎重，尤其是反向踢，踢之后的前摇是相当大的。</p><p>　　2、突进技能我偶尔会作为位移来用，很不错。对自己操作很有自信也可以直接直线释放，打个出其不意的成功率还是蛮高的。</p><p>　　3、铁球有两段伤害，砸中正中心才可以打出全部伤害，所以偶尔连招时要时刻注意这一点。擦边的铁球伤害较低，不过也是有浮空效果就是了。</p><divclass=\"img_wrapper\"><img"""
# reList = re.findall('>\s*(.*?)\s*<',testTxt,re.S)
# print(reList)
# print(''.join(reList))





# testStr = """hello  dksafk
# jsdkf asdfj
# """
# resultStr = testStr.replace('\r','').replace('\n','').replace('\t','').replace(' ','')
# print(testStr)
# print(resultStr)