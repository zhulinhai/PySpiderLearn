
# Beautifil Soup库的安装小测

### 演示HTML页面地址：https://python123.io/ws/demo.html

```
<html><head><title>This is a python demo page</title></head>
<body>
<p class="title"><b>The demo python introduces several python courses.</b></p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and <a href="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.</p>
</body></html>
```

### 
```
>>> import requests
>>> r = requests.get("https://python123.io/ws/demo.html")
>>> r.text

'<html><head><title>This is a python demo page</title></head>\r\n<body>\r\n<p class="title"><b>The demo python introduces several python cours
es.</b></p>\r\n<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional 
by tracking the following courses:\r\n<a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and <a hre
f="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.</p>\r\n</body></html>'

>>> demo = r.text
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(demo, "html.parser")
>>> print(soup.prettify())

```

# Beautiful Soup库入门

### bs4库的基本元素
Tag Name  Attributes  NavigableString Comment

### bs4库的遍历功能
.contents     .parent   .next_sibling
.children     .parents  .previous_sibling
.descendants            .next_siblings
                        .previous_siblings

# 信息的标记

标记后的信息可形成信息组织结构，增加了信息纬度
标记后的信息可用于通信、存储或展示
标记后的结构与信息一样具有重要价值
标记后的信息有利于程序理解和运用

# 信息标记的三种形式

XML

JSON

YAML

# 信息提取的一般方法

### 方法一：完整解析信息的标记形式，再提取关键信息
XML JSON YAML

需要标记解析器 例如：bs4库的标签树遍历
优点：信息解析准确
缺点：提取过程繁琐，速度慢

### 方法二：无视标记形式，直接搜索关键信息
搜索

对信息的文本查找函数即可
优点：提取过程简洁，速度较快
缺点：提取结果准确性与信息内容相关

### 融合方法

融合方法：结合形式解析与搜索方法，提取关键信息。

XML JSON YAML 搜索
需要标记解析器及文本查找函数

实例

提取HTML中所有URL
思路： 1）搜索到所有<a>标签
      2）解析<a>标签格式，提取href后的链接内容。


<>.find_all(name, attrs, recursive, string, **kwargs)
返回一个列表类型，存储查找的结果

name: 对标签名称的解锁字符串


# 正则表达式

```
import re

soup.find_all(id=re.compile('link'))
```