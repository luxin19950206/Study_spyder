# -*- coding:utf-8 -*-
"""
@author: luxin
@usage:
"""
from selenium import webdriver

"""访问页面"""
browser = webdriver.Chrome()  # 声明浏览器
url = 'https://www.baidu.com/'
browser.get(url)  # 打开浏览器预设地址
# print(browser.page_source)  # 打印网页源代码
browser.close()  # 关闭网页

"""查找元素"""
element = browser.find_element_by_id("passwd-id")  # 如果有多个符合条件的，返回第一个
element = browser.find_element_by_name("passwd")  # 如果有多个符合条件的，返回第一个
element_list = browser.find_elements_by_id("passwd-id")  # 以列表形式返回所有的符合条件的element
element_list = browser.find_elements_by_name("passwd")  # 以列表形式返回所有的符合条件的element
element = browser.find_element_by_xpath("//input[@id='passwd-id']")  # 如果有多个符合条件的，返回第一个
element = browser.find_element_by_xpath("//input[@id='passwd-id']")  # 以列表形式返回所有的符合条件的element
