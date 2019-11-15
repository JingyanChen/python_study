import requests
import re

def get_html_text(url):
    try:
        headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        r = requests.get(url,timeout = 30,headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
        

def parsePage(ilt , html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*"',html)
        tlt = re.findall(r'\"raw_title\':\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print("error")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods = '中老年服饰'
    depth = 2
    start_url = "https://search.jd.com/Search?keyword=" + goods

    infoList = [] 

    for i in range(depth):
        try:
            url = start_url + "&s=" + str(44 * i)
            html = get_html_text(url)
            parsePage(infoList,html)
        except:
            continue

    printGoodsList(infoList)

if __name__ == "__main__":
    main()



