from class_obj.zhibo import zhibo8
import defind
def run(url):
    print("zhibo8")
    zb=zhibo8.ZbClass(defind.FROMZHIBO8)
    doc=zb.getUrlsData(url) #获取HTML
    dataList=zb.PassHTMLData(doc) #获取新闻列表
    #访问新闻url,获取正文图片
    articleDict=zb.getArticleInfo(dataList[0],dataList[1]) #所有新闻的数据
    #检查新闻内容是否缺失
    urlList=dataList[1]
    articles=zb.checkData(articleDict,urlList)
    word='直播吧' #过滤词汇
    missArticle=zb.formatArticle(articles[0],word)
    intactArticle=zb.formatArticle(articles[1],word)
    #存储数据
    zb.storageData(missArticle,defind.MISSDATA)
    zb.storageData(intactArticle,defind.INTACTDATA)
    
    return