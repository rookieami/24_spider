import requests
from xml.etree import ElementTree
from util import PrintErr
from bs4 import BeautifulSoup
class Spider(object):
    def __init__(self,url,articleInfos,urlList):
        self.url=url #原始爬虫路径
        self.articleInfos=articleInfos   #列表map
        self.urlList=urlList  #新闻列表地址
    def getUrlsData(self):
        ''' 访问url 获取html原始文件
            转换为lxml格式
        '''
        try:
            resp= requests.get(self.url)
            resp.raise_for_status() #状态码不是200,异常
            resp.encoding='utf-8'
        except Exception as e:
            PrintErr(e)
            return
        return resp
    def getPassData(self,BeautifulSoup):
        '''解析内容,返回原始新闻列表'''

        return

    def getArticle(self,articleInfos,urlList):
        '''
        遍历新闻列表，获取新闻正文，图片
        '''
        for url in urlList:
            resp=self.getUrlsData(url)
            
    def passArticleInfo(self,articleInfo,)

