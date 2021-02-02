#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from xml.etree import ElementTree
from util import *
from bs4 import BeautifulSoup

from contextlib import closing
from store import ds,req_url
import json

class Spider(object):
    def __init__(self,catchFrom):
        self.catchFrom=catchFrom

    def getUrlsData(self,url):
        ''' 访问url 获取html原始文件
            转换为lxml格式
        '''
        try:
            headers={
                'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            resp= requests.get(url,headers=headers,timeout=5)
            resp.raise_for_status() #状态码不是200,异常
            resp.encoding='utf-8'
        except Exception as e:
            print("解析新闻首页出错")
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
                fromtWord=fromatContent(str(article[5]),word)    
                article[5]=fromtWord    
        return articleList

    def storageData(self,dataList,dataType):
        '''
        原始数据入库
        dataList 数据列表
        dataType 数据类型 0:完整 1缺失
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
        ]
        # except_list=['create_at']
        insert_key_list=update_key_list # +except_list
        sql=mixInsertUpdateSql(insert_key_list,update_key_list,[],tableName,True)

        respList=[] #记录入库数据
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
                )
                #查询是否有这条数据
                querySql="select id from %s where origin_url='%s'" %(tableName,data[1])
                with closing(ds.get_connection()) as conn, closing(conn.cursor()) as cur:
                    cur.execute(querySql)
                    id=cur.fetchone()
                if id is not None and id[0] >0:
                    print("新闻已经存在,id:%s" % (id[0]))
                    continue #存在该记录,跳出
                #入库
                with closing(ds.get_connection()) as conn, closing(conn.cursor()) as cur:

                    # print(insert_tup)
                    cur.execute(sql, insert_tup)
                    id=int(cur.lastrowid)
                    respList.append((id,)+insert_tup)
                    conn.commit()
            except Exception as e:
                print("存储错误")
                PrintErr(e)
                continue
        return respList
    def request_Wash_article(self,dataList):
        '''
        文章洗稿
        datalist 传入的数据列表
        '''
        url="http://"+req_url
        fromName=getFromName(self.catchFrom)
        for data in dataList:
            try:

                data={
                    "saved_id":data[0],"catch_from":self.catchFrom,
                    "origin_url":data[2],"title":data[3],
                    "origin_author":fromName,"content":data[7],
                    "img_url":data[5],"all_tags":data[6],
                    "origin_publish_at":data[8],
                }

                resp=requests.post(url=url,data=data)
                jsonstr=json.loads(resp.text)
                if jsonstr["code"]!=0:
                    PrintWarn("数据未正常进行处理,line: 160,id:%s"% data[0])
            except Exception as e:
                PrintErr(e)
                PrintErr("洗稿操作出现异常,请处理")
                continue
        


