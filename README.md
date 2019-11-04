### [在线课程地址](https://www.icourse163.org/learn/BIT-1001870001?tid=1206951268#/learn/content?type=detail&id=1211970245&cid=1215042937&replay=true)
# Python网络爬虫与信息提取

## 安装Requests库

```
pip install requests
```

请求百度网页内容
```
>>> import requests
>>> r = requests.get('http://www.baidu.com')
>>> r.status_code
200
>>> r.encoding = 'utf-8'
>>> r.text

>>> r.encoding
'ISO-8859-1'
>>> r.apparent_encoding
```
爬取网页的通用代码框架


## 安装 beautifulsoup4

```
pip install beautifulsoup4
```

## Mac 设置默认Python版本

1. 首先打开终端
```
open ~/.bash_profile
```
