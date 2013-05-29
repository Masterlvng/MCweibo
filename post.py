# -*- coding: utf-8 -*-
from spider import Spider
from weiborobot import *
import os
import logging
#four file are used to indicate news that last time posted
FILE = ['activity','teaching','learning','student']
BASE_URL = 'http://math.sysu.edu.cn'
COLUMNS = [u'学院动态',u'教学经纬',u'学术资讯',u'学生园地']

def post(poster=None):
    spider = Spider(BASE_URL)
    all_news = spider.work()

    for i,file in enumerate(FILE):
        if os.path.exists(file):
            url = None
            with open(file) as f:
                url = f.read()
            ToPost = []
            for news in all_news[i]:
                if news[0] != url:
                    ToPost.append(news)
                else:
                    break

            if len(ToPost) != 0:
                poster.post(ToPost,i)
                with open(file,'w+') as f:
                    f.write(ToPost[0][0])
        else:
            poster.post(all_news[i],i)
            with open(file,'w+') as f:
                f.write(all_news[i][0][0]+'\n')

if __name__ =="__main__":
    FORMAT = '%(asctime)-15s %(where)-8s %(message)s'
    logging.basicConfig(filename='MCNews.log')
    robot = weiborobot()
    post(robot)

