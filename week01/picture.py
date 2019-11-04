#网络图片的爬取和存储

import requests
import os

#url = "https://www.nationalgeographic.com/content/dam/magazine/rights-exempt/2019/12/departments/explore/through-the-lens-bear.adapt.1900.1.jpg"
url = "https://media3.giphy.com/media/UQOJnmhiTgB4qb6mvQ/200w.webp"
root = "D://pics//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        print(r.status_code)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")