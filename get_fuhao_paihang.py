import requests
import bs4

def main():
    url = "https://web.phb123.com/renwu/fuhao/px_CN.html"
    fuhaoList = []
    
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
    except:
        print("get html error!")
        return ""

    #print("start soup\r\n")   
    
    soup =  bs4.BeautifulSoup(html,"html.parser") 

    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            try:
                fuhaoList.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string,tds[4].string])
            except:
                pass

    #print("get len = %d" % len(fuhaoList))


    print("为你爬取到了 %d 个超级富豪" % len(fuhaoList))



    print("{0:^10}{1:^10}{2:^10}{3:^30}{4:^20}".format("中国排名","世界排名","人名","财富值","财富来源",chr(12288)))
    
    for i in range(400):
        u=fuhaoList[i]
        try:
            print("{0:^10}{1:^15}{2:^15}{3:^20}{4:^20}".format(u[0],u[1] ,u[2],u[3],u[4],chr(12288)))
        except:
            pass
            

if __name__ == "__main__":
    main()
