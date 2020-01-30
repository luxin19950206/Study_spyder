# -*- coding: utf-8 -*-
"""
@author：日行小逻辑19950206
@usage：静态爬虫中正则表达式学习

"""
import re

"""
Basic symbol
"""
"""
.号
点号可以代表除了\n(换行符)以外的字符
一个点号代表一个字符
jikexueyuan==ji.......an，有多少个字母就代表着需要打多少个点号
点号就是一个占位符
"""

"""
星号* 代表它前面的子表达式0次到多次
jikexueyuan==j.*yuan 代表多个点号
jikexueyuan==jike.*an 
jikeeeeeeee==jike*
jike==jikex* 这里的*号代表0个x
"""

"""
?号代表前面的子表达式0次或者1次
jikexueyuan==jikexu.?yuan
jikexueyuan==jikew?xueyuan
"""

"""
转义字符\
\不能单独使用
让有特殊意义的字符变成普通的字符:"\*"代表普通的星号
让普通的字符变成特殊的字符："\d代表数字"
"""

"""
实际应用
括号()的使用
"""
sentence_1 = 'jikexueyuan'
sentence_2 = '我的密码是123456678，你的密码是112312312，他的密码是sadfwerasdf，请牢记'
sentence_3 = '我是kingname, 我的微博账号是:kingname, 密码是:12345678, QQ账号是:99999, 密码是:890abcd, 银行卡账号是:000001, 密码是:654321, Github账号是:99999@qq.com, 密码是:7777love8888, 请记住他们。'

result_1 = re.findall('jike...yuan', sentence_1)
# 这样提取了全部的内容即['jikexueyuan']
result_11 = re.findall('jike(...)yuan', sentence_1)
# 加了括号仅提取了括号中的内容['xue']
"""
提取数字
\d用来表示一位数字，\d+代表一个或多个数字
"""
result_2 = re.findall('(\d+)', sentence_2)

"""
提取文本、多行文本
.*外号贪心算法，获取最长的满足条件的字符串
.*?外号非贪心算法，获取最短的能满足条件的字符串
"""
result_111 = re.findall('密码是(.*)，', sentence_2)
# .* 代表多个点号，同来匹配一串任意长度的字符串，前后需要其他符号来限定长度
result_1111 = re.findall('密码是(.*?)，', sentence_2)
# .*? 匹配一个能满足要求的最短字符串，前后需要其他符号来限定长度，比如这个里面的，
user_password = re.findall('账号是:.*?, 密码是:.*?,', sentence_3)
# ['账号是:kingname, 密码是:12345678,', '账号是:99999, 密码是:890abcd,', '账号是:000001, 密码是:654321,', '账号是:99999@qq.com, 密码是:7777love8888,']
result_3 = re.findall('账号是:(.*?), 密码是:(.*?),', sentence_3)
# [('kingname', '12345678'), ('99999', '890abcd'), ('000001', '654321'), ('99999@qq.com', '7777love8888')]
# 上方的账号和密码之间需要空格
"""
re.findall(pattern,string,flags=0)
Python的正则表达式以列表的形式返回所有满足要求的字符串
"""

"""
re.search(pattern,string,flags=0)
search方法可以返回第一个满足要求的字符串，一旦找到要求的内容就会停止查找
"""
result_4 = re.search('账号是:(.*?), 密码是:(.*?),', sentence_3)
# print(result_4)
# <re.Match object; span=(16, 43), match='账号是:kingname, 密码是:12345678,'>
# print(result_4.group())
# 账号是:kingname, 密码是:12345678,
# print(result_4.group(1))
# kingname
# print(result_4.group(2))
# 12345678

"""
正则表达式提取技巧：
1先处理大后处理小
"""
example_text = """
有效用户：
姓名：张三
姓名：里斯
姓名：里斯
无效用户：
姓名：某某
姓名：某人
"""
user = re.findall('有效用户：(.*?)无效用户', example_text, re.S)
# ['\n姓名：张三\n姓名：里斯\n姓名：里斯\n']
user_useful = re.findall('姓名：(.*?)\n', user[0])
# ['张三', '里斯', '里斯']
