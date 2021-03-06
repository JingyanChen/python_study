# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("get html error \r\n")
        return "error"


def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])


def printfUnivList(ulist, num):
    a="{0:^10}{1:{3}^10}{2:^10}"
    print(a.format("排名","学校","地域",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(a.format(u[0],u[1],u[2],chr(12288)))

def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html"
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printfUnivList(uinfo,20)

if __name__ == "__main__":
    main()
