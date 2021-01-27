
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
    获取字典的key值
    '''
    rindex=str.rfind("/")
    lindex=str.rfind('.htm')
    return str[index+1:ind]

