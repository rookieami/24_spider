#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import defind
from contextlib import closing
from store import ds
import time
import datetime

def PrintErr(*strInfo):
    '''
    打印错误信息
    '''
    print("err:", strInfo)


def PrintWarn(*strInfo):
    '''
    打印警告信息
    '''
    print("warn:", strInfo)


def PrintInfo(*strInfo):
    '''
    打印信息
    '''
    print(strInfo)


def getKeys(str):
    '''
    根据url获取字典的key值
    '''
    rindex = str.rfind("/")
    lindex = str.rfind('.htm')
    return str[rindex+1:lindex]


def joinUrl(url, format):
    '''
    拼接url地址
    url 地址
    format 前缀 http:或https:
    '''
    return format+url


def htmlToLmx(data):
    '''
    将HTML转换为指定格式内容返回
    '''
    pass


def strReplace(content, word):
    '''
    word替换为空格
    '''
    return content.replace(word, '')


def fromatContent(content="", word=""):
    '''
    格式化文本内容
    '''
     # 去除\n
    content = strReplace(content, '\n')
    # 替换style属性
    st = re.search('style="[^=]*?"', content)
    if st is not None:
        content = re.sub('style="[^=]*?"', '', content, 0)  # 替换所有的style为空格

    #替换class=
    st=re.search('class="[^=]*?"',content)
    if st is not None:
        content=re.sub('class="[^=]*?"','',content,0)

    #去除style标签
    st=re.search('<style+>(.+)</style>',content)
    if st is not None:
        content=re.sub('<style+>(.+)</style>','',content,0)
        
    # 去除 span标签
    st = re.search('<span\s*[^>]*>', content)
    if st is not None:
        content = re.sub('<span\s*[^>]*>', '', content, 0)
        content = re.sub('</span>', '', content, 0)

    # 去除img标签
    st = re.search('<img.*?(?:>|\/>)', content)
    if st is not None:
        content = re.sub('<img.*?(?:>|\/>)', '', content, 0)

    #过滤iframe标签
    st = re.search('<iframe[\s\S]+</iframe *>', content)
    if st is not None:
        content = re.sub('<iframe[\s\S]+</iframe *>', '', content, 0)
    #过滤input
    st=re.search('<input[\s\S]+</input *>',content)
    if st is not None:
        content = re.sub('<input[\s\S]+</input *>', '', content, 0)
    #过滤frameset
    st=re.search('<frameset[\s\S]+</frameset *>',content)
    if st is not None:
        content = re.sub('<frameset[\s\S]+</frameset *>', '', content, 0)
    # 去除链接,仅保留内容
    st = re.search('<a[^>]+>(.+)</a>', content)  # 正文去除<a></a>标签,内含超链接\
    if st is not None:
        content = re.sub('<a[^>]*>','', content, 0)
        content = re.sub('</a>', '', content, 0)
        # content=re.sub('<a[^>]+>(.+)</a>','',content,0)

    # 去除所有空格
    # content = content.replace(" ", "")
    # 去除空的<p><\P>
    content = re.sub(
        '<p[^>]*>(\s|&nbsp;|</?\s?br\s?/?>)*</?p>', '', content, 0)
    # 过滤注释
    content = re.sub('<!--[^>]*-->', '', content, 0)
    #去除空的div
    content=strReplace(content,'<div ></div>')
    # 敏感词替换为空格
    content = strReplace(content, word)
    content = strReplace(content, '视频代码结束')
    return content

# 将数据整合成insert update sql语句
# insert_key_list 要插入得key数组
# update_key_list 要更新得key数组
# except_list insert_key_list 和 update_key_list 的差别key数组
# is_many  是否是  execute many 插入
# return string
# update by bobo 2020-05-29


def mixInsertUpdateSql(insert_key_list, update_key_list, except_list, table_name, is_many=False):
    update_sql = ''
    insert_sql = ' ('
    insert_values_sql = ' ('
    insert_index = 0
    update_index = 0
    for key in insert_key_list:
        if insert_index > 0:
            insert_sql += ','
            insert_values_sql += ','
        insert_sql += ('`'+key+'`')
        insert_values_sql += '%s'
        insert_index += 1
        if key in except_list:
            continue
        if update_index > 0:
            update_sql += ','
        update_index += 1

        if is_many == True:
            # 这里必须拼 `` 防止关键字.太坑了 2020-07-03
            update_sql += ('`'+key+'`'+'=values(`'+key+'`)')
        else:
            update_sql += ('`'+key+'`'+'=%s')

    insert_sql += ') '
    insert_values_sql += ') '
    sql = 'INSERT INTO `' + table_name + '`' + insert_sql + ' VALUES ' + \
        insert_values_sql + ' ON DUPLICATE KEY UPDATE ' + update_sql
    return sql


def getTableName(dataType):
    tableName = 'article_origin'
    if dataType == defind.MISSDATA:
        tableName = 'article_origin_broken'
    elif dataType == defind.FORMATDATA:
        tableName = 'article_remake'
    return tableName


def getFromName(catchFrom):
    '''
    根据来源码获取平台名称
    '''
    fromName = 'zhibo8'
    if catchFrom == defind.FROMQQ:
        fromName = 'QQ'
    return fromName


def timeToStamp(date):
    '''
    %Y-%m-%d %H:%M:%S格式转换时间戳
    '''
    return time.mktime(time.strptime(date, "%Y-%m-%d %H:%M:%S"))


def getEndTime():
    respTime = 0
    sqlone = "select origin_publish_at from article_origin ORDER BY origin_publish_at desc LIMIT 1 "
    with closing(ds.get_connection()) as conn, closing(conn.cursor()) as cur:
        cur.execute(sqlone)
        endTime = cur.fetchone()
    sqlTwo = "select origin_publish_at from article_origin_broken ORDER BY origin_publish_at desc LIMIT 1 "
    with closing(ds.get_connection()) as conn, closing(conn.cursor()) as cur:
        cur.execute(sqlTwo)
        brokenEndTime = cur.fetchone()
    if endTime is not None and brokenEndTime is not None:
        if endTime[0] > brokenEndTime[0]:
            respTime = endTime[0]
            return time.mktime(respTime.timetuple())
        respTime = brokenEndTime[0]

    if respTime==0:
        return 0
    return time.mktime(respTime.timetuple())

 