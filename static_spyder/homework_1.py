# -*- coding:utf-8 -*-
"""
@author: luxin
@usage:极客学院静态爬虫项目中爬去百度贴吧半自动化项目
"""
import re
import csv

with open('source.html', 'r', encoding='UTF-8') as f:
    source = f.read()

every_reply=re.findall('')