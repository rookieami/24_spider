from class_obj.zhibo import zhibo8

def run(url):
    print("zhibo8")
    zb=zhibo8.ZbClass()
    doc=zb.getUrlsData(url) #获取HTML
    dataList=zb.PassHTMLData(doc) #获取新闻列表
    #访问新闻url,获取正文图片
    articleDict=zb.getArticleInfo(dataList[0],dataList[1]) #所有新闻的数据
    #检查新闻内容是否缺失
    urlList=dataList[1]
    articles=zb.checkData(articleDict,urlList)
    print(articles[0])