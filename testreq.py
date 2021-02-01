import requests
from util import PrintErr
from bs4 import BeautifulSoup
import bs4
import re
from util import fromatContent,timeToStamp

import time
import datetime


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

    articleinfo={}
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

    resp = requests.get('https://news.zhibo8.cc/zuqiu/2021-01-25/600e6dee1e5dd.htm')
    resp.raise_for_status()  # 状态码不是200,异常
    resp.encoding = 'utf-8'
    # doc = BeautifulSoup(resp.text, 'lxml')
    doc=BeautifulSoup(resp.text, 'lxml')
    if doc is None:
        return
                #解析详情页，获取首张图，文章正文
                #signals > p:nth-child(1) > img
    content=doc.find('div',class_='content')
    # print(content)
    # print(content.string)
    
    imgTag=content.find('img')
    img=""
    if imgTag is not None:
        img=imgTag.get('src')
    # print("妖兽啦,没标签啊")
                
    stri=''
    for na in content:
        # # print(type(na))
        if isinstance(na,bs4.element.Tag):
        #     if na.find('style') is not None:
        #         na.style.extract()
        #     #     # continue
        #         print(na)
        #     if na.string is None:  #过滤图片
        #         # print(na)
        #         continue #移除该标签
        #         # pass
        #     if na.attrs=={'class': ['img-info']}: #过滤图片注释
        #         # print(na.attrs)
        #         continue  
            if na.name !='p':
                print(na.name)
                continue
                
        stri+=str(na)

    print(stri)
       
    
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
    stri='\n<p style="text-align: center;"><img alt="" src="//tu.duoduocdn.com/uploads/day_210129/202101290049394993.jpg"/></p><p>直播吧1月29日讯\xa0<span style="">热刺官方宣布年轻后卫马拉奇（</span>Malachi Fagan-Walcott<span style="">）租借加盟苏冠邓迪联，租期至本赛季结束。</span></p><p><span style="">马拉奇现年</span>18<span style="">岁，是热刺青训营培养的球员。去年</span><span style="">3</span><span style="">月对阵莱比锡的欧冠</span><span style="">1/8</span><span style="">决赛，他在比赛最后阶段替补登场为一线队上演首秀。最近，马拉奇从伤病中复出并开始代表热刺预备队出战比赛。</span></p><p><span style="">（二怪）</span></p> '
    # groupStr=re.search('(<a)[^>]*([^<]*)</a>',stri)
    # groupStr=re.search('<[a-zA-Z]+.*?>([\s\S]*?)</[a-zA-Z]*?>',stri)
    # print(string)
    # if groupStr is not None:
    #     # ('<!--[^>]*-->','',st,0) 
    #     print(groupStr)
    #     print(groupStr.group(2))
    #     st=re.sub('<a href[^>]*>','',stri,0) #<a>标签置空
    #     st=re.sub('</a>','',st,0)
    #     print(st)

    # print(fromatContent(stri,'直播吧'))






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
    a='2021-02-01 18:38:43'
    # print(time.strptime(a,"%Y-%m-%d %H:%M:%S"))
    # print(time.mktime(time.strptime(a,"%Y-%m-%d %H:%M:%S")))
    print(timeToStamp(a))

    
if __name__=='__main__':
    main()
