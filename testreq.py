#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from util import PrintErr
from bs4 import BeautifulSoup
import bs4
import re
from util import fromatContent,timeToStamp,getEndTime

import time
import datetime
from class_obj.zhibo import zhibo8
import defind
from store import req_url

url = 'https://news.zhibo8.cc/zuqiu/more.htm'


def getUrls(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status()  # 状态码不是200,异常
        resp.encoding = 'utf-8'
    except Exception as e:
        PrintErr(e)
        return
    return resp
    # 解析原始数据,返回新闻列表


def getPassData(url):
    doc = getUrls(url, lambda resp: BeautifulSoup(resp.text, 'lxml'))
    if doc is None:
        return
    print(doc)


def main():
    # resp = requests.get(url)
    # resp.raise_for_status()  # 状态码不是200,异常
    # resp.encoding = 'utf-8'
    # doc = BeautifulSoup(resp.text, 'lxml')
    # if doc is None:
    #     return
    # print(doc)

    # articleinfo={}
    # for k in doc.find_all('div',class_='dataList'):
    #     # print(k)
    #     for articleList in k.find_all('ul',class_='articleList'):
    #         for data in articleList.find_all('li'):
    #             # print(data.get('data-label'))
    #             # print(data.find('span',class_="articleTitle").find('a').get('href')) #新闻链接
    #             tag=data.get('data-label')  #标签
    #             tempTag=tag[1:-1]
    #             link=data.find('span',class_="articleTitle").find('a').get('href') #url
    #             title=data.find('span',class_="articleTitle").find('a').text  #标题
    #             time=data.find('span',class_="postTime").text  #时间
    #             list=[tempTag,link,title,time]
    #             index=link.rfind("/")
    #             ind=link.rfind('.htm')
    #             key=link[index+1:ind]
    #             print(key)
    #             demList=[title,time,tag,link]
    #             print(demList)
    #             articleinfo[key]=demList
    #             print(articleinfo)

    #             break

    #             #处理数据
    #         # print(articleList)

    # resp = requests.get('https://news.zhibo8.cc/zuqiu/2021-01-26/match602536date2021v.htm')
    # resp.raise_for_status()  # 状态码不是200,异常
    # resp.encoding = 'utf-8'
    # # doc = BeautifulSoup(resp.text, 'lxml')
    # doc=BeautifulSoup(resp.text, 'lxml')
    # if doc is None:
    #     return
    #             #解析详情页，获取首张图，文章正文
    #             #signals > p:nth-child(1) > img
    # content=doc.find('div',class_='content')
    # # print(content)
    # # print(content.string)
    
    # imgTag=content.find('img')
    # img=""
    # if imgTag is not None:
    #     img=imgTag.get('src')
    # # print("妖兽啦,没标签啊")
                
    # stri=''
    # for na in content:
    #     # # print(type(na))
    #     if isinstance(na,bs4.element.Tag):
    #     #     if na.find('style') is not None:
    #     #         na.style.extract()
    #     #     #     # continue
    #     #         print(na)
    #     #     if na.string is None:  #过滤图片
    #     #         # print(na)
    #     #         continue #移除该标签
    #     #         # pass
    #     #     if na.attrs=={'class': ['img-info']}: #过滤图片注释
    #     #         # print(na.attrs)
    #     #         continue  
    #         if na.name !='p':
    #             # print(na.name)
    #             continue
                
    #     stri+=str(na)

    # print(stri)
       
    
    # ##测试字典追加是否更改
    # testMap={1:{'name':"lsh",'age':1},2:{'name':"lzw",'age':18}}
    # print(testMap)
    # data=testMap[1]
    # data['test']=None
    # print(testMap)
    # p

    #字符截取测试
    # str='//news.zhibo8.cc/zuqiu/2021-01-28/60121cb3e07c7.htm'
    # rindex=str.rfind("/")
    # lindex=str.rfind('.htm')
    # print(str[rindex+1:lindex])
    # print(str+"woe")


    #正则校检
#     stri='\n<style>\na.jijin-link {\n\tmargin: 10px auto;\n\tdisplay: block;\n\twidth: 540px;\n}\n\n.jijin-box {\n\twidth: 540px;\n\theight: auto;\n\tmargin: 0 auto;\n\tposition: relative;\n}\n.jijin-box .jijin-img{width:100%;}\n.jijin-thumb {\n\tposition: absolute;\n\tleft: 0;\n\ttop: 0;\n\tbottom:0;\n\tright:0;\n\tbackground: url(\'//tu.duoduocdn.com/uploads/news/day_170418/20170418143737_video_player.png\') no-repeat center center;\n\tbackground-size: 110px;\n}\n\n.jijin-box b {\n\tposition: absolute;\n\tleft: 90px;\n\tright: 15px;\n\tcolor: #333;\n\tline-height: 50px;\n\toverflow: hidden;\n\ttext-overflow: ellipsis;\n\twhite-space: nowrap;\n\tfont-size: 16px;\n}\n</style>\n<a  href="//www.zhibo8.cc/zuqiu/2021/0124-match596997v-jijin.htm">\n<div >\n<img  src="//tu.duoduocdn.com/v/img/210124/382268_01040043517.jpg"/>\n<div >\n</div>\n</div>\n</a><p>直播吧1月24日讯 北京时间1月24日01:15，西乙第22轮，西班牙人客场挑战赫罗纳。上半场，恩巴尔巴远射中柱，帕布洛-莫雷诺助赫罗纳取得领先；下半场，普阿多头球中柱，武磊第77分钟替补登场，但没有太多机会。最终，西班牙人客场0-1不敌赫罗纳。</p><p ><img alt="" src="//tu.duoduocdn.com/uploads/news/day_210124/202101240306411665.jpg" width="500"/></p><p>本场比赛之前，前21轮战罢，西班牙人取得14胜3平4负的战绩，积45分领跑西乙积分榜，赫罗纳8胜6平7负，积30分排名西乙第8位。西班牙人本场首发方面，德托马斯领衔出战，武磊替补待命。</p><p>随着主裁判的一声哨响，双方比赛正式开始。第5分钟，恩巴尔巴开出角球，中路德托马斯高高跃起头球攻门角度太正，赫罗纳门将胡安-卡洛斯将球抱住。<span >↓</span></p><p ><span ><img alt="" referrerpolicy="no-referrer" src="http://wx1.sinaimg.cn/mw690/008dBGCAly1gmy4zr82afg30ba05a7wj.gif"/></span></p><p>第11分钟，恩巴尔巴前场任意球直接攻门，胡安-卡洛斯稳稳没收皮球。第12分钟，西班牙人打出精彩配合，恩巴尔巴送出直塞球，普阿多前插突入禁区内一脚劲射高出球门。↓</p><p ><img alt="" referrerpolicy="no-referrer" src="http://wx3.sinaimg.cn/mw690/008dBGCAly1gmy58meawdg30ba05a1l1.gif"/></p><p>第17分钟，梅拉梅德禁区前沿强行突破两人防守，随后起脚抽射被胡安-卡洛斯单掌扑出底线。↓</p><p ><img alt="" referrerpolicy="no-referrer" src="http://wx3.sinaimg.cn/mw690/008dBGCAly1gmy5dm7mv8g30ba05a1l2.gif"/></p><p>第20分钟，米格隆右路传中，德托马斯包抄射门被防守球员挡出底线。随后的角球机会，恩巴尔巴开出，大卫-洛佩斯近距离头球攻门，胡安-卡洛斯用腿神勇将球挡出。↓</p><p ><img alt="" referrerpolicy="no-referrer" src="http://wx3.sinaimg.cn/mw690/008dBGCAly1gmy5h37nkzg30ba05a1l1.gif"/></p><p>第22分钟，赫罗纳定位球制造威胁，塞斯禁区内射门被防守球员挡出底线。↓</p><p ><img alt="" referrerpolicy="no-referrer" src="http://wx3.sinaimg.cn/mw690/008dBGCAly1gmy5j0jhbxg30ba05a1l0.gif"/></p><p>第29分钟，恩巴尔巴右路内切后起左脚抽射，皮球遗憾击中立柱弹出。↓</p><p ><img alt="" referrerpolicy="no-referrer" src="http://wx3.sinaimg.cn/mw690/008dBGCAly1gmy5qjporgg30ba05a7wm.gif"/></p><p>第36分钟，巴雷小禁区附近射门被防守球员挡出，不过边裁示意西班牙人进攻球员已经处于越位位置。↓</p><p ><img alt="" referrerpolicy="no-referrer" src="http://wx4.sinaimg.cn/mw690/008dBGCAly1gmy5xwm581g30ba05akjq.gif"/></p><p><strong>第41分钟，赫罗纳取得领先，塞斯送出精彩传球，帕布洛-莫雷诺抽射上角得手，西班牙人0-1落后赫罗纳。↓</strong></p><p ><strong><img alt="" referrerpolicy="no-referrer" src="http://wx3.sinaimg.cn/mw690/008dBGCAly1gmy62g4ltvg30ba05a7wm.gif"/></strong></p><p>半场战罢，西班牙人0-1落后赫罗纳。</p><p>易边再战，第50分钟，赫罗纳门将出击解围不远，德托马斯停球之后面对空门抽射，皮球被门线前的防守球员挡出。↓</p><p ><img alt="" referrerpolicy="no-referrer" src="http://wx1.sinaimg.cn/mw690/008dBGCAly1gmy6syq56lg30ba05ahdy.gif"/></p><p>第54分钟，梅拉梅德大禁区角附近送出精准传中球，普阿多头球攻门再度击中门框。↓</p><p ><img alt="" referrerpolicy="no-referrer" src="http://wx4.sinaimg.cn/mw690/008dBGCAly1gmy6wmkk0og30ba05a7wl.gif"/></p><p>第55分钟，斯图亚尼打入一球，不过主裁示意这位赫罗纳前锋犯规在先，进球无效。↓</p><p ><img alt="" referrerpolicy="no-referrer" src="http://wx4.sinaimg.cn/mw690/008dBGCAly1gmy6y7klm3g30ba05anpe.gif"/></p><p>第64分钟，武磊场边热身。↓</p><p ><img alt="" referrerpolicy="no-referrer" src="http://wx2.sinaimg.cn/mw690/008dBGCAly1gmy76ia9zsg30ba05ab2d.gif"/></p><p>第67分钟，德托马斯左路传中，巴雷头球冲顶被胡安-卡洛斯神勇扑出。↓</p><p ><img alt="" referrerpolicy="no-referrer" src="http://wx2.sinaimg.cn/mw690/008dBGCAly1gmy7anyxurg30ba05akjr.gif"/></p><p>第76分钟，塞斯连续横向摆脱后起脚低射，迭戈-洛佩斯倒地将球抱住。<strong>第77分钟，武磊替补普阿多登场。↓</strong></p><p ><img alt="" referrerpolicy="no-referrer" src="http://wx3.sinaimg.cn/mw690/008dBGCAly1gmy7o8d0dxg30ba05aqv9.gif"/></p><p>全场比赛结束，西班牙人客场0-1不敌赫罗纳。</p><p>双方出场阵容</p><p>西班牙人：13-迭戈-洛佩斯、2-米格隆、4-卡夫雷拉、15-大卫-洛佩斯、3-佩德罗萨、20-凯迪-巴雷（84\' 8-弗兰-梅里达）、10-达德尔、33-尼科-梅拉梅德（84\' 19-巴迪略）、23-恩巴尔巴、9-普阿多（77\' 7-武磊）、11-德托马斯</p><p>未出场替补：1-奥耶尔、34-约安-加西亚、5-卡莱罗、14-梅伦多、17-迪达克、22-巴尔加斯、24-坎布萨诺、26-洛萨诺、27-奥斯卡-希尔</p><p>赫罗纳：1-胡安-卡洛斯、17-卡拉维拉、22-桑蒂-布埃诺、2-贝尔纳多、3-弗兰奎斯塔（46\' 4-拉马略）、14-蒙楚、8-克里斯托弗洛、10-萨穆-塞斯（85\' 26-伊布拉希玛）、11-阿代伊（70\' 20-瓦拉里）、19-帕布洛-莫雷诺（63\' 23-巴塞纳斯）、7-斯图亚尼（70\' 18-西拉）</p><p>未出场替补：25-A-穆里奇、30-若纳坦、9-N-巴斯托斯、16-扬-库托</p><p>（Luca）</p>\n'
#     # '
# #     groupStr=re.search('(<a)[^>]*([^<]*)</a>',stri)
# #     groupStr=re.search('<[a-zA-Z]+.*?>([\s\S]*?)</[a-zA-Z]*?>',stri)
# #     print(string)
# #     if groupStr is not None:
# #         # ('<!--[^>]*-->','',st,0) 
# #         print(groupStr)
# #         print(groupStr.group(2))
# #         st=re.sub('<a href[^>]*>','',stri,0) #<a>标签置空
# #         st=re.sub('</a>','',st,0)
# #         print(st)
#     # li=str(stri)
#     print(type(stri))
#     print(fromatContent(stri,'直播吧'))






    #list双重循环是否修改了
    # lis=[[1,2,4],[1,2,6],[132,3,56]]
    # for v in lis:
    #     v[1]=6  #[[1, 6, 4], [1, 6, 6], [132, 6, 56]]
    # print(lis)  

    #语句拼接
    # querySql="select id from %s where  `type`='%s' and origin_url='%s'" %('mytest','newsType','adqwdwaewd')
    # print(querySql)

    #时间格式化
    #字符串转换为时间戳
    # a='2021-02-01 18:38:43'
    # print(time.strptime(a,"%Y-%m-%d %H:%M:%S"))
    # print(time.mktime(time.strptime(a,"%Y-%m-%d %H:%M:%S")))
    # print(timeToStamp(a))

    

    # zb=zhibo8.ZbClass(defind.FROMZHIBO8)
    # endTime=getEndTime() #获取最新抓取新闻的发布时间
    
    #是否for循环 休眠三分钟 time.sleep(180)
    # doc=zb.getUrlsData(url) #获取HTML
    # dataList=zb.PassHTMLData(doc,endTime) #获取新闻列表 

    # endTime=dataList[-1] #返回新一次抓取最新时间
    # mapl={'6015df99ec8da':{'tag':"lanqiu",
    #                         'link':'https://news.zhibo8.cc/zuqiu/2021-01-24/match596997date2021v.htm',   
    #                         'title':'woede',
    #                         'time':'2012'},}
    # dataList=['https://news.zhibo8.cc/zuqiu/2021-01-31/6015df99ec8da.htm',]
    # #访问新闻url,获取正文图片
    # articleDict=zb.getArticleInfo(mapl,dataList) #所有新闻的数据
    # #检查新闻内容是否缺失
    # urlList=dataList
    # articles=zb.checkData(articleDict,urlList)
    # print(articles)
    # word='直播吧' #过滤词汇
    # missArticle=zb.formatArticle(articles[0],word)
    # intactArticle=zb.formatArticle(articles[1],word)
    # print(intactArticle)
    # #存储数据
    # zb.storageData(missArticle,defind.MISSDATA)
    # zb.storageData(intactArticle,defind.INTACTDATA)



    ## 调用接口
    # data={
    #     "saved_id":12,
    #     "catch_from":1,
    #     "origin_url":'https://news.zhibo8.cc/zuqiu/2021-01-24/600c60d8044b3.htm',
    #     "title":'托纳利任意球吊后点，伊布失扳平良机',
    #     'origin_author':'zhibo8',
    #     "content":'<p>1月24日讯 AC米兰vs亚特兰大第41分钟，托纳利任意球罚下后点，伊布很好的扳平比分的机会，但是皮球偏出球门！</p>',
    #     "img_url":'http://wx2.sinaimg.cn/mw690/71a4f909ly1gmy5o4sptrg20c605su0y.gif',
    #     "all_tags":'甲,AC米兰,亚特兰大,足球',
    #     "origin_publish_at":'2021-01-24 01:47:27',
    # }
    
    # url='http://'+req_url
    # res=requests.post(url=url,data=data)
    # print(res.text)

    apu=(1,2,3,"lsda")
    id=6
    print((id,)+apu)
if __name__=='__main__':
    main()
