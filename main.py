from class_obj.zhibo import zhibo8
import requests
import requests
from util import PrintErr
from bs4 import BeautifulSoup
from news.basketball import zb_basketball
import defind
import time

url='https://news.zhibo8.cc/zuqiu/more.htm'
def main():
    
    zb_basketball.run(url,defind.ZUQIU)
if __name__=='__main__':
    main()