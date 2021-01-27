from common import news_spider
from bs4 import BeautifulSoup
class ZbClass(news_spider.Spider):
    self.url=url
    def getUrlsData(self,url):
        try:
            resp= requests.get(url)
            resp.raise_for_status() #状态码不是200,异常
            resp.encoding='utf-8'
        except Exception as e:
            PrintErr(e)
            return
        return resp
    #方法重写
    def getPassData(self,url):
        doc=ZbClass.getUrlsData(url,lambda resp: BeautifulSoup(resp.text, 'lxml'))
        print(doc)
        return

