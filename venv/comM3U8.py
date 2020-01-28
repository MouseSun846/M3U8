import os
import requests
import re


def download(url,counter):
    baseDir = "down/"
    r = requests.get(url)
    with open(baseDir+str(counter)+".ts", "wb") as tsf:
         tsf.write(r.content)
def parseUrlContent(file,counter,head):
    if len(file.text)>0:
        res = re.findall(".*?\.ts",file.text)
        print(res)
        mlist=[]
        for line in res:
            mlist.append(head+line)
        # print(mlist)
        for line in mlist:
            counter = counter + 1
            download(line,counter)
            print("downloading file ("+str(counter+1)+"/"+str(len(mlist))+")")
url = "http://db.qingk.cn:80/vod/online/hqsjt/c6ccd309dc86959be4280c7fe919f315.mp4/chunklist.m3u8"
head = "http://db.qingk.cn:80/vod/online/hqsjt/c6ccd309dc86959be4280c7fe919f315.mp4/"
file = requests.get(url)
counter = 0
parseUrlContent(file,counter,head)
