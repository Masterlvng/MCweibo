from spider import Spider
import os
FILE = ['activity','teaching','learning','student']
BASE_URL = 'http://math.sysu.edu.cn'

def post(poster=None):
    spider = Spider(BASE_URL)
    all_news = spider.work()
    for i,file in enumerate(FILE):
        if os.path.exists(file):
            url = None
            with open(file,'r+') as f:
                url = f.readline()
            ToPost = []
            for news in all_news[i]:
                if news[1] != url:
                    ToPost.append(news)
                else:
                    break
            #poster.post(ToPost)
            with open(file,'w+') as f:
                f.write(ToPost[-1][0])

        else:
            #poster.post(all_news[i])
            with open(file,'wr') as f:
                f.write(all_news[i][-1][0])

if __name__ =="__main__":
    post()

