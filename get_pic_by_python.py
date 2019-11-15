import requests
import os

url = "https://cdn.pixabay.com/photo/2016/06/06/21/53/child-1440526_960_720.jpg"
root = "D://PIC_FORM_PYTHON//"
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("file save success!\r\n")
    else:
        print("file has exist")
except:
    print("get error")
