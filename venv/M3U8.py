import os
import requests
import re
def download(url):
    baseDir = "down/10"
    r = requests.get(url)
    with open(baseDir+".mp4", "ab+") as tsf:
         tsf.write(r.content)
def parseUrlContent(file,counter,head):
    if len(file.text)>0:
        res = re.findall(".*?\.ts",file.text)
        mlist=[]
        for line in res:
            mlist.append(head+line)
        for line in mlist:
            counter = counter + 1
            download(line)
            print("downloading file ("+str(counter+1)+"/"+str(len(mlist))+")")
        print("下载完成！")
url = "https://youku.cdn2-okzy.com/20200130/7452_f33dce52/index.m3u8"
url1="http://cn7.qxreader.com/hls/20200130/0e4ebab6b8156d7f2e6408598ee3428a/1580396818/index.m3u8"
url2="http://cn7.qxreader.com/hls/20200131/61dd5801c4991eab7f953d9bb3b6b572/1580456347/index.m3u8"
head = "http://cn7.qxreader.com"
file = requests.get(url2)
counter = 0
parseUrlContent(file,counter,head)