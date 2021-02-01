import requests
from xml.etree import ElementTree
from util import *
from bs4 import BeautifulSoup

from contextlib import closing
from store import ds

class Spider(object):
    def __init__(self,catchFrom,newsType):
        self.catchFrom=catchFrom
        self.newsType=newsType

    def getUrlsData(self,url):
        ''' 访问url 获取html原始文件
            转换为lxml格式
        '''
        try:
            resp= requests.get(url,timeout=5)
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

    def formatArticle(self,articleList,word):
        '''
        格式化文章
        '''
        for article in articleList:
            #标题处理
            if article[2] is not None:
                article[2]=strReplace(article[2],word) #敏感词替换为空格
            #正文格式化,去掉链接,敏感词等
            if article[5] is not None:
                article[5]=fromatContent(article[5],word)        
        return articleList

    def storageData(self,dataList,dataType,newsType):
        '''
        原始数据入库
        dataList 数据列表
        dataType 数据类型 0:完整 1缺失
        newsType 新闻类型 足球,篮球,综合
        '''
        if dataList is None:
            return
        #根据类型选择数据表
        tableName=getTableName(dataType)
        fromName=getFromName(self.catchFrom)
        update_key_list=[
            'catch_from', #来源
            'origin_url', #原贴地址
            'title',  #文章标题
            'origin_display_author', #文章来源
            'img_url', #封面图地址
            'all_tags', #原文标签
            'origin_content', #原文内容
            'origin_publish_at',#原文发布时间
            'type',# 新闻类型
        ]
        # except_list=['create_at']
        insert_key_list=update_key_list # +except_list
        sql=mixInsertUpdateSql(insert_key_list,update_key_list,[],tableName,True)
        for data in dataList:
            try:
                
                # print(data)
                insert_tup=(
                    self.catchFrom,
                    data[1], #url
                    data[2], #标题
                    fromName, #来源
                    data[4], #img
                    data[0], #tag
                    data[5], #content
                    data[3],  #time
                    self.newsType,     
                )
                #查询是否有这条数据
                querySql="select id from %s where  `type`='%s' and origin_url='%s'" %(tableName,newsType,data[1])
                with closing(ds.get_connection()) as conn, closing(conn.cursor()) as cur:
                    cur.execute(querySql)
                    id=cur.fetchone()
                if id is not None and id[0] >0:
                    print("%s类型新闻已经存在,id:%s" % (newsType,id[0]))
                    continue #存在该记录,跳出
                #入库
                with closing(ds.get_connection()) as conn, closing(conn.cursor()) as cur:

                    # print(insert_tup)
                    cur.execute(sql, insert_tup)
                    conn.commit()
            except Exception as e:
                PrintErr(e)
                continue
        


