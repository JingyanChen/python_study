import requests
url = "http://m.ip138.com/ip.asp?ip="
ip = '117.62.180.83'

try:
    r = requests.get(url + ip)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('get error')
