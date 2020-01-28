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
        mlist=[]
        for line in res:
            mlist.append(head[0]+line)
        # print(mlist)
        for line in mlist:
            counter = counter + 1
            download(line,counter)
            print("downloading file ("+str(counter+1)+"/"+str(len(mlist))+")")
url = "https://m3u8.cnkamax.com/useruploadfiles/e189b564e09b5b62a660234ce395d957.m3u8"
nurl = url.replace("https://m3u8","https://p")
head = re.split("\w+\.m3u8",nurl)
file = requests.get(nurl)
counter = 0
if file.status_code == 200:
    parseUrlContent(file,counter,head)
else:
    file = requests.get(url)
    parseUrlContent(file,counter,head)