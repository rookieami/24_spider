import requests
from xml.etree import ElementTree
from util import PrintErr
from bs4 import BeautifulSoup
class Spider(object):
    def __init__(self,url):
        self.url=url
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

    # def get