from cla_object import  zhibo8



def run(url):
    zb=zhibo8.ZbClass()
    doc=zb.getPassData(url)
    print(doc)