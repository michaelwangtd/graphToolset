# -*- encoding:utf-8 -*-
import re
import json
import index
import jieba.analyse
# from collections import *
from utils import io

tagbaseFilePath = io.getSourceFilePath('tagbase.txt')
tagbaseList = io.readListFromTxt(tagbaseFilePath)
print(tagbaseList)

# def test():
#     testList = [1,1,1,1]
#     for item in testList:
#         print(item)
#         if item == 1:
#             return 'ok'
#     return 'on'
#
# if __name__ == '__main__':
#     test()


# content = """同样尺寸的屏幕，如何做到“画面更大、手感更轻盈”？努比亚给出的最佳答案是，无边框。标准版的 Z11 售价 2499 元 ，配以高通骁龙 820 处理器、4GB RAM 64GB ROM 等主流旗舰的硬件方案，作为首次体验“无边框”的门槛确实也不算高。我先下个结论，如果你是安卓手机用户、钟爱无边框屏幕、对手机拍摄又有一定追求、又恰逢换机的档期，不妨考虑一下努比亚 6 月 28 日刚推出的这款 Z11。觉得以上描述挺符合心理预期的朋友，可以继续往下翻。无边框的野心日常关注努比亚的朋友或多或少会了解，努比亚的无边框设计是通过一项名为 aRC（arc Refractive Conduction，弧面折射传导）的技术，是将屏幕的显示内容折射到玻璃面板的边缘，从视觉上，边缘部分也承担了部分显示屏的作用。这么一来，尽管 Z11 采用的是一块 5.5 英寸 1920 x 1080 分辨率的 SuperAMOLED 显示屏，他的机身尺寸做到与市面 5.2 英寸的手机尺寸差不多。由于无边框的“减法”主要体现在手机的两侧，机子整体反而会因两边变窄而显得修长。尺寸：151.8 x 72.3 x 7.5（mm）/162g上一代 Z9 饱受诟病的厚度与重量问题，在 Z11 身上也得到良好的改善。努比亚宣称 Z11 的屏占比达到 81%，这给没有感受过“无边框”的用户（例如我）所带来最直观的感受是，视觉体验的全面升级。视频应当是人们日常使用频率颇高的一个场景，如图，当我用 Z11 观赏影片时，鲜艳效果且不说，画面仿佛有种要从屏幕溢出、铺面而至的感觉。这或许就是屏幕边界消除后无拘无束的视觉快感，是我之前使用手机所没感受过的。在上一代 Z9 出现的靠近屏幕边缘部分有画质损失的问题，在这一代的 Z11 也得到很好解决。从正面观看时，你是不会感到屏幕边缘与中心的精细度会有所偏差。取代了手机边框的屏幕边缘，努比亚希望你也能把它用起来。于是 Z11 进一步优化边缘手势的功能，如“边缘双击”快速返回、“双边滑动”调节亮度等等。但这些功能在实际使用上，并没有比现有的触屏方式有太大的操作优势。例如在我单手握着 Z11 操作，双击边缘并不比我横跨至屏幕右下角点击“返回”虚拟键简单。但无论如何，多一个选择总不是坏事。中规中矩的背面与指纹识别对比令人惊艳的正面，努比亚 Z11 的背面就有点叫人失望了。跟上一代 Z9 前后两面均为玻璃面板不同，Z11 的背面采用了三段式的金属外壳设计。部件间的接合严实，体现了努比亚的一流造工，但这近乎没有设计的背面设计实在谈不上美。我拿到手测评的机子是银色版本，虽然这已经是旗舰，没有添加任何涂料的金属原件配色，还是不免透露出“千元机”般的粗劣感。现在 Z11 可选的配色包括：星空灰、皓月银、旭日金、咖啡金、曜石金。建议大家在选购时挑选深色调，而非灰色或银色版本。Z11 系列的三款手机（另外两款分别为大屏的Z11 Max、小屏的 Z11 mini），均采用后置指纹识别的方案。努比亚在发布会上说 Z11 的指纹识别速度是 0.1s。可能是我容易出手汗的缘故，实际的指纹识别还是会存在时灵时不灵的情况。我刚拿到 Z11 ，经常会莫名奇妙地弹出以下的截屏画面。我纳闷了许久也找不到触发截屏的原因。最后才发现，原来 Z11 还内置了名为“超级截图”的功能。当手机画面出于正常开启状态，长按指纹键，便能进入截屏、长截图以及录屏的状态。习惯了真觉得这功能十分便利。不变的 UIZ11 采用的是基于 Android 6.0 的定制系统 Nubia UI 4.0，这一版 UI 延续了 Z9 扁平化的设计风格。系统自带的图标形状圆形、方形兼备，对于外部安装的应用采用圆形包围的处理。配合我这张法国圣米歇尔山的壁纸，整个 UI 配色更显清新、整洁。不过系统默认一级菜单，安装的应用稍微多一些，画面便会显得凌乱。在主屏的最左侧一页是自带的 9 种特效相机，无法变更或删去。顺便一提的是，手机的锁屏样式均为努比亚定制的美图壁纸，同样是无法变更。屏幕下方中央的红色圆形 Home 触摸键，也是信息提醒的呼吸灯。这跟背面摄像头的小红圈已经成了 nubia 手机的标志。另外 Home 键右侧是大家熟知的返回键，左侧为选项设置键，保留了 Z9 时代的按键设计。强化拍摄拍照向来是努比亚手机的卖点， Z11 除了采用索尼最新的 1600 万像素、F2.0 光圈的 IMX298 图像传感器，更搭载了全新的 NeoVision 6.0 影像引擎。PDAF 混合相位对焦、DTI 像素隔离技术、LTM 局部调色技术，NeoVision 6.0 集成了一堆我记不住名字的技术。这不重要，你只要记住， Z11 的手持电子光圈功能已经做到手持长曝光的程度。简单来说，过往需要使用单反、将三脚架固定在某处、设置匹配光圈与快门的复杂操作，现在只需你手持 Z11 就能轻松完成。借助手持长曝光的功能，你可以把波涛的海浪拍得平面如镜，也可以把流淌的小溪拍得如水雾般的立体。NeoVision 6.0 在桌面提供了多重曝光、光绘、电子光圈、慢门、星轨、短视频、运动轨迹、DNG 和克隆等9 个拍摄功能的入口，这满足了部分摄影爱好者的专业需求。但实际上，绝大多数人使用手机相机，都是即开即拍，随手记录生活的画面。先说说日常光照下的拍摄体验，对焦速度很快，能够实现即开即拍，画质也还不错，1600 万像素的解析力也令人满意。值得注意的是，类似华为的 P9，如果采用 Z11 内置的相机拍照，照片会强行打上努比亚的水印。这要求用户保持较高的品牌认同感，在分享照片时也要有足够的自信。迎着车灯的逆光，采用自动模式拍中啊。在手持状态下，使用光绘模式拍照。总结在几天的使用中，Z11 并没有出现机身过热的现象。高通骁龙 820 与 4GB ROM 的组合几乎满足我日常需求，暂时也没有遇到卡顿或死机的状况。充电方面，Z11 支持 Type-C 接口和 QC 3.0 快充（最大输出功率 18W）。就我最近的充电来说，充电一小时，电量从  10% 提升至 70% 。努比亚强调在系统层面进行了诸如限制应用自启、防止偷跑等省电算法。3000mAh 的电池容量 ，基本能满足我工作日情况下一天半以上的使用需求。如今能让留下印象的国产手机是越来越少， Z11 无疑是令人印象深刻的一部。无边框屏幕、便捷与强大的拍摄功能、全网通……努比亚的这些鲜明特色在国产品牌当中也是独树一帜的。比起去年 Z9 刚发布时 3499 元起的价格， 这次 Z11 的定价务实了许多。再说 Z11 的卖点还有一个，那就是 C 罗代言。Z11 系列手机邀请 C 罗这位国际顶级球星担任代言，这既符合努比亚中高端的自身定位，也意在笼络那些喜欢体育的年轻人们。同时，努比亚签约 C 罗也是今年宣布国际化战略后的重要布局，为的让更多的人迅速对这个年轻的品牌建立品牌认知。"""
# # result = jieba.analyse.extract_tags(content,topK=10,withWeight=True)
# result = jieba.analyse.extract_tags(content)
# print(type(result),result)
# for item in result:
#     print(item)
# print(type(str(result)),str(result))
# print(str(result).replace(',','，'))
# for item in result:
#     print(item[0],item[1],type(item[1]))








# if __name__ == '__main__':
#     try:
#         testList = ['a','b','c','d']
#         a = 0
#         for i in range(len(testList)):
#             a +=1
#             print(a )
#             if i == 0:
#                 testList.remove(testList[i])
#                 testList[3] = 1
#         print(testList)
#     except:
#         print('---')






# dic = OrderedDict()

# testList = ['1','2','1']
# for key,value in enumerate(testList):
#     print(key,value)
#     if value == '1':
#         print('进行caozuo')
#         value = '2'
# print(testList)


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