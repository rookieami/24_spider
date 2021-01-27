import requests
from util import PrintErr
from bs4 import BeautifulSoup
url='https://news.zhibo8.cc/zuqiu/more.htm'
def getUrls(self,url):
    try:
        resp= requests.get(url)
        resp.raise_for_status() #状态码不是200,异常
        resp.encoding='utf-8'
    except Exception as e:
        PrintErr(e)
        return
    return resp
    #解析原始数据,返回新闻列表
def getPassData(url):
    doc=getUrls(url,lambda resp: BeautifulSoup(resp.text, 'lxml'))
    if doc is None:
        return
    print(doc)
def __init__():
    getPassData(url)