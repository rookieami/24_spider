from common import news_spider
from bs4 import BeautifulSoup
from util import PrintErr,getKeys
from xml.etree import ElementTree
import requests

class ZbClass(news_spider.Spider):
    def __init__(self,url):
        self.url=url    
        super().__init__(url)
    def getPassData(self,resp):
        try:
            doc=BeautifulSoup(resp.text, 'lxml')
            if doc is None:
                return
            urlList=[] #记录新闻url
            articleInfos={}  #map存储信息
            for k in doc.find_all('div',class_='dataList'):
                for articleList in k.find_all('ul',class_='articleList'):
                    for data in articleList.find_all('li'):
                        tag=data.get('data-label')  #标签
                        tempTag=tag[1:-1] #去除多余的','
                        link=data.find('span',class_="articleTitle").find('a').get('href') #url
                        title=data.find('span',class_="articleTitle").find('a').text  #标题
                        time=data.find('span',class_="postTime").text  #时间
                        key=getKeys(link)         
                        demList=[title,time,tag,link]
                        articleinfo[key]=demList #字典存储该记录
                        urlList.append(link) #记录url
        except Exception as e:
            PrintErr(e)
            return
        return articleinfo,urlList


