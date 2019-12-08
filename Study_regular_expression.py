# -*- coding: utf-8 -*-
"""
@author：日行小逻辑19950206
@usage：正则表达式学习

"""
import re

"""
Basic symbol
"""
"""
.号
点号可以代表除了\n以外的字符
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
如何从提取数字
\d用来表示一位数字
\d+代表一个或多个数字
提取文本、多行文本
"""
sentence_1 = 'jikexueyuan'
sentence_2 = '我的密码是123456678，你的密码是112312312'
sentence_3 = '我是kingname，我的微博密码是1223131'
result_1 = re.findall('jike...yuan', sentence_1)
# 这样提取了全部的内容即['jikexueyuan']
result_11 = re.findall('jike(...)yuan', sentence_1)
# 加了括号仅提取了括号中的内容['xue']
print(result_1, result_11)

result_2 = re.findall('(\d+)', sentence_2)
print(result_2)
