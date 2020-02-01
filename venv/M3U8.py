import os
import requests
import re
import json
from urllib.parse import unquote
def download(url):
    baseDir = "down/下一站是幸福12"
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
# 获取视频key值
def getKey(parseUrl,videoUrl):
    res = requests.get(parseUrl+videoUrl)
    key = re.findall("key:\s\"(.*?)\"",res.text)
    return key[0]
# 获取data
def getData(key,videoUrl):
    # 格式化url
    res = re.findall(".*?\.html",videoUrl)
    req = requests.post("http://yun.mt2t.com/lines/getdata",
                  {'url': res[0], 'type': '', 'name': '', 'episode': '0','key': key})
    jreq = req.json()
    pUrl = jreq[0]['Url']
    encurls = pUrl.split('=')
    return encurls[-1]
# 获取m3u8
def getM3U8(udata):
    udata = unquote(udata,'utf-8')
    res = requests.post("http://y6.mt2t.com/ifr/api",
                        data={'url':udata,'type':'','from':'mt2t.com','device':'','up':'0'},
                        cookies={'UM_distinctid':'16ffb68230d6e-043cd0f275d51a-36664c08-100200-16ffb6823101c8',
                                'weParser_youku_cna':'FhRPFjp3ggUCAXAKgnN1DtXN','top':'true',
                                'CNZZDATA1274094140':'1586191632-1580468275-null|1580522704'},
                        headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
                        })
    req = res.json()
    return req['url']
url = "https://youku.cdn2-okzy.com/20200130/7452_f33dce52/index.m3u8"
url1="http://cn7.qxreader.com/hls/20200130/0e4ebab6b8156d7f2e6408598ee3428a/1580396818/index.m3u8"
url2="http://cn7.qxreader.com/hls/20200131/61dd5801c4991eab7f953d9bb3b6b572/1580456347/index.m3u8"
url3="http://cn6.qxreader.com/hls/20200131/4dea35ce61963392f18329287abd9e7d/1580480574/index.m3u8"
url4="http://cn6.qxreader.com/hls/20200131/d1d637a15c48c5d0b240cba383f00e16/1580480258/index.m3u8"
head = "http://cn7.qxreader.com"
# 解析地址
mparseUrl = "http://yun.mt2t.com/yun?url="
# VIP视频地址
videoUrl = "https://www.mgtv.com/b/328837/7488432.html?fpa=prc"

key = getKey(mparseUrl,videoUrl=videoUrl)
udata = getData(key,videoUrl)
m3u8 = getM3U8(udata)
file = requests.get(m3u8)
counter = 0
parseUrlContent(file,counter,head)
