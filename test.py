# -*- encoding:utf-8 -*-
import re
import json
import index
import jieba.analyse
# from collections import *
from utils import io,cutWord
import time





# sum = 0
# first = time.time()
# for i in range(10000):
#     sum = sum + 1
# end = time.time()
# # formattime = '%H:%m:%S'
# # time.strftime(formattime,end-first)
# print(end-first)
# test = """我们这一步很难"""
# result = cutWord.cutStopWord(test)
# print(result)
# print(time.localtime())

# testTxt = """http://36kr.com/p/533206.html	2015-05-23 20:40:10 +0800	乐行周伟：在一线城市卖生活方式，在二三四线城市卖个人交通工具	小米投资Ninebot后，平衡车再度成为热点。业界一度传言会合作推出一款999元（后有消息称可能是1599元）的平衡车。不过，在他们出售之前，乐行先出手了，本周他们发布了两款新的代步工具，一款双轮平衡车，一款电动滑板，售价均为2999。36氪联系了乐行的CEO周伟，聊了聊这两款产品背后的故事。为什么会想到做这两款产品？周伟：个人交通机会很大，很多公司都加入到了这个行列，说明大家都意识到了这个问题。中国未来的城市聚集程度越来越高，而未来城市交通有两个方向——共享经济和个人交通。个人交通成本最低，落实时间最快，相比于共享经济，能够真正解决交通拥堵和绿色出行问题。未来，城市最贵的是空间 ，现在写字楼下已经很难停车。所以未来个人交通工具必须能随身携带，且能与其他工具结合。独轮车紧凑、便携、易用，但学习成本很大，至少需要20-30分钟的学习成本，双轮平衡车的学习成本就会降低。而滑板车，不仅便携、而且简单易用，唯一的不足可能就是它看起来不够酷。2999元能撬动多大的市场？周伟：早期我们每次做活动的时候，都会有不少年轻人咨询、购买。很多年轻人很喜欢它，但消费能力有限，一万左右的价格只能望而却步。我们通过微信、微博、线下，做过调研，降价了用户是否会购买，最终也验证了我们早期的认知。至于要用一个什么样的价格给到用户，根据调研，3千元左右的价格最好。我们也曾先通过逐步迭代、降价，最终达到这个价格。但后来想，何不一步到位呢。这个价格，销售肯定会有很大提升。我们今年的目标是25万。小米入局，是我们早就知道的事情。降价，确切的说，是我们自己对自己的超越。平衡车为什么一直没有普及？未来什么样的产品形态才能够普及？周伟：最先做数码相机的柯达被颠覆掉了，最先智能手机的诺基亚被颠覆掉了，因为他们没有提供最完美的解决方案。Segway这样的产品形态有问题，没有办法作为一个工具使用。受制于续航，你往往不能骑着它回家；受制于形态，你望望不能放到后备箱里。甚至，你也未必能把它带进办公楼，因为它体积太大了，要占用空间；又很少有人认识它。Segway到现在也没有弄明白2C的产品怎么做，简单抄袭Segway必然机会渺茫。中美国情又不同，中国是单元楼，不是国外的大house，因此，简洁、紧凑就是必须的。现在平衡车行业竞争激烈，各家都在思考创新，都在根据自己的理解暗暗做一些事情。也许到明年就知道了。如何做营销、推才能推动代步产品尽快普及？周伟：我们团队的强项是做产品，短板就是营销、推广。对个人代步工具来说，市场培育很重要。现在用户仅仅是知道有这样多产品，广泛接受还需要花很长的时间。去年，我们花了一年时间培育市场，做了不少电视植入和线下活动，用户就能知道产品的使用场景和用途。像《辣妈正传》的植入，效果就特别好。共享经济是否会比个人交通更快普及？周伟：毕业5年以内的人，考虑最多的是自由和方便。所有的补贴都不可能一直补贴下去。长远来看，肯定是个人交通能解决问题，且能最快能解决。不过，现在的难点是我们国家的城市交通建设，都是围绕汽车建设的，没有预留其他交通工具的空间。北京还好，还留有自行车道，但很多城市都没有预留空间。因此，你会看到，目前在二线、三线、四线城市的销售，全面超过了一线城市。在一线城市，个人代步工具是一种生活方式；在二三四线城市，它是一种很便携易用的交通工具，都会有市场。原创文章，作者：小石头"""
# result = testTxt.split('\t')
# for item in result:
#     print(item)




testTxt = """先直接给你看视频吧：这是Magic Leap和卢卡斯影业合作的最新成果，前者是AR/VR领域最神秘也最受关注的公司，后者则是全世界最会讲故事的电影公司之一，同时也是电影行业视觉特效、声音特效和计算机动画的业界领袖，《星球大战》六部曲都是它的作品。视频里的场景看起来就发生在普通的房间内，开头还有一个真人的身影从旁边走开。但接下来的场景就很梦幻了：《星球大战》里真人身高的机器人C-3PO面对着你说到，“能跟你说句话吗？很遗憾地报告你，因为意料之外的状况，我们未能就汉·索罗船长的债务和贾巴达成协议。”与此同时，R2-D2机器人走到房间内的桌边，在桌上展示了一副全息影像，就像它在电影里做的一样：帝国突击队的士兵在其庞大的基地巡逻走动，接着，千年隼号飞船从你的眼前起飞并向远方飞去。“我们该怎么进入里面？”C-3PO悲伤地问到。视频下的小字显示：直接用Magic Leap的技术拍摄，制作这则视频时没有使用任何特效及合成。如果这一切都是真实的，那简直太酷了。你所在的真实环境，房间、卧室、办公室，都能成为“梦幻之地”。科技媒体WIRED甚至脑洞大开了一下：如果人工智能可以越来越好，你是不是可以和里面的角色互动呢？想象一下，一个圆滚滚的BB-8机器人对你寸步不离，还能听懂你的话，还能一言不合就给你展示全息影像……以往，Magic Leap在展示自己的成果时，会用很“极客范儿”的视频：办公室的桌子上空漂出通知栏，在空中看立体的股票信息、邮件、PPT。混合现实版的《星球大战》，则是让普通人都会兴奋的东西。这当然是卢卡斯影业的功劳。而且，双方不是一次玩票性质的跨界合作，卢卡斯影业的视觉特效子公司工业光魔（ILM）的xLAB将在旧金山成立一个秘密实验室，Magic Leap的工作人员也将加入；卢卡斯影业中参与了《星球大战》电影的故事组也将加入；另外，卢卡斯影业的音效公司Skywalker Sound也将参与其中，最近大热的电影《魔兽世界》的音效就由Skywalker Sound制作。工业光魔（ILM）本身是一个顶级的视觉特效公司，也是乔治·卢卡斯为了拍摄第一部《星球大战》而专门成立的公司，截至2015年2月，它已经获得了15次奥斯卡最佳视觉特效奖及28座奥斯卡技术贡献成就奖。可以说，是这家公司开创了电影特效行业。作为工业光魔的新部门，xLAB成立于2015年，目的是探索借助虚拟现实、增强现实和混合显示技术，提供沉浸式体验。合作达成后，它也将制作适用Magic Leap技术的《星球大战》内容。xLAB负责人Vicki Dobbs Beck这样形容Magic Leap，“我在工业光魔工作了24年，但我想不起来有任何东西哪怕有一点像它。我从来没有见过想象力和技术在如此接近的水平。”不过，Magic Leap依然发挥了“最神秘公司”的传统，除了这个视频，我们还是无法获取更多一点的关于其技术的内幕，甚至不知道其产品的形态会是如何。Magic Leap的CEO，Rony Abovitz也没有透露我们什么时候能看到一个消费级的产品，“我们正在调试，产品可能很快就能和大家见面。”"""
testTxt2 = """Google 的创始人每年都会写一封公开信，告诉外界企业的发展情况以及未来的愿景。以往，这封信一般是由 Google 两位联合创始人 Larry Page 和 SergeyBrin 一起撰写，但今年，这个任务留给了新上任的 Google CEO Sundar Pichai。接下来，我们看看他是如何描绘 Google 未来的样子。在信中，Sundar Pichai 分别描述了 Google 搜索、Google Photos、Google 地图、Google Play、YouTube、Chrome、Google Cardboard、Google 云计算平台这些产品当下的状况及未来的意义。从行业角度来说，Sundar Pichai 给出的排序是搜索、机器学习和人工智能、优质内容、计算平台和企业级服务。在这个顺序中，搜索作为 Google 的重要营收来源，它的重要性自然无需多言。机器学习和人工智能被提到一个如此靠前的位置，那是因为 Google 认为这些技术将成为旗下产品继续成长、进步的动力源。比如说，如果没有这些智能技术的支持，Google Photos 就不可能做到那么聪明，进而在发布不到一年的时间里就达到月活跃用户数过亿的成绩。在优质内容方面，Google 依靠的是 Google Play 和 YouTube。此外，Google 也在用“加速的移动页面”（AMP）、“模仿原生应用的 Web 应用”(PWA)这些技术性的项目让内容在移动端的呈现方式更高效。对于用户来说，有好内容消费就够了，但对于技术从业者来说，它们还要打造能支撑这些内容消费的计算平台。目前，Android 系统已经有超过 14 亿的月活跃用户，Google Cardboard 也已经让 500 多万用户感受到了虚拟现实的样子。未来，Google 还将在这些领域继续投入。在企业服务方面，Google 已经开发了诸多与之相关的产品，比如 Google 云服务（GCP）、Google 企业应用、Chromebooks、Android、Google Analytics 等等，未来这些产品也将借助机器学习和人工智能技术继续改进。在这封公开信的最后，Sundar Pichai 特意强调了 Google 要服务于每个人，无论你身处大都市还是农村乡舍，Google 都希望能提供平等的服务。之所以这么说，那是因为在 Google 看来：“技术，绝不仅仅是我们创造的设备或产品，因为那并不是终极目标。技术，是一种民主的力量，它所提供的信息，便是力量之源”。附公开信全文：去年八月，我宣布成立Alphabet并公布了公司新架构，同时也分享了我对企业未来发展的思考。对于Alphabet目前的发展，我很欣慰，也十分欣赏Sundar作为Google新任CEO之后的表现。由于Google集中了我们大部分的投入与期许，我愿在此给予Sundar最大的空间展现Google的成就，分享他的愿景。将来，Sundar，Sergey与我，将在这里分享我们对于企业现状及未来发展的理解，敬请期待。–Alphabet 总裁， Larry Page当Larry与Sergey在1998年创建Google时，全球有3亿人使用网络。人们大都坐在椅子上，登陆至桌面设备，然后在一个连接着又大又笨拙显示器的大键盘上敲着字符，进行搜索。而如今，网民数量已升至30亿，他们中的许多人也都可以随时随地通过便携设备搜索信息。多年来，Google一直坚持着自1998年创立以来就立下的使命：“整合全球信息，使人人都能访问并从中受益。”这一使命也在如今变得更加切实且至关重要。因为，在当今世界，人们已经习惯于使用设备来帮助他们安排每天的生活、来往于各地并与彼此保持联系。手机也已成为管理我们日常生活的远程控制器。人们正在手机上，以许多过去无法想象的方式，进行沟通、消费、教育以及娱乐。搜索与支持：满足人们对知识的渴望正如我们在宣布成立Alphabet时说的：“这一新的企业架构会使我们能够集中精力，把握住Google业务中的各种绝佳机遇。”我们也将这些机遇融入了企业使命之中，而其中最重要的，是要让人人皆可获得信息与知识。正因此，搜索始终是我们企业的核心。多年的努力让我们很容易将这一切能看似理所当然，但是当我们回顾搜索已经取得的成就与将要面对的机会时，依旧会感到欣喜和期待。我仍然记得那些通过桌面的10个浅蓝色链接去浏览互联网的日子，而到今天大多数搜索是来自于我们的移动端，并有越来越多的人通过语音使用它。有些问题在过去一年变得越发具有挑战性—— 人们希望更多本地化的内容，更多符合当下情景的信息，他们还想要仅动动手指头就能获得这一切。所以我们正在努力使这些变为可能，让你轻松搜索到[奥斯卡影帝莱昂纳多·迪卡普里奥电影] 或 [寨卡病毒]，此外我们的所有面板上还有更加丰富的资讯以及图像。你也可以通过Google Now获得想要的答案，比如说即将要去的度假胜地的天气，或者何时动身前往机场合适？有一些你甚至不需要去问就能得到答案。帮助你获取信息并利用这些信息度过每一天已经远远超过传统搜索查询的范畴了。想一想你和家人一共照过多少张承载着回忆的照片？总的来说，这一年，人们通过各自的设备会拍摄1万亿张照片。所以我们发布了Google Photos，为的是让人们更加轻松便利的整理照片和视频，在保证照片安全的同时，让你在任何设备上随时找到你想要的图片。Photos不到一年前发布，现在每月已经有超过1亿的活跃用户了。对了，还有我们的Google地图，当你询问我们地址的时候，你应该不会只想知道A点到B点怎么走，根据不同的情境，你也许还想知道躲避拥堵的最佳时间段，想要逛的店铺是否还开门，以及第一次探访的目的地有什么好玩的。而这些仅仅是一个开始。为了让搜索以及Google的服务能够全天候地帮助到你的日常生活，我们仍有许多工作要做。未来，你将能够自然穿梭于Google的各项服务，并获得基于你所处环境、情境以及需求的各项帮助，同时，我们会尊重你的隐私并保护你的个人数据。父母和大学生的需求不同，用户在车中或者在家中所需的帮助也不尽相同。聪明的支持是需要理解这其中的差异并在正确的时间提供恰当的帮助。机器学习与人工智能的力量推动这些工作的是我们在机器学习和人工智能方面的长期投入。正是它们使得你可以通过语音来搜索信息，进行不同语言间的转换，过滤掉邮箱中的垃圾邮件，找到Photos中和“拥抱”有关的照片…..来解决我们日常生活中面临的众多问题。在过去的日子里，是它们让Google的产品不断成长，越来越有帮助。多年来，我们致力于组建最好的人工智能团队和工具，最近的一些突破让我们有机会做的更多。在已经过去的3月，DeepMind研究的AlphaGo战胜了传奇围棋选手李世石，成为自围棋这一最复杂的游戏发明至今第一个打败专业棋手的程序。并不夸张的说，这次胜利影响了围棋这一古老的游戏，最终的胜利属于我们人类。对于通过人工智能在方方面面协助我们，包括完成日常任务以及出行，到最终解决更重大的挑战，比如气候变化以及癌症诊断方面，这将是另外一个重要的阶段。在更多地方提供更多优质内容在互联网发展初期，一提到信息，人们首先会想到网页。这些年来，我们专注于达成核心使命，从索引图片、视频和新闻到构建Google Play及YouTube等平台，我们采取的众多行动都推动了内容的发现、创造以及变现。随着内容向移动端的不断迁移，人们正在比以往任何时候观看更多的视频、玩更多的游戏、聆听更多的音乐、阅读更多的书籍，且使用更多的应用程序。因此，我们努力将YouTube和Google Play打造成为发现与传递优质内容的有效平台，让用户能够随时随地，在任意屏幕上观看来自创作者和开发者的优质内容。Google Play覆盖了超过10亿的Android用户。YouTube也是人们观看视频的首选平台，每月有超过10亿用户访问YouTube网站。此外，YouTube还是年度下载次数最多的移动应用程序之一。事实上，人们在YouTube上观看视频的时长实现了持续的快速增长，其中超过半数的观看时长来自于移动端。未来，我们致力于为YouTube用户提供更多选择，让他们以更多方式与创作者和其他用户进行互动，并以更多方式获取优质内容。为此，我们推出了YouTube Kids等专用应用程序，并推出了YouTube Red订阅服务，让用户享受无广告的观看体验。此外，用户还可以享受优质YouTube Music体验，观看来自PewDiePie、Lilly Singh等知名YouTube创作者的原创影视剧。与此同时，我们继续对移动网络进行投资，这已成为绝大多数网站重要的访问量来源。在过去一年的时间里，Google与发布者、开发者以及生态系统里的其他各方进行了紧密合作，致力于为用户提供更加流畅、更加快速的移动网络体验。“加速的移动页面”（AMP）项目就是这方面很好的一个例子。这是我们携手新闻发布者推出的一项开源举措，旨在帮助发布者创造能够在任意地点即刻加载的移动优化内容。“模仿原生应用的 Web 应用”(PWA)是这方面的另一个例子，通过将网页和应用程序各自的优势相结合，该应用能够让企业创建可快速加载、发送推送通知、拥有主屏幕图标等更多特点的移动站点。最后，我们继续投入与对Chrome移动端性能的改进。自推出以来，短短四年的时间里，Chrome移动端的月度活跃用户就已突破了10亿。当然，优质内容需要资金投入。不论是对Google的网页搜索，还是对于《纽约时报》或《卫报》上引人注目的新闻文章，抑或是对于在YouTube上观看的视频，广告都有助于为广大用户所享受的这些内容提供资金支持。为此，我们致力于打造有效的优质广告产品，为创作者和发布者创造收益。强大的计算平台在十年前，计算还等同于那些放在桌子上的大型计算机。然而仅仅几年后，支持强大计算能力的关键—处理器和传感器，就已变得小巧而经济了。得益于此，易于随身携带的超级计算机—手机，得以快速发展。Android操作系统则进一步推进了手机的普及。目前，Android系统拥有超过14亿的月活跃用户，且这一数字仍在继续扩大。如今，“含屏电子设备”快速发展，早已不限于手机、台式电脑与平板电脑的范畴。随着屏幕应用扩展至汽车及手腕，Android Auto车载系统以及Android Wear可穿戴平台也应运而生。此外，虚拟现实技术也展现出惊人的潜力——Google Cardboard已为500多万用户带去无与伦比、生动逼真，且具有教育意义的美好体验，展现了虚拟现实技术的无限潜力。放眼未来，“设备”的概念将与我们渐行渐远。有朝一日，各种外形的计算机将会在我们生活的各个方面，扮演智能助手的角色。这个世界将从“移动设备优先”变为“人工智能优先”。为企业服务未来，绝大多数计算将很可能在云端进行。不管是对于自动化操作、机器学习，还是对于高效智能办公工具，云端运行都更加安全、经济高效，也更利于运用这些最新科技。Google从一开始就从事云端服务，并投资开发基础构架、数据管理、分析工具及人工智能。目前我们已开发出类别众多并不断增加的企业产品，如Google公共云（GCP）、Google企业应用、Chromebooks、Android、Google Analytics、图像识别、语音翻译、地图及支持用户专用数据集服务的机器学习等。我们的用户，如Whirlpool，O’Lakes以及Spotify等，正在利用Google企业应用套件与Google云平台服务等企业级产能工具来进行商业转型。我们长期投入于开发以机器学习及人工智能为支持的产品，并以此明显改善人们的工作方式。在未来，你的手机将能够自动提取正确文件、规划会议日程并追踪会议进展、通知别人你能否按时到达、草拟短信回复，并能够处理你的开销等等。服务于每一个人无论是使用Google公共云推动新应用研发的开发者，还是通过YouTube发现新收入来源和观众的创作者，我们都相信Google会为每个人提供一个公平竞争的平台。互联网是世界上最强大的均衡器之一，让更多人享受到这项服务，也始终是我们的宗旨所在。这从一开始便是Google的核心原则。早在Google广告诞生之前，Google搜索就已被广为利用。我们从事广告业务也是因为它能使这些服务免费化。Google搜索也致力于为每个网民提供平等的服务，无论他身处现代化大都市还是农村乡舍。但实现该目标，远比简单地引进产品或启用当地国家的域名，要复杂地多。落后的基础设施让全世界数以亿计的人们无法通过网络接触外面的大千世界。这就是为什么我们要生产50美元一部的Android手机或100美元一台的Chromebook笔记本。也是为什么今年我们推出了可离线使用的路线导航。即使网速较慢，人们也能快速地加载，且流畅地进行Google搜索。我们想确保无论你是谁、身处何地，也无论你使用何种水平的设备……Google皆可为你效劳。通过不懈努力，我们致力于让技术能够服务于每一个人。例如，肯尼亚的农民可以使用Google搜索关注农作物的价格，从而卖得好价钱；威斯康星州的学生可以利用Cardboard 眼镜去西斯廷教堂进行“实地考察旅行”；通过在YouTube上制作和观看视频，各地的人们都能分享自己的新观点，与他人沟通。17年来，Google始终不忘初心：做Google该做的，以期完成使命。对此，我十分感动。对我们而言：技术，绝不仅仅是我们创造的设备或产品，因为那并不是终极目标。技术，是一种民主的力量，它所提供的信息，便是力量之源。而Google正是这样一家信息公司，成立至今，始终坚守初衷，从未改变。同时，人们对信息的运用，也不断给我带来惊喜与启迪。Google CEO, Sundar Pichai"""
testTxt3 = """在人们的印象里，自动驾驶、无人驾驶还只是某些公司和尖端科研实验室的内部项目。它们看起来很酷，但是却不知道什么时候才会真正出现在生活中。然而，它的进展其实比人们想象的快： Google 早就在加州和美国其他几个州取得了自动驾驶上路的许可；特斯拉已经交车的 Model S、X 系列中也已经上线了实际可用的自动驾驶功能，驾驶员可以在高速公路环境下把方向盘和油门制动交给计算机和传感器接管。别以为只有 Google、特斯拉这样具有科技和互联网基因的公司才会钻研自动驾驶技术。通用汽车、宝马、福特等一众“传统”汽车公司也在这条路上越走越远。当然，它们拥有丰富的造车经验，因而大都选择了跟互联网科技公司合作，交换资源。我们整理了一个列表，对各大押注自动驾驶技术的公司进行了盘点，你会发现，原来整个汽车工业都认准了，自动驾驶和无人驾驶汽车将会在未来正式接管道路。通用汽车（General Motors）是美国最大的汽车制造商之一，总部位于美国的汽车之城，密歇根州底特律。通用汽车旗下拥有别克、凯迪拉克、雪佛兰和 GMC 四大本土品牌，以及欧宝、五菱等其他小品牌。通用汽车在今年以 10 亿美元收购了自动驾驶技术创业公司 Cruise Automation，此前还斥资 5 亿美元购买了手机叫车软件公司 Lyft 9% 股份。通用汽车与卡耐基梅隆大学等美国科研单位有合作，也在硅谷 Palo Alto 设立了前沿科技实验室，启动了自动驾驶技术方面的研究。就在最近，通用汽车宣布将和 Lyft 合作，争取在一年内上路实测自动驾驶电动专车——不是一两辆，而是一个专车编队。通用汽车计划在雪佛兰推出的电动汽车 Bolt 基础上进行改装，设计并等产出这个计划所使用自动驾驶电动专车。目前，通用汽车和 Lyft 还没有正式宣布其他的细节，但就华尔街日报报道，它们会在一个尚未揭晓的美国城市进行测试，而当地的用户在叫车的时候，将有机会选择是否乘坐自动驾驶的专车。克莱斯勒 Pacifica。图片来自《连线》菲亚特克莱斯勒（Fiat Chrysler）是世界上知名的汽车制造商，由意大利的菲亚特和美国的克莱斯勒在 2014 年并购组合而成。菲亚特克莱斯勒旗下拥有菲亚特、法拉利、克莱斯勒、道奇、阿尔法·罗密欧、玛莎拉蒂等知名汽车品牌。菲亚特克莱斯勒与近日和 Google 母公司 Alphabet 达成了合作，将向后者旗下的自动驾驶部门提供 100 辆经过改装的 Pacifica 厢式轿车，用于测试 Alphabet 的自动驾驶技术。福特（Ford）是汽车业界的元老，现在也是美国最大的汽车制造商之一，总部位于美国密歇根州迪尔伯恩。福特旗下拥有福特、林肯等汽车品牌。福特在世界一线的传统汽车公司当中较早确定了自动驾驶发展路线，投入了重金和大量研发力量进行研究，在密歇根州、亚利桑那州和加州都进行过上路测试。和其他汽车公司还处在自动驾驶研究初级阶段不同，福特宣称已经在雪地、完全无光的黑夜环境等非最佳环境下完成了自动驾驶的测试，效果比人类驾驶更好。福特主要采用 Fusion 混合动力轿车进行测试，据称拥有目前汽车工业最大规模的自动驾驶汽车编队，多达数十辆。丰田（Toyota）是日本最大的汽车制造商之一，旗下拥有雷克萨斯、斯巴鲁等品牌。丰田是 Google 此前无人驾驶汽车技术的汽车供应商，为 Google 提供了混动车普锐斯，以及雷克萨斯 RX 等车型。丰田也在去年 10 月设立了自己的自动驾驶研究单位 Toyota Research Institute，跟斯坦福、MIT 等美国名校正在进行合作。TRI 的主要技术成员来自美国国防部 DARPA 实验室、Google、Facebook 和 MIT 等。奥迪基于 RS7 改装的自动驾驶汽车奥迪（Audi）属于德国的大众汽车集团旗下，是一家中高端轿车品牌。2014 年初，奥迪在 CES 上推出过辅助驾驶技术 Traffic Jam Assistant。顾名思义，它的主要功能是在交通堵塞时辅助司机驾驶。司机按动方向盘上的 TJA 按钮，当硬件系统探测到周围的车况适合启动自动驾驶状态时（比如适当的车速、无路边行人等），就会在中控屏上提示驾驶员 TJA 系统已激活。2015 年 6 月 PingWest品玩曾经试乘过搭载自动驾驶功能的奥迪 A7 汽车。这辆车只有在道路封闭、没有红绿灯、地面标识清晰的路况下才能进入自动驾驶状态，而且时速必须低于 60 公里——说白了，就是只有在城市的环路或者快速路上才可以开启。这属于有限条件下的辅助驾驶，不在我们今天的讨论范围，但仍然算做自动驾驶。奥迪方面透露 2017 年就将在市售的 A8 等高端车型当中加入这种自动驾驶功能。其他正在研究这种辅助性质，条件有限的自动驾驶功能的汽车品牌，还包括戴姆勒（奔驰）、吉利（沃尔沃）等等。Delphi可能并不是一家十分知名的公司。然而在过去一百年中这家公司为全世界几乎所有的一线汽车制造商提供零部件。据雷锋网报道，Delphi 曾经发明了世界上第一款电力起动机，第一款嵌入式收音机，第一套车用无线电导航系统。近年来，Delphi 开始为它的客户，比如奥迪、奔驰等提供自动驾驶外包技术。就像它过去发明的零部件一样，Delphi 生产的自动驾驶模块，将被其他汽车制造商作为标配零件放入到汽车当中。尽管仍然不太属于我们今天讨论的范畴，但 Delphi 的重要意义在于，可能未来所有的小轿车，都能在一些特定情形下具有自动驾驶的功能。（其他为汽车制造商提供自动驾驶、辅助驾驶相关技术的零件供应商，还包括 Continental（马牌）、博世等。）Google 自动驾驶汽车。图片来自纽约时报Alphabet是 Google 公司拆分重组之后的母公司，将以前 Google 名目的多项尖端科研项目归到旗下，当中就包括 Google 无人车研发团队。Google 很早就开始在加州的湾区，包括旧金山城市街道的场景上测试无人驾驶汽车。2010 年时 Google 的自动驾驶车队里程数已经超过了 10 万公里。当时他们使用的是市面上销售汽车，进行改装，曾经使用过丰田旗下的雷克萨斯、普锐斯等车型。当然，人们对 Google 无人车印象最深的，还是下面这辆：截至 2015 年 11 月，Google 用来测试的各种无人驾驶汽车已经跑了 200 万公里。在湾区 Moutain View Google 总部附近的大小街道上，经常能看到顶着一个飞速旋转的“蘑菇”的 Google 无人/自动驾驶汽车。身为互联网公司的 Google，在政策法律方面的动作也很激进。它跟福特、Uber 等公司建立了游说机构，在美国各州以及联邦的立法机构中进行游说工作，推动无人/自动驾驶在美国更多地方合法。特斯拉（Tesla）是被称为“钢铁侠”的著名创业者 Elon Musk 创立的，世界上最著名的电动汽车公司。特斯拉生产的电动汽车，如 Model S、Model X 等，出厂时均已内置了足够自动驾驶的机器视觉传感器和摄像头等，但顾客可以选择是否在购买时或以后激活这一功能——有点像“应用内购买”。特斯拉的自动驾驶功能主要应用于两种场景：高速路和拥堵路段。在高速路上，驾驶员长时间看到的是重复的场景，而在拥堵路段，驾驶员频繁踩油门和刹车，容易疲劳。自动驾驶功能可以接管汽车，在这两种情况下节省驾驶员的精力。最近有人用特斯拉自动驾驶功能开了个大玩笑：一位车主邀请他的母亲驾驶自己的特斯拉，却在高速路上开启了自动驾驶功能，把 70 岁的老太太吓了个够呛……Uber是总部位于加州旧金山的手机叫车软件公司，也是世界上估值最高的互联网创业公司之一。对于 Uber 这样的公司来说，提高交通效率，降低交通成本是营收增长的关键，而无人驾驶将带来很大的帮助。Uber 布局无人驾驶的动作非常大，2015 年 5 月几乎招走了卡耐基梅隆大学机器人研究院（National Robotics Engineering Center，NREC）所有和无人驾驶有关专家，然后在 NREC 的隔壁租了一个办公室，让这些专家为自己研究自动驾驶技术，两栋楼使用同一个停车场。并且，Uber 还在匹兹堡距离 NREC 一英里以外的地方又租下了超大的办公空间，用来修建自己的尖端技术研发总部。据路透社今年 3 月报道，Uber 正在寻找汽车制造商购买大量（六位数）的汽车用于自动驾驶计划，潜在的购买对象可能是奔驰。Uber 计划在 2020 年将自动驾驶专车投入到运营当中。然而现在看来，它的计划赶不上变化了。Lyft，另一家美国手机叫车软件，以粉色的小胡子作为标志。虽然在美国本土的竞争中已经输给了 Uber，但 Lyft 在自动驾驶上的干劲比 Uber 强得多。前面已经提到，Lyft 和通用汽车合作，打算在一年内就在美国一个尚未揭晓的城市运营自动驾驶的专车服务。但目前，Lyft 和通用汽车的自动驾驶计划仍然面临着较大的法律风险。有人驾驶的专车业务本身就存在法律监管的盲点——更别提无人驾驶的了。Mobileye 是一家创立于以色列，现在总部位于荷兰的自动驾驶技术公司，已经在纳斯达克上市。这家公司是业界知名的行车相关机器视觉技术供应商，生产的“高级驾驶员辅助系统”（ADAS）被世界上多家一线汽车厂商所采用。也算是一家跟 Delphi 差不多的，闷声发财的自动驾驶相关公司。百度和 Google 一样，也在研发自己的自动驾驶技术。去年年底，百度在北京宣布成立自动驾驶事业部，跳过智能跟车、车道保持，以及有限条件下的自动驾驶，一上来就要搞完全自动的无人驾驶。该事业部的前身和宝马公司共同研制了一台自动驾驶汽车。在此前的一次测试中，这辆车从百度位于北京市区西北郊西二旗的总部出发，在全程均无人工控制和干预的情况下，上五环，开到北京中轴线上的奥森公园，掉头并最终安全回到了百度。该部门负责人王劲认为，传统的车企的应对策略太过保守。“汽车公司都是循序渐进的……但 Google 曾经说过，循序渐进是不可能的，一直在跳，怎么可能飞起来呢？”百度的自动驾驶商用计划是在北京的各个卫星城，比如亦庄、天通苑等这样的大规模居住区，推出自动驾驶公共汽车，来补充公共交通运力。该公司已经和亦庄定下合作意向，这意味着具有百度自动驾驶功能的公交汽车或将首先在亦庄试点运行。百度首席科学家吴恩达曾对 PingWest品玩表示，百度已经有了一个很清晰的自动驾驶计划。三年内商用没问题。你的汽车是几核的？我的是十二核的！英伟达（Nvidia），世界上最知名的显卡厂商，从近几年开始将他们在图像处理方面的专长延续到了机器视觉方面，也就成了世界上最受关注的自动驾驶技术供应商之一。2014 年英伟达就加入了Google、奥迪、通用汽车等成立的“开放汽车联盟”当中，作为该组织的芯片供应商。2016 年 CES 上，英伟达推出了基于 Tegra 芯片的Drive PX2 自动驾驶平台，拥有十二颗 CPU 核心，搭载了英伟达专门为自动驾驶而研发的深度学习架构 Pascal GPU，采用水冷，计算效能高达 8 TFLOPS，本质上是一个深度学习神经网络。“约等于 150 台 MacBook Pro，只有一个午餐盒的大小，可以放在你的车后备箱里。”英伟达 CEO 黄仁勋这样介绍，他宣称 Drive PX2 对交通状况的细微感知能力超过真人驾驶员。（其他正在研究自动驾驶相关技术的科技公司，还包括英特尔、高通、OmniVision、德仪等。）还有哪些正在推动自动驾驶的巨头公司我们没有提到？欢迎在评论中和我们分享。"""
testTxt4 = """一觉醒来世界还是原来的样子，变坏的人工智能和终结者并没有诞生，更别提控制人类……可是就在一夜间，几乎所有知名的互联网科技公司都重新捡起了一项已经“过时很久”的技术：“Bot”。——可别搞错了，我们说的可不是 Alphabet 旗下波士顿动力制造的、能飞速狂奔数十迈还怎么都踹不倒的机器人，而是由一群看不见摸不到的聊天机器人组成的大军。Bot 是什么？它们会出现在哪里，谁又在开发它们？它们能做什么，更重要的是，能帮你做什么？它们会像很多所谓的科技前沿人士认为的那样，最终取代你手机里的 App 吗？如果你对 Bot 感兴趣，你将在本文中找到这些问题的答案。Bot 是什么？我们正在讨论的 Bot，全称应该是 Chatbot——聊天机器人。过去的聊天机器人是计算机工程师们开发的软件，专门用来跟人聊天玩。之前在微博微信上刷存在感的微软小冰就是一个基于人工智能的聊天机器人，但最早的聊天机器人其实是计算机科学家约瑟夫·维森班在 1966 年编写的 Eliza。这些聊天机器人的拟人程度各不相同，计算机学界还专门为了评判这些机器人的拟人度设立了一项测试，你一定听说过他的名字——图灵测试。但我们讨论的 Bot，会做的不只是聊天。它像是一个客服，要在跟你聊天的同时，了解你的意图，帮你处理你的事项，完成你想让它帮你完成的工作。准确的来说，我们讨论的 Bot，是一个功能强大的聊天机器人助理。Bot 出现在哪里？Bot 已经出现在我们生活中使用的各种计算机系统、社交服务和聊天软件里了。比如微软 Cortana、苹果 Siri 和 Google Now，从聊天机器人的角度来看它们都属于这个范畴；微软小冰则已经出现在了微博、微信里；Slack 虽说是个工作用的 IM 软件，里面也有很多 Bot，具有各种有意思的功能；微信就更别说了，公众/服务号的自动回复也可以被理解为简单的聊天机器人，而微信也对服务号的运营者开放了接口，允许他们接入采用第三方服务设计聊天机器人，来满足用户的更多需求。现在来看 Bot 出现在 IM 软件里最多。原因显而易见：Bot 是帮用户边聊天边把事办了，而IM 软件对于用户来说就是聊天用的……更何况，如果要说IM 是移动应用之王，相信没有人会反对吧？谁在开发这些 Bot？更合适的方式，是先把这些 Bot 背后的拥趸分成两个组别：平台方和服务方。平台方指的是所有那些允许 Bot 在自己的系统、软件等平台上出现，那些鼓励开发者在自己平台上开发 Bot 的公司。比如微软基于 Cortana 的经验、自然语言理解技术开发了一个Bot 框架工具。开发者可以开发 Bot 并放到 Skype 上，也可以以 API 形式集成到其他聊天软件里；出现在 Skype 里的 Bot，以 Cortana 的形态存在。Facebook 跟微软几乎雷同，但它主要是想让第三方服务商把 Bot 放到自家的 IM 软件 Messenger 上；Slack 和 Telegram 也一样。你可以把这些公司看做 Bot 平台。但这些公司首先要向第三方开放一定量的用于开发 Bot 的技术，以及开放自家 IM 软件的 API ，好让第三方开发完了 Bot 能放进去。而服务方，指的是那些把自己提供的具体服务变成 Bot 的形态，放到平台上的公司。比如披萨速递公司达美乐 (Domino’s) 就在跟微软合作，让用户可以在 Skype 上用 Cortana 点披萨；再比如 电商公司 Spring、新闻服务 CNN 和天气服务 Poncho，这三家公司已经作为首批合作伙伴，把自己的服务做成了 Bot 放到了 Facebook 的 Messenger 上。Poncho 和 Spring：它们都是第三方提供的服务，可以以 Bot 形态跟 Messenger 用户聊天，但并不限于 Facebook 的平台。当然也有一些趁着这股 Bot 的势头获得了知名度的小型公司，专门夹在平台和服务商之间提供开发 Bot 的技术支持。比如硅谷有一家名叫 api.ai 的公司，专门帮助第三方减少 Bot 的开发时间，降低 Bot 的反应时间，提高对话的拟真程度，从而提升用户体验。而说到 Bot，亚马逊也是最近一年在这方面有所成就的一家公司。它曾经推出过一个名为 Echo 的音响系列。你要问了，亚马逊卖 Kindle 可以看书也就算了，卖音响用来干什么呢？实际上，这个音响里也有一个数字助理名叫 Alexa。跟 Siri 差不多，除了能帮你处理一些日常的简单任务之外，Alexa 最大的功能就是可以直接帮你在亚马逊上买东西。当然，送到家里还是要靠真人快递员的，但把 Alexa 也算作一个 Bot，是没有任何问题的。可以说，因为微软、Facebook、亚马逊等巨头公司的推进，现在 Bot 已经成为了互联网科技行业中又一个崭新的热门类别了。Bot 能做什么？相信你看完上面这几段描述，已经对 Bot 的能力大概有所了解了。可以说，Bot 可以帮你做到任何事情，无论是订飞机火车票，还是追踪一个快递的位置，甚至在你最没头绪的时候，帮你选好今晚应该送给太太的生日礼物。Bot 能做到很多事情，但更重要的是它能帮你自动化很多繁琐的事务，让你在一个场景下（比如 IM 应用）里就把所有的事情都办了。PingWest品玩在 Slack 里使用的 Bot为什么 Bot 如此厉害？因为那些驱动它们的技术在近几年有了突飞猛进的发展……首先是 AI。基于最先进的卷积神经网络，再整合相对传统但仍然有效的蒙特卡洛树搜索技术，Google 的人工智能 AlphaGo 在人们普遍认为机器无法驾驭的围棋项目上，赢下了世界上最强大的围棋选手李世乭职业九段。围棋都能下了，帮你叫个外卖还不是小菜一碟？其次是与对话相关的技术。自然语言处理技术已经如此发达，以至于你很难想象，现在的计算机软件已经能轻松理解那些高度口语化，甚至口音严重的闲聊。其实机器人不光能听懂一句话说的什么，还能参考上下文，在一段连续的对话中理解你的意图，帮你处理各种事务。目前这些 Bot 大部分还都在文字对话阶段，但对语音对话支持已经近在眼前了。Bot 会取代 App 吗？另一个让 Bot 突然热闹起来的原因是大公司的推进。以微软和 Facebook 举例：Skype 有超过 3 亿 月活跃用户，Facebook Messenger 有 9 亿月活跃用户……当用户量如此巨大的 IM 软件变成了各种 Bot 服务平台，它们对平台方带来的流量入口价值是十分显著的。苹果公司和 Google 在移动时代地位如此显赫，App Store 和 Google Play 的功劳巨大。任何提供服务的 App 想要来到用户的面前，都要先经过 App Store 和 Google Play，让这两家公司变成了流量的入口和 App 的把关人；而现在，当Skype、Messenger 成为了新的服务的聚合处，用户可以直接在 IM 软件里找到自己需要的服务。倘若这种模式被用户接受，未来的普及度越来越高，你很容易看出微软和 Facebook 将有机会取代苹果和 Google 现在的地位——我说的是倘若。Facebook 相信 Messenger 平台有能力接入数以万计的 Service Bot。到那时，它将从一个 IM 成为一个 OS……但显然，Bot 取代 App 不是说说就能做到的，毕竟不是所有人都喜欢那种跟机器人聊天的诡异的感觉。更何况也不是所有的 App 功能都能被 Bot 取代：比如玩游戏，可能除了 Lifeline 这种纯粹对话型的游戏能用 Bot 来玩，其他的游戏仍然需要够大的窗口来显示画面，以及独立的交互；再比如电商购物，就算 Facebook 展示了能用 Messenger 买东西，大家肯定还是喜欢自己挑东西，而不是等着机器人给自己推荐。但现在来看，很多服务性质简单（提供信息），功能单一的 App 很有可能第一波遭到取代的风险，比如天气、新闻、订餐、机票和酒店预订服务等。但这并不是说一定会取代，只是说那些需要立刻搞定琐事的人，可能会觉得让 IM 里的机器人代管这些琐事来的更方便一些。"""
testTxt5 = """看到AlphaGo以4：1碾压人类最优秀的围棋选手时，我的第一反应是，唉，小学时我就下不过小霸王学习机上的“象棋大师”了，如果你从小就爱玩游戏，那很多年前，你应该就接触过AI（人工智能）这个词，很多游戏的单机模式用它来指代由程序控制的电脑玩家，我和小伙伴们统称之为“电脑人”。不知道你的经历如何，我学习游戏的过程基本就是被“电脑人”惨虐的过程：红色警戒，开局对方一阵异常猛烈的攻势经常让我撑不过5分钟；CS（反恐精英），电脑人飘忽不定的走位和精准的枪法也时不时让我怀疑人生；最惨的是Dota，AI的反应速度简直是神级水准，最初学习游戏的很长一段时间，杀一次AI都会让我兴奋半天。Dota的游戏画面为什么我们对这些游戏里的AI早就习以为常，却对AlphaGo这个人工智能系统战胜李世石大惊失色，开始认真考虑机器会不会取代人类？如果你有类似的疑问，那就来了解一下游戏AI是怎么工作的吧。“我就静静地等着你来唤醒”很多MMO游戏（大型多人在线游戏）走的就是这个路子，游戏里的NPC（非玩家角色）出现的时间、地点，遇到NPC后续的剧情等都是提前设定好的，玩家在完成游戏任务的过程中，按照提示和NPC相遇，就能触发预设的剧情。这是最简单的游戏AI类型之一，实现难度也不高，主要依赖一种被称为“有限状态机”的解决方案，即当满足某种状态时，AI才会从一个状态转移到下一个状态，而且状态总数是有限的，这也是游戏AI实现更高级的动作的基础。网络游戏中的NPC如果你接触过编程，简单来说“有限状态机”就是一堆if else语句：“如果玩家点了对话，AI就把任务告诉他”，“玩家完成了一个任务，AI就把奖励给他”……当然，这类AI的缺点也不言自明：即使从表面来看，它也太不智能了。“对面有一个敌人，砍！对面有一群敌人，跑！”像CS（反恐精英）这样的射击游戏和Dota这样的即时战略游戏，AI就需要做一些复杂的事情了。在玩CS时，你会发现“电脑人”有时会蹲下瞄准射击（准确度最高但也最容易被击中），有时又会选择跑动射击（准确度降低但可以躲避子弹）；在Dota中，电脑控制的英雄有时会坚决地试图击杀你，有时看到你又掉头就跑。CS GO中的“电脑人”这个时候，游戏AI在什么情况下执行什么状态就需要一个决策支持系统。知乎用户韦易笑用篮球游戏AI解释了何为决策支持系统，如果又兴趣你可以进一步了解。简单来说，游戏AI要根据当前的游戏情况来确定首要目标是进攻还是防守，之后，再根据不同的情况决定具体的策略。比如在一场篮球游戏中，整个球场被划分为若干个相同的格子，球员和篮板所在格子的距离、球员和球员之间的距离等都会有一个分值。当球在AI手中时，它的首要目标就是进攻，具体执行防守策略时，持球队员和防守队员之间的距离、和队友间的距离、和篮筐的距离都会有一个分值，这些分值根据不同的加权相加，会得到一个总分数。AI根据这个总分值确定接下来采取的行动。这一类AI就聪明多了，毫秒级的响应速度让它们反应迅速，操作犀利，游戏的初学者通常很难战胜他们。“你下一步，我已经算出了之后的12步”在五子棋、国际象棋、围棋等游戏中，AI的行动同样依靠类似的决策支持系统，对当前局面下的每一种合法走法所直接导致的局面进行评估，然后选择“获胜概率”最高的局面所对应的那个走法。和要在毫秒之间做出反应的即时战略游戏不同，的计算时间比较宽裕，游戏规则也更加明确。不过，这并不意味着这类AI的开发难度更低。拿国际象棋来说，每盘旗大约80步，每一步有35种可选下法，所以要计算35^80种情况，大概是10^124。而在人类已经观测到的宇宙中，原子的数量才10^80个。即使是对每秒可以计算2亿步棋的“深蓝”超级计算机来说，这个数字也过于庞大。深蓝和国际象棋大师卡斯帕罗夫对弈 / AP Photo/George Widman所以，“深蓝”还采用了剪枝算法。通俗来说就是，“深蓝”在下棋时会往前看几步（比如12步），然后对棋局进行打分（分数越大表明对我方越有利，反之表明对对方有利），并将该分数向上传递。当搜索其他可能的走法时，会利用已有的分数，减掉对我方不利对对方有利的走法，尽可能最大化我方所得分数，按照我方所能得到的最大分数选择走步。所以，理论上来说，当AI的搜索深度，也就是能往前看的步数大于人类时，它获胜的概率就大大提高。“深蓝”战胜人类象棋大师，是一个里程碑式的事件。为什么AlphaGo值得我们特别关注回到开头的问题，为什么AlphaGo战胜李世石值得我们特别关注呢？首先，相比国际象棋，围棋的复杂程度是呈指数级上升的。即使在深蓝战胜人类最优秀的国际象棋大师后很多年，能和职业围棋手过招的人工智能依然迟迟没有突破，甚至就在比赛前，多数意见都认为AlphaGo战胜李世石。AlphaGo做到了，它依靠的是“两个大脑”：政策网络（policy）和价值网络（value network），前者用来预测下一步，后者用来预测棋盘上不同的分布会带来什么不同的结果。政策网络可以把非常复杂的搜索树减到可操作的规模，AlphaGo只需要从几十种最有前景的“下一步”中选择一种；价值网络则能减少搜索的深度，AlphaGo不用往下看几百步，只需要搜索最有价值的10-20多步。还有更不一样的，AlphaGo并不是只会下围棋，它背后的人工智能系统一种具有广泛适应性的强化学习模型，也就是说，用同样一套算法，它可以下围棋，也可以玩打砖块、太空侵略者等。AlphaGo所属的DeepMind公司CEO Demis Hassabis曾在一个演讲中科普过这个系统，还展示了它经过学习后快速掌握几款游戏的成果。演讲深入浅出，很值得看：这个过程像什么？不就是人脑学习的过程嘛！而这种通用型的人工智能被称为强人工智能，和那些专门为了一个游戏开发的游戏AI有本质不同。"""
testTxt6 = """本文来自TalkingData首席数据科学家 张夏天AlphaGo与李世石的对战已经进行了四局。前三局世人惊叹于AlphaGo对李世石的全面碾压，很多人直呼人类要完。因为被视为人类智能的圣杯－围棋，在冷酷的机器（或者是疯狂的小狗）面前变成了唾手可得的普通马克杯，而人类的顶尖棋手似乎毫无还手之力。3月12号的第四局，李世石终于扳回一居，而且下了几手让人惊叹的好棋。特别是第78手，围棋吧很多人赞为“神之一手”，“名留青史”，“扼住命运喉咙的一手”。因为这一局，围棋吧的主流舆论已经从前几天的震惊, 叹息，伤心，甚至是认为李世石收了谷歌的黑钱转变为惊喜，甚至认为李世石已经找到了打狗棒法。而人类要完党则认为这比AlphaGo 5:0 大胜更可怕，因为这只狗甚至知道下假棋来麻痹人类，真是细思极恐。不论怎样，AlphaGo在与人类顶尖围棋高手的对决中已经以3胜的优势锁定了胜局，李世石目前只是在为人类的尊严而战了。围棋一年前还通常被认为是10年内都无法被人工智能攻克的防线，然而转眼就变成了马其诺防线了。那么这场人机大战到底意味着什么？人类已经打开了潘多拉魔盒吗？ AlphaGo的胜利是否意味着人工智能的黑色方碑（图1， 请参见电影《2001：太空漫游》）已经出现? 本文将从AlphaGo的原理入手逐步探讨这个问题。1.AlphaGo的原理网上介绍AlphaGo原理的文章已经有不少，但是我觉得想深入了解其原理的同学还是应该看看Nature上的论文原文 “Mastering the game of Go with deep neural networks and tree search”。虽然这篇文章有20页，但是正文部分加上介绍部分细节的Method部分也就8页，其中还包括了很多图。个人觉得介绍AlphaGo的原理还是这篇最好。为了后面的讨论方便，这里对其原理做简要总结。对于围棋这类完全信息博弈，从理论上来说可以通过暴力搜索所有可能的对弈过程来确定最优的走法。对于这类问题，其难度完全是由搜索的宽度和深度来决定的。1997年深蓝解决了国际象棋，其每步的搜索宽度和深度分别约为35和80步。而围棋每步的搜索宽度和深度则分别约为250和150步，搜索计算量远远超过国际象棋。减少搜索量的两个基本原则是：1. 通过评估局势来减少搜索的深度，即当搜索到一定深度后通过一个近似局势判断函数(价值函数)来取代更深层次的搜索；2. 通过策略函数来选择宽度搜索的步骤，通过剔除低可能性的步骤来减少搜索宽度。很简单的两个原则，但难度在于减少搜索量和得到最优解之间是根本性矛盾的，如何在尽可能减少搜索量和尽可能逼近最优解之间做到很好的平衡才是最大的挑战。传统的暴力搜索加剪枝的方法在围棋问题上长期无法有大的突破， 直到2006年蒙特卡洛树搜索(Monte Carlo Tree Search)在围棋上得到应用，使得人工智能围棋的能力有了较大突破达到了前所未有的业余5-6段的水平。MCTS把博弈过程的搜索当成一个多臂老虎机问题（multiarmed bandit problem），采用UCT策略来平衡在不同搜索分支上的Exploration和Exploitation问题。MCTS与暴力搜索不同点在于它没有严格意义的深度优先还是宽度优先，从搜索开始的跟节点，采用随机策略挑选搜索分支，每一层都是如此，当随机搜索完成一次后，又会重新回到根节点开始下一轮搜索。纯随机的搜索其效率是极低的，如同解决多臂老虎机的问题一样，MCTS会记录每次搜索获得的收益，从而更新那些搜索路径上的节点的胜率。在下一轮搜索时就可以给胜率更高的分支更高的搜索概率。当然为了平衡陷入局部最优的问题，概率选择函数还会考虑一个分支的被搜索的次数，次数越少被选中的概率也会相应提高。面对围棋这么巨大的搜索空间，这个基本策略依然是不可行的。在每次搜索过程中的搜索深度还是必须予以限制。对于原始的MCTS采取的策略是当一个搜索节点其被搜索的次数小于一定阈值时（在AlphaGo中好像是40）， 就终止向下搜索。 同时采用Simulation的策略，从该节点开始，通过一轮或者若干轮随机走棋来确定最后的收益。当搜索次数大于阈值时，则会将搜索节点向下扩展。Wikipedia上MCTS词条中的示例图（图2）展示了MCTS的四个步骤：AlphaGo其基本原理也是基于MCTS的，其实一点也不深奥。但是AlphaGo在MCTS上做了两个主要的优化工作，使得围棋人工智能从业余水平飞跃至职业顶尖水平。这两个优化工作分别是策略网络和价值网络，这两个网络都是深度神经网络，本质上是还是两个函数。这两个网络分别解决什么问题呢？在原始MCTS中的选择步骤中，开始的那些搜索只能纯随机的挑选子节点，其收敛效率显然是很低的。而策略网络以当前局势为输入，输出每个合法走法的概率，这个概率就可以作为选择步骤的先验概率，加速搜索过程的收敛。而价值网络则是在仿真那一步时直接根据当前局势给出收益的估值。 需要注意的是在AlphaGo中，价值网络并不是取代了随机走棋方法，而是与随机走棋并行（随机走棋在CPU上而价值网络在GPU上运行）。 然后将两者的结果进行加权(系数为0.5)。当然AlphaGo的随机走棋也应该是做了大量的优化工作，可能借鉴了之前的一些围棋人工智能的工作。摘自AlphaGo论文的图3清晰展示了策略网络和价值网络如何将围棋人工智能的水平从业余水平提升到职业水平（Rollouts就是随机走棋）。因此AlphaGo的精髓就是在策略网络和价值网络上。策略网络可以抽象为, 其中s为当前局势，a为走法，其实就是在当前局势下每一个合法走法的条件概率函数。为了得到这个函数，AlphaGo采用的监督学习的办法，从KGS Go Server上拿到的三千万个局势训练了深达13层的深度神经网络。这一网络能将走法预测准确度提高到57%。如果将这一问题看成一个多分类问题，在平均类别约为250个的情况下取得57%的精确度是十分惊人的。在这个训练过程中，其目标是更看重走法对最后的胜负影响而不仅仅是对人类走法的预测精度。 这个深度学习网络的预测耗时也是相当大的（需要3毫秒）。为此AlphaGo又用更简单的办法训练了一个快速策略函数作为备份，其预测精度只有24.2%但是预测耗时仅为2微秒，低1000个数量级。需要注意的是，AlphaGo实际使用的策略网络就是从人类棋谱中学到的策略网络，而并没有使用通过自我对弈来强化学习获得的策略网络。这是因为在实际对战中，监督学习网络比强化学习网络效果要好。价值网络是个当值函数，可以抽象为， 即当前局势下的收益期望函数。价值网络有14个隐层，其训练是通过采用强化学习策略网络AlphaGo的自我对弈过程中产生的局势和最终的胜负来训练这个函数。强化学习或者说自我学习这个过程是大家对AlphaGo最着迷的部分，也是药丸党最忧心的部分。这个过程甚至被解读成了养蛊，无数个AlphaGo自我拼杀，最后留下一个气度无比的。但读完论文发现，强化学习的作用其实并没有那么大。首先是强化学习是在之前学习人类棋谱的监督学习网络的基础上进一步来学习的，而不是从0基础开始。其次，强化学习网络的并没有用在实际博弈中，而是用在训练价值网络中。而且在训练价值网络中，并不是只使用那条最强的蛊狗，而是会随机使用不同的狗。个人认为，强化学习在AlphaGo中主要是用来创造具有不同风格的狗，然后通过这些不同风格的狗训练价值网络，从而避免价值网络的过拟合。这可能是因为目前人类棋谱的数量不够用来训练足够多的水平高的策略网络来支持价值网络的训练。2.AlphaGo到底从人类经验中学到了什么？个人认为，AlphaGo有某种程度的超强学习能力，能够轻松的学习人类有史以来所有下过的棋谱（只要这些棋谱能够数字化），并从这些人类的经验中学到致胜的秘诀。但显然，AlphaGo下围棋的逻辑从人类看起来肯定是不优美的。MCTS框架与人类棋手的布局谋篇完全没有相同的地方，只是冷冰冰的暴力计算加上概率的权衡。策略网络学习了大量人类的策略经验，可以非常好的判断应该走哪一步，但并不是基于对围棋的理解和逻辑推理。如果你要问为什么要选择这一步，策略网络给出的回答会是历史上这种情况90%的人都会走这一步。而策略网络呢，学习的是当前局面的胜负优势的判断，但是它同样无法给出一个逻辑性的回答，而只能回答根据历史经验，这种局面赢的概率是60%这样的答案。有些人说，这种能力近乎人的直觉，但我觉得人类直觉的机制应该比这复杂得多，我们的直觉无法给出判断的概率， 或者说人类的思维核心并不是概率性的。AlphaGo从大量人类经验中学到了大量的相关性的规律（概率函数），但是确没有学习到任何的因果性规律。这应该是AlphaGo和人类棋手最本质的区别了。3.AlphaGo超越了人类的智能了吗？要回答这个问题，首先要明确超越的定义。如果说能打败人类顶尖棋手，那AlphaGo在围棋上的智能确实是超越了人类。 但是假设，人类再也不玩围棋了，没有更新的人类棋谱，AlphaGo的围棋智能还能提高吗？ 从前面的分析看， AlphaGo的自我学习过程作用并不是那么大，这点我是表示怀疑的。也许人类沉淀的经验决定了AlphaGo能力的上界，这个上界可能会高于人类自身顶尖高手。但是当人类不能继续发展围棋，AlphaGo的能力也就会止步不前。从理论上来说围棋可能发生的变化数量是个170位数， 这是人类和计算机的能力都无法穷尽的。无论是人类的逻辑推理，还是人工智能的搜索策略，陷入局部最优是无法避免的命运。而目前AlphaGo的机制，决定了其肯定是跟着人类掉进坑里（某些局部最优）。如果人类不能不断的挖掘新坑（新的局部最优，或者围棋新的风格和流派），AlphaGo能跳出老坑的可能性并不是太大。从这个意义上来说，AlphaGo在围棋上超越人类智能应该还没有实现。4.AlphaGo会故意输给李世石吗？12号这一局有人认为是AlphaGo故意输给李世石，或者为了保存实力，或者为了能够进入排名。但是从Google公开的原理来看，其显然不具备做这样决策的机制。AlphaGo的机制就是追求当局取胜，完全没有考虑各局之间的关系，更没有人工智能伟大崛起的战略目标。 AlphaGo故意输只是句玩笑而已。真要说故意，那也只可能是DeepMind中的人干的事情。5.人类能否战胜AlphaGo？李世石赢了一局，围棋吧不少人都认为人类找到了克制AlphaGo的打狗棒法。就是不要把狗当人，不要用人的思维对待狗，我们需要大胆跳出以往的经验，去寻找神之一手。结合前面的分析，我觉得这个思路是对的。本质上AlphaGo是在追随人类围棋的发展，如果人类不能跳出自己的窠臼，则只会被在这个窠臼中算无遗策的AlphaGo碾压。人类棋手可以通过自己的逻辑推理，寻找跳出当前局部最优的方法。但这也不是一件容易的事情，跳出经验思维，更多的可能性是陷入更大的逆势，这对人的要求太高了，也只有顶尖棋手才有可能做到。而且AlphaGo也能够不段的学习新的经验，神之一手可能战胜AlphaGo一次，但下一次就不见得有机会了。AlphaGo就如同练就了针对棋力的吸星大法，人类对他的挑战只会越来约困难。6.AlphaGo能干什么以及不能干什么？DeepMind的目标肯定不只是围棋，围棋只是一个仪式，来展示其在人工智能上的神迹。看公开报导，下一步可能是星际争霸，然后是医疗，智能手机助手，甚至是政府，商业和战争决策等领域。Demis Hassabis在接受The Verge采访时透露DeepMind接下来关注的核心领域将会是个人手机助手。Hassabis认为目前的个人手机助手都是预编程的，过于脆弱，无法应变各种情况， 而DeepMind想通过人工智能技术，特别是无监督的自我学习方式具有真正智能的真正智能手机助手。这是因为智能手机的输入变化太多，需要巨量的训练样本才能学到有用的东西。而这正是AlphaGo目前主要依赖的方法。为此，Hassabis想挑战让机器的自我学习成为主要的学习方式， 他对此充满了信心。但我认为这个问题可能不是那么好解决的，因为在AlphaGo中自我学习的作用是相对有限的。如果在围棋这种相对简单的环境中，自我学习的作用都相对有限，在更加复杂的环境中要能有很好的自我学习效果其挑战会更加巨大。不过从我们TalkingData的角度来看，把我们的海量移动端数据和监督学习技术相结合，可能更容易实现Hassabis的设想。我个人期待AlphaGo能够创造更大的神迹，但同时也认为其应用还是有一定局限性的。因为并不是所有的实际问题都能找到这么多的训练数据。尤其在政府，商业和战争决策上，穷尽人类历史也找不到多少精确的训练集，而问题本身的复杂性又是超过围棋这种完全信息博弈的。在这种情况下，恐怕很难学到足够准确的策略网络和价值网络。这就使得AlphaGo的方法面对这些问题，可能是完全无法解决的。"""
testTxt7 = """2014年，O2O是进击的一年。对于教育领域，家教O2O的模式被越来越多的创业者采纳，现在这个市场上，出现了多个玩家，例如跟谁学、轻轻家教、老师来了、神州佳教、请他教、师全师美、突破互动等等。但事实上，这并不是一个新鲜的模式，过去O2O的Online端口可能并不集中在移动设备，而是电话（华东师范大学家教中心），或者是一个简单的答疑产品，例如早期的211高考梦工厂，力强，问吧教育等。O2O模式是否能够在教育领域跑通，从过去开始就有很多质疑。1. 家教的选择并不是一个频率很高的选择，老师和家长建立沟通之后可以完全抛弃平台；2. 家教服务并不是一个标准化的服务形式，而非标准化的服务不容易品控，服务质量得不到保证，就会影响平台的公信力。可以说，目前这类平台的主要作用是帮助那些个人和小机构获得流量，而在家长端痛点的解决则并不显著。那么，为什么从2014年下半年开始，家教O2O会出现大爆发呢？“轻轻家教”的创始人胡国志分享了他的看法。私人家庭教师职业化&nbsp;目前，私人家庭教师已经逐渐成为一个职业，每年师范类学校毕业的学生大部分都无法进入公立学校，他们形成了目前私人教师的主力军，这部分人群现在是在50万人左右。高学费低课酬悬殊化 机构老师目前处于一个低收入状态。传统1对1机构中老师课时费在家长所交全部学费中占比仅20%左右。即使是这样，机构每年暑假前也还在从高校招应届毕业生，来降低他们的运营成本，而对于成熟老师来说，他们只能够选择从机构大量出走，自由执业，以便获得更多的收入。&nbsp;移动助力双选简单化&nbsp;移动互联网的时代到来，让服务者和消费者双方的联系建立变得更加快速。基于地理位置的推荐，通过各种社会化媒体进行分享，对于老师来说，即使离开机构也能获得新家长用户，而家长可以获得更多的教师选择。互评促进供需诚信化&nbsp;点评模式已经成为服务产品一个必备的要素，它会深刻影响到用户的产品体验，影响他们的购买决策。而当点评引入家教O2O产品之后，会在家长和老师之间形成良性循环，家长可以选择到好老师，刺激消费，而老师也会因为点评不断改进教学。草根翻身革命井喷化目前，培训机构的老师都在做自媒体，越来越多的优秀老师都有自己的工作室，大背景下，就会刺激在互联网上产生一种平台和渠道产品的必要性。本文来自轻轻家教创始人胡国志在“未来之星”上的分享，作者在其基础上增加了自己的思考。原创文章，作者：荔闽"""
testTxt8 = """来自The Verge的消息，苹果刚刚发布了新款入门级5K分辨率iMac，同时升级了15寸MacBook Pro产品线。新款5K分辨率iMac配备了英特尔3.3GHz四核Core i5处理器、AMD Radeon R9&nbsp;M290显卡、8GB内存和1TB硬盘，售价1999美元。当然你也可以选择定制升级，比如将硬盘换成Fusion Drive。除此之外苹果还将高配iMac的售价调低至2299美元，但配置保持不变。这款高配iMac在去年10月上市时的售价为2499美元。除了一体机，苹果还升级了15寸MacBook Pro。升级后的这一系列笔记本电脑采用了Force Touch触控板和更快的闪存。值得一提的是，再有不久你就可以直接在Apple Store买到新MacBook了。选择困难症患者，可能要挠头了。原创文章，作者：大飛哥"""
testTxt9 = """2014年2月28日，东京比特币交易所Mt Gox申请破产，该公司声称丢失了大约85万枚比特币。近日，一份来自东京比特币安全公司WizSec的调查报告显示Mt Gox丢失的比特币是从2011年开始逐渐从该交易所被偷走的，而这批比特币在Mt Gox破产之前早已失窃，Mt Gox在那之后是通过一部分比特币储备继续运作的，Mt Gox本身对当时比特币的流失是否知情还未查明。被窃的比特币被卖到了包括Mt Gox在内的很多家交易所。根据时间推测这些比特币被卖掉的价格应该比2013年和14年比特币价格最高时低很多。根据上面的图标可以看出，在Mt Gox应该持有的比特币数量和其实际持有的数量之间存在非常悬殊的差距。Mt Gox从2013年5月开始持有的比特币数量仅有约10万枚。那么到底Mt Gox的比特币是被偷了还是他们从始至终都在伪造持有比特币数量的数据呢？报告的作者Kim Nilsson表示这些比特币的确是从Mt Gox交易所流出了，这也表示它们肯定也曾经流入了Mt Gox。Mt Gox的比特币失窃案一直非常扑朔迷离，至今也没查出罪魁祸首，这也暴露了Mt Gox交易所的种种漏洞。原创文章，作者：DingDing"""



# userDicPath = io.getSourceFilePath('tagbase.txt')
# tagbaseList = io.readListFromTxt(userDicPath)
# jieba.load_userdict(userDicPath)
# 提取文章主题
# testTxt = testTxt7.replace('nbsp','').replace('选择','').replace('产品','').replace('一个','').replace('目前','').replace('获得','').replace('他们','').replace('可以','')
# themeList = jieba.analyse.extract_tags(testTxt)
# print('原始提取的词：',themeList)
# for item in themeList:
#     if item in tagbaseList:
#         print(item)

# test = """就在5月6日，中国民用无人机制造商大疆创新（DJI）宣布获得顶级风投Accel的7500万美元投资。但业内人士透露，这只是大疆本轮融资的一部分，其他融资情况将在近期陆续公布。 一向不缺钱的大疆此番进行大额融资，很有可能是为了收购具有潜力的技术型团队，打造更强的竞争实力。这一消息已经得到了一名看过大疆DD的人士确认。而来自&nbsp;recode 消息称，大疆将和Accel共同成立一个单独的投资基金，专门关注无人机生态领域的投资。目前有关这个基金的资金数额以及大疆在其中扮演的角色暂未可知，但可以肯定的一点是，大疆的此番动作将继续拓展其无人机周边相关的软件、硬件布局，建立起一个规模化的无人机生态平台。 一直以来，大疆无人机对于众多消费者而言都将其作为航拍爱好，面对无人机领域越来越多的各路竞争者，尤其是商用领域的大规模拓展（比如医药和物资快递、地图测绘、农耕辅助、安全监控等），对大疆未来发展的确是一个不小的威胁。36氪从一名业内人士那里了解到，大疆目前已经收购了航拍图片社区Skypixel和图像传输公司TAU。而有投资人也告诉36氪，大疆已经把无人机上游公司尤其是供应链领域基本都进行了投资。此次与Accel合作创建投资基金，很有可能将继续扩大大疆的投资版图，拓展应用领域，打造起一个更为庞大的无人机生态体系。原创文章，作者：Jie"""
# test2 = """Apple Watch一表难求，开发者应该是最着急的人。不过这一情况可能得到缓解。苹果通过邮件告知部分开发者称，为了帮助开发者尽早拿到Apple Watch，测试WatchKit App，开发者可以购买配有蓝色腕带的42mm Apple Watch Sport，并保证4月28日之前发货。虽然不清楚苹果为何指定这个配置的Apple Watch，但此款手表的储备应该比较充足。不过，通过这个方式购买Apple Watch依然有名额限制。至于谁是“幸运儿”，则完全随机。有开发者留言称，自己开发并在App Store上架了超过50款App，并有1款App已经适配Apple Watch，但是依然没有收到邮件邀请。也有部分开发者连一个App都没提交过，却收到邮件邀请。感兴趣的开发者可以在美国太平洋时间4月23日上午10点之前注册，苹果将在4月23日反馈购买状态。此外，没有收到邮件提醒的开发者，也能在苹果提供的链接上注册成功。原创文章，作者：feng"""
#
# print(list(jieba.cut(test2)))





# tagbaseFilePath = io.getSourceFilePath('tagbase.txt')
# tagbaseList = io.readListFromTxt(tagbaseFilePath)
# print(tagbaseList)

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