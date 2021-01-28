
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
    format 前缀
    '''
    return format+url

def htmlToLmx(data):
    '''
    将HTML转换为指定格式内容返回
    '''
    pass 