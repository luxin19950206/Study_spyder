# -*- coding:utf-8 -*-
"""
@author: luxin
@usage:极客学院Mongodb相关讲解

"""
from mongoengine import *

# 1 初始化链接
connect('jikexueyuan')


# connect('数据库名称')
# 如果mongodb不是运行在本地电脑上面，就需要制定ip地址和端口
# connect('数据库名称',host='192.168.2.12',,port)

# 2 定义文档
# 定义一个类，类名对应了mongodb中的集合名，类中的每个变量对应了每条记录中的列名
class People(Document):
    name = StringField(required=True)
    # 所有写了required=True在初始化的时候都是必填的参数项
    age = IntField(required=True)
    sex = StringField(required=True)
    salary = IntField()
    # 这里的IntField或者StringField对应类数据类型

# 3 创建对象
# 初始化类
mei = People(name='mei', age=24, sex='female', salary=4000)
mei.save()
# 如果想要修改信息
mei.age=22
mei.save()

# 4 读取对象
for each in People.objects:
    print(each.name)
    print(each.age)

# 按照条件搜索
for each in People.objects(age=22):
    print(each.name)

# 5 删除记录
# 如果你想删除记录，那就先把记录找出来，然后调用delete()方法
kingname_list=People.objects(name='nei')
for kingname in kingname_list:
    kingname.delete()