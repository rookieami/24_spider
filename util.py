import re
import defind

def PrintErr(*strInfo):
    '''
    打印错误信息
    '''
    print("err:", strInfo )

def PrintWarn(*strInfo):
    '''
    打印警告信息
    '''
    print("warn:", strInfo )

def PrintInfo(*strInfo):
    '''
    打印信息
    '''
    print(strInfo)


def getKeys(str):
    '''
    根据url获取字典的key值
    '''
    rindex=str.rfind("/")
    lindex=str.rfind('.htm')
    return str[rindex+1:lindex]
def joinUrl(url,format):
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
def strReplace(string,word):
    '''
    word替换为空格
    '''
    return string.replace(word,'')
def fromatContent(content,word):
    '''
    格式化文本内容
    '''
    st=re.sub('<(.*?)>','',content,0)  #正文去除<a></a>标签,内含超链接\
    st=re.sub('<!--[^>]*-->','',st,0)   #过滤注释

    st=strReplace(st,word) #来源替换为空格
    return st 

# 将数据整合成insert update sql语句
# insert_key_list 要插入得key数组
# update_key_list 要更新得key数组
# except_list insert_key_list 和 update_key_list 的差别key数组
# is_many  是否是  execute many 插入
# return string
# update by bobo 2020-05-29
def mixInsertUpdateSql(insert_key_list,update_key_list,except_list,table_name,is_many=False):
    update_sql=''
    insert_sql=' ('
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
    sql = 'INSERT INTO `' + table_name + '`' + insert_sql + ' VALUES ' + insert_values_sql + ' ON DUPLICATE KEY UPDATE ' + update_sql
    return sql

def getTableName(dataType):
    tableName='article_origin'
    if dataType==defind.MISSDATA:
        tableName='article_origin_broken'
    elif dataType==defind.FORMATDATA:
        tableName='article_remake'
    return tableName

def getFromName(catchFrom):
    '''
    根据来源码获取平台名称
    '''
    fromName='zhibo8'
    if catchFrom==defind.FROMQQ:
        fromName='QQ'
    return fromName