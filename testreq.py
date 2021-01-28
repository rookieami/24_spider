import requests
from util import PrintErr
from bs4 import BeautifulSoup
import bs4
import re
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

    # resp = requests.get('https://news.zhibo8.cc/zuqiu/2021-01-28/60101eeb048b3.htm')
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
    # img=content.find('img').get('src')
    # print(img)
    # stri=''
    # for na in content:
    #     # print(type(na))
    #     if isinstance(na,bs4.element.Tag):
    #         if na.string is None:  #过滤图片
    #             continue #移除该标签
    #         # print(na.attrs)
    #         if na.attrs=={'class': ['img-info']}: #过滤图片注释
    #             # print(na.attrs)
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
    stri='<a class="reference external" href="http://www.crummy.com/software/BeautifulSoup/bs3/documentation.html">Beautiful Soup3</a>'
    result_div_list=re.findall('<(.*?)>'stri)
    if 'href' in str(result_div_)

if __name__=='__main__':
    main()
