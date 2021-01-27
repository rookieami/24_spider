from cla_object import zhibo8
import requests
import requests
from util import PrintErr
from bs4 import BeautifulSoup
from news.basketball import zb_basketball


url='https://news.zhibo8.cc/zuqiu/more.htm'

def getUrls(url,transform):
    try:
        resp= requests.get(url)
        resp.raise_for_status() #状态码不是200,异常
        resp.encoding='utf-8'
    except Exception as e:
        PrintErr(e)
        return
    return transform(resp) if resp.status_code == requests.codes.ok else None
    #解析原始数据,返回新闻列表
def getPassData(url):
    doc=getUrls(url,lambda resp: BeautifulSoup(resp.text, 'lxml'))
    if doc is None:
        return
    # print(doc)
    for div in doc.select('div.dataList'):
        # print(div)
        for u1 in div.select('u1.articleList'):
            print(u1)

def main():
    zb_basketball.run(url)
if __name__=='__main__':
    main()