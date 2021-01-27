from cla_object import  zhibo8



def run(url):
    zb=zhibo8.ZbClass(url)
    doc=zb.getUrlsData()
    dataList=zb.getPassData(doc)