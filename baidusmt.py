import requests

def research_by_baidu(keyword):
    kv = {'wd':keyword}
    try:
        r = requests.request('GET',"http://www.baidu.com/s",params = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(len(r.text))
    except:
        print('error')


if __name__ == "__main__":
    research_by_baidu('python')

