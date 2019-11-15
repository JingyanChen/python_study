import requests

def get_html(URL):
    try:
        r = requests.get(URL)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"

def get_html_header(URL):
    try:
        r = requests.head(URL)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.headers
    except:
        return "error"

if __name__ == "__main__":
    print(get_html_header("http://www.baidu.com"))
