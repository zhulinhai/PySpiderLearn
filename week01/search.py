# 搜索引擎关键词提交接口
# 百度的关键词接口: http://www.baidu.com/s?wd=keyword

import requests

keyword = "Python"
try:
    kv = {'wd': keyword}
    r = requests.get("http://www.baidu.com/s", params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")

