from cla_object import zhibo8
import requests
import requests
from util import PrintErr
from bs4 import BeautifulSoup
from news.basketball import zb_basketball


url='https://news.zhibo8.cc/zuqiu/more.htm'
def main():
    zb_basketball.run(url)
if __name__=='__main__':
    main()