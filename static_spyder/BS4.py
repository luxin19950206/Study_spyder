# -*- coding:utf-8 -*-
"""
@author: luxin
@usage:极客学院关于beautifulsoup4的讲解
"""
from bs4 import BeautifulSoup
import requests
import re

source = """
<html>
  <head>
    <title>测试</title>
  </head>
  <body>
    <div class="useful">
      <ul>
        <li class="info">我需要的信息1</li>
        <li class="test">我需要的信息2</li>
        <li class="iamstrange">我需要的信息3</li>
      </ul>
     </div>
     <div class="useless">
       <ul>
         <li class="info">垃圾1</li>
         <li class="info">垃圾2</li>
       </ul>
     </div>
  </body>
</html>"""

soup = BeautifulSoup(source, 'html.parser')

useful = soup.find_all('class="useful"')
print(useful)
exit()
all_content = useful.find_all('li')
for i in all_content:

    print(i.text)

"""


"""
