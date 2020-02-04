import re
import csv

with open('source.html', 'r', encoding='UTF-8') as f:
    source = f.read()

# 首先获得包含每一层楼所有信息的大文本块
every_reply = re.findall('l_post l_post_bright j_l_post clearfix  "(.*?)p_props_tail props_appraise_wrap', source, re.S)
resultList = []
# 从每一个大文本块里面提取出各个楼层的发帖人姓名,发帖内容和发帖时间
for each in every_reply:
    result = {}
    result['username'] = re.findall('username="(.*?)"', each, re.S)[0]
    result['content'] = re.findall('j_d_post_content ">(.*?)<', each, re.S)[0].replace('            ', '')
    result['reply_time'] = re.findall('class="tail-info">(2016.*?)<', each, re.S)[0]
    resultList.append(result)

with open('../../../Downloads/8372201e-df59-4028-b6f1-fad24f907887/result.csv', 'w', encoding='UTF-8') as f:
    writer = csv.DictWriter(f, fieldnames=['username', 'content', 'reply_time'])
    writer.writeheader()
    writer.writerows(resultList)
