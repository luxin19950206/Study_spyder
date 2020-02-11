import json

"""
解析:json.loads(json格式字符串)
生成:json.dumps(Python字典)

"""

# 字典->json格式字符串
person_dict = {'basic_info':
                   {'name': 'kingname',
                    'age': 24,
                    'sex': 'male'},
               'work_info':
                   {'salary': 99999,
                    'position': 'engineer',
                    'department': 'spider'}
               }

person_json = json.dumps(person_dict, indent=4)
print(person_json)
print(type(person_json))
# str


# json格式字符串->字典
data_json = '{"data": {"head": "我是头", "body": "我是身体"}, "status": "true"}'
data_dict = json.loads(data_json)
print(data_dict)
print(type(data_dict))
print(data_dict['data']['body'])

