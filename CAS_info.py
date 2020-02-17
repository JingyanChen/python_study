import re # 不用安装（注意！！）
import os # 文件夹等的操作（注意！！）
import time 
import requests # http urllib2
from bs4 import BeautifulSoup 

url = 'http://casad.cas.cn/ysxx2017/ysmdyjj/qtysmd_124280/'
html = requests.get(url)
#print(html.status_code) # 状态码200 404 500 502
html.encoding = 'utf-8'
#print(html.text) # 以文本形式返回网页

# 提取数据
# + 一次或多次 大于等于一次
# findall返回的是列表（注意！！）
number = re.findall(
'<a href="http://casad.cas.cn/sourcedb_ad_cas/zw2/ysxx/sxwlxb/\d\d\d\d\d\d/t20\d\d\d\d\d\d_\d\d\d\d\d\d\d.html" target="_blank">', html.text)

#默认全部爬取,i是下一级网址的index
for i in range(0,len(number)):
    nextUrl = number[i]

    #number[i]储存的数据格式是
    # <a href="http://casad.cas.cn/sourcedb_ad_cas/zw2/ysxx/sxwlxb/200906/t20090626_1854608.html" target="_blank">
    # 使用re库做一个分离，获得其中的"http://casad.cas.cn/sourcedb_ad_cas/zw2/ysxx/sxwlxb/200906/t20090626_1854608.html"

    pattern = re.compile('"(http://.*.html)"') #定义一个常用正则表达式，.*代表任意内容，获取双引号内的任意内容
    linkList = pattern.findall(number[i]) # linkList[0]为下一级有效的URL

    # 再次请求数据
    nexthtml = requests.get(linkList[0])
    nexthtml.encoding = 'utf-8'

    #数据的整理使用beautifulSoup4库
    soup = BeautifulSoup(nexthtml.text,'html.parser')

    nameData = soup.title.text

    #对introduce做汉字打头的提取，避免因为html编写不规范导致的.p错误
    pattern = re.compile('[\u4e00-\u9fa5].*')# 汉字打头后面无所谓
    introduceList = pattern.findall(soup.p.text)
    introduce = introduceList[0]

    # 保存数据
    with open(r'CAS_info.txt', mode='a+', encoding="utf-8") as f: # 特别注意这里的要以编码utf-8方式打开
        f.write("序号:{index} \r\n 姓名:{name} \r\n 介绍:{ind} \r\n ".format(index=i,name=nameData,ind=introduce))

    # 不要下载太快
    # 限制下载的速度
    time.sleep(0.3)

    print("URL:{url} 姓名:{n} 爬取成功 {now}/{all}".format(url = linkList[0],n = nameData,now = i,all = len(number) ))
    # 程序运行到这个地方 暂停1s
