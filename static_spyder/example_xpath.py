import lxml.html

html = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>测试-常规用法</title>
</head>
<body>
<div id="content">
    <ul id="useful">
        <li class="thisiswhatIwant">这是第一条信息</li>
        <li class="thisiswhatIwant">这是第二条信息</li>
        <li>这是第三条信息</li>
    </ul>
    <ul id="useless">
        <li>不需要的信息1</li>
        <li>不需要的信息2</li>
        <li>不需要的信息3</li>
    </ul>

    <div id="url">
        <a href="http://jikexueyuan.com">极客学院</a>
        <a href="http://jikexueyuan.com/course/" title="极客学院课程库">点我打开课程库</a>
    </div>
</div>

</body>
</html>
'''

selector = lxml.html.fromstring(html)

# 提取文本
# content_0 = selector.xpath('//ul[@id="useful"]')[0]
# content = content_0.xpath('li/text()')
# content = selector.xpath('//ul[@id="useful"]/li/text()')
# content = selector.xpath('//li[@class="thisiswhatIwant"]/text()')
# content = selector.xpath('/html/body/div/ul[@id="useful"]/li[@class="thisiswhatIwant"]/text()')
# print(content)
# for each in content:
#     print(each)

# 提取属性
# link = selector.xpath('//div[@id="url"]/a/@href')
# for each in link:
#     print(each)
#
title = selector.xpath('//a/@title')
print(title[0])
