import requests
from xml.etree import ElementTree
from util import PrintErr
from bs4 import BeautifulSoup
class Spider(object):
    #解析url下的内容,返回原始数据
    def getUrlsData(sele,url):
        # try:
        #     resp= requests.get(url)
        #     resp.raise_for_status() #状态码不是200,异常
        #     resp.encoding='utf-8'
        # except Exception as e:
        #     PrintErr(e)
        #     return
        return resp
    #解析原始数据,返回新闻列表
    def getPassData(self,data):
        # doc=self.getUrlsData(url,lambda resp: BeautifulSoup(resp.text, 'lxml'))
        # if doc is None:
        #     return
        # return doc
        return

    # def get