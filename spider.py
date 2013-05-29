import requests as rq
import re
BASE_URL = 'http://math.sysu.edu.cn'

class NewsElement:
    def __init__(self,type,bref,url):
        self.type = type
        self.bref = bref
        self.url = url
    @property
    def type(self):
        return self.type
    @property
    def url(self):
        return self.url
    @property
    def bref(self):
        return self.bref


class Spider:
    def __init__(self,url):
        self.url = url

    def work(self):
        reg_Column = re.compile('<table width="100%" cellpadding="3">(.*?)</table>')
        reg_News = re.compile('<a.*?href="(.*?)"\s+target="_blank"\stitle=(.*?)>.*?</a>')
        r = rq.get(self.url)
        Column = reg_Column.findall(r.text)
        rst = []
        for col in Column:
            rst.append(reg_News.findall(col))
        return rst

if __name__ == '__main__':
    spider = Spider(BASE_URL)
    rst = spider.work()



