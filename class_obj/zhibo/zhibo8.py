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
                        articleDict={
                            'tag':tempTag,
                            'link':link,   #确认这个地方要不要存
                            'title':title,
                            'time':time
                        }
                        articleinfo[key]=articleDict #字典存储该记录
                        urlList.append(link) #记录url
        except Exception as e:
            PrintErr(e)
            return
        return articleinfo,urlList
    
    def getArticle(self,articleInfos,urlList):
        '''
        方法重写
        遍历新闻列表，获取新闻正文，图片
        '''
        for url in self.urlList:
            resp=self.getUrlsData(url) #获取新闻详情页
            try：
                doc=BeautifulSoup(resp.text, 'lxml')
                if doc is None:
                    return
                #解析详情页，获取首张图，文章正文
                #signals > p:nth-child(1) > img
                content=doc.find('div',class_='content')
                img=p.find('img').get('src')
                
                for p in conten.find_all('p'):
                    article+=p.get('p')
                    article+='\n'
                key=getKeys(url)
                info=articleInfos[key].
                info['img']=img
                info['content']=article
                article[key]=info
            except Exception as e:
                PrintErr(e)
                return
        return articleInfos  #返回所有数据，包含完整数据
    def passData(articleInfos):
        ''' 
        解析数据，将字典中数据取出，存入数据库
        '''
        #遍历数据，字典取值
        #判断列表是否>6，完整取值存储
        
        for dataList in articleInfos.values:


                    

                



