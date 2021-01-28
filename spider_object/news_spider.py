import requests
from xml.etree import ElementTree
from util import PrintErr,getKeys
from bs4 import BeautifulSoup
class Spider(object):
    def __init__(self):
        pass
        # self.url=url #原始爬虫路径
    def getUrlsData(self,url):
        ''' 访问url 获取html原始文件
            转换为lxml格式
        '''
        try:
            resp= requests.get(url)
            resp.raise_for_status() #状态码不是200,异常
            resp.encoding='utf-8'
        except Exception as e:
            PrintErr(e)
            return
        return resp
    def PassHTMLData(self,resp):
        '''解析内容,返回原始新闻列表'''
        pass    

    def getArticleInfo(self,articleInfos,urlList):
        '''
        遍历新闻列表，获取新闻正文，图片
        填充完整数据
        '''
        pass
            
    def checkData(self,articleInfos,urlList):
        '''
        读取数据,检查数据完整性,分别存入list
        list[0] 缺失记录 list[1] 完整记录
        '''
        missList=[] #缺失的数据
        completeList=[]#完整数据
        for index in urlList:
            key=getKeys(index)
            data=articleInfos[key] #取出文章记录
            logNum=0
            artList=[] #记录文章数据
            for k in ['tag','link','title','time','img','content']:
                if data[k] == "":
                    logNum+=1
                artList.append(data[k])
            if logNum>0:
                #缺失
                missList.append(artList)
                continue
            completeList.append(artList)
        respList=[missList,completeList]
        return  respList            

