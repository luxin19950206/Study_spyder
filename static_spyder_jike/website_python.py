# -*- coding:utf-8 -*-
"""
@author: luxin
@usage: 关于如何处理
"""
"""
get与post方法的使用
1 对于大多数直接在浏览器输入网址就能访问的网页，使用requests的get方法就能获取到网页的源代码：
requests.get('website').content
2 对于不能直接在浏览器中输入网址访问的页面，就需要使用requests的post方法来获取源代码。

"""
import requests
import lxml.html

# get方法
source = requests.get('http://www.jikexueyuan.com').content
print(source.decode())

# xpath语法讲解
"""
使用xpath的流程如下
from lmxl import html
selector=html.from string('网页源代码')
info=selector.xpath('一段xpath语句')
"""
# xpath语句格式
"""
获取文本：
//标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/..../text()
获取属性值：
//标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/..../@属性n
"""

source = """
<html>
  <head>
    <title>测试</title>
  </head>
  <body>
    <div class="useful">
      <ul>
        <li class="info">我需要的信息1</li>
        <li class="info">我需要的信息2</li>
        <li class="info">我需要的信息3</li>
      </ul>
     </div>
     <div class="useless">
       <ul>
         <li class="info">垃圾1</li>
         <li class="info">垃圾2</li>
       </ul>
     </div>
  </body>
</html>
"""
selector = lxml.html.fromstring(source)
info = selector.xpath('//div[@class="useful"]/ul/li/text()')
