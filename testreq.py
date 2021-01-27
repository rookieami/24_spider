import requests
from util import PrintErr
from bs4 import BeautifulSoup
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
    resp = requests.get(url)
    resp.raise_for_status()  # 状态码不是200,异常
    resp.encoding = 'utf-8'
    doc = BeautifulSoup(resp.text, 'lxml')
    if doc is None:
        return
    # print(doc)

    articleinfo={}
    for k in doc.find_all('div',class_='dataList'):
        # print(k)
        for articleList in k.find_all('ul',class_='articleList'):
            for data in articleList.find_all('li'):
                # print(data.get('data-label'))
                # print(data.find('span',class_="articleTitle").find('a').get('href')) #新闻链接
                tag=data.get('data-label')  #标签
                tempTag=tag[1:-1]
                link=data.find('span',class_="articleTitle").find('a').get('href') #url
                title=data.find('span',class_="articleTitle").find('a').text  #标题
                time=data.find('span',class_="postTime").text  #时间
                list=[tempTag,link,title,time]
                index=link.rfind("/")
                ind=link.rfind('.htm')
                key=link[index+1:ind]
                print(key)
                demList=[title,time,tag,link]
                print(demList)
                articleinfo[key]=demList
                print(articleinfo)

                break

                #处理数据
            # print(articleList)


if __name__=='__main__':
    main()
