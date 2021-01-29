from spider_object import news_spider
from bs4 import BeautifulSoup
from util import PrintErr,getKeys,joinUrl
from xml.etree import ElementTree
import requests
import bs4
class ZbClass(news_spider.Spider):
    def __init__(self, catchFrom):
        # self.url=url    
        self.catchFrom=catchFrom
        super().__init__(catchFrom)
    def PassHTMLData(self,resp):
        '''
        解析html,存储新闻链接列表
        返回[0] 新闻内容 ; [1] 新闻urlList
        '''
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
                        url=joinUrl(link,'https:')
                        title=data.find('span',class_="articleTitle").find('a').text  #标题
                        time=data.find('span',class_="postTime").text  #时间
                        key=getKeys(link)         
                        articleDict={
                            'tag':tempTag,
                            'link':url,   
                            'title':title,
                            'time':time
                        }
                        articleInfos[key]=articleDict #字典存储该记录
                        urlList.append(url) #记录url   
        except Exception as e:
            PrintErr(e)
            return
        respList=[articleInfos,urlList]
        return respList
    
    def getArticleInfo(self,articleInfos,urlList):
        '''
        方法重写
        遍历新闻列表，获取新闻正文，图片
        '''
        for url in urlList:
            resp=self.getUrlsData(url) #获取新闻详情页
            try:
                doc=BeautifulSoup(resp.text, 'lxml')
                if doc is None:
                    return
                #解析详情页，获取首张图，文章正文
                #signals > p:nth-child(1) > img
                content=doc.find('div',class_='content')

                imgTag=content.find('img')
                img=""
                if imgTag is not None:
                    img=imgTag.get('src')
                # print("妖兽啦,没标签啊")
                
                conStr=''
                for p in content:
                    if isinstance(p,bs4.element.Tag):
                        if p.find('style') is not None: #先移除style标签,防止干扰下一步图片过滤
                            p.style.extract()
                        if p.string is None: #标签下内容为空,用来过滤图片
                            continue
                        if p.attrs=={'class': ['img-info']}: #过滤图片注释
                            # print(na.attrs)
                            continue  
                        if p.name !='p':
                            continue
                        conStr+=str(p) #拼接存储文章正文内容
                    
                key=getKeys(url)
                info=articleInfos[key]  #找出单个新闻字典
                #追加元素
                info['img']=img
                info['content']=conStr 
                print(url)
            except Exception as e:
                PrintErr(e)
        return articleInfos  #返回所有数据，包含完整数据
    # def passArticleInfo(self,articleInfo):
    #     ''' 
    #     解析数据，将字典中数据取出，存入数据库
    #     '''
    #     #遍历数据，字典取值
    #     #判断列表是否>6，完整取值存储
        
    #     for dataList in articleInfos.va



                    

                



