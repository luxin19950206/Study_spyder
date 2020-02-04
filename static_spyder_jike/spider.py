# -*-coding:utf8-*-

import requests
import lxml.html
import csv

doubanUrl = 'https://movie.douban.com/top250?start={}&filter='


def getSource(url):
    '''
    获取网页源代码。
    :param url:
    :return: String
    '''
    head = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.108 Safari/537.36'}
    content = requests.get(url, headers=head)
    content.encoding = 'utf-8'  # 强制修改编码,防止Windows下出现乱码
    return content.content


def getEveryItem(source):
    '''
    获取每一个电影的相关信息。movie_dict字典用于保存电影的信息。
    :param source:
    :return: [movie1_dict, movie2_dict, movie3_dict,...]
    '''
    selector = lxml.html.document_fromstring(source)
    movieItemList = selector.xpath('//div[@class="info"]')  # 此处使用到了先抓大再抓小的技巧
    movieList = []

    for eachMoive in movieItemList:
        movieDict = {}
        title = eachMoive.xpath('div[@class="hd"]/a/span[@class="title"]/text()')
        print(title)
        otherTitle = eachMoive.xpath('div[@class="hd"]/a/span[@class="other"]/text()')
        link = eachMoive.xpath('div[@class="hd"]/a/@href')[0]
        directorAndActor = eachMoive.xpath('div[@class="bd"]/p[@class=""]/text()')
        star = eachMoive.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')[0]
        quote = eachMoive.xpath('div[@class="bd"]/p[@class="quote"]/span/text()')
        if quote:
            quote = quote[0]
        else:
            quote = ''

        movieDict['title'] = ''.join(title + otherTitle)
        movieDict['url'] = link
        # 你可以试一试直接打印''.join(directorAndActor),看看他的格式是多么的混乱
        movieDict['directorAndActor'] = ''.join(directorAndActor).replace('                            ', '').replace(
            '\r', '').replace('\n', '')
        movieDict['star'] = star
        movieDict['quote'] = quote
        print(movieDict)
        movieList.append(movieDict)
    return movieList


def writeData(movieList):
    with open('doubanMovie_example2.csv', 'w', encoding='UTF-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'directorAndActor', 'star', 'quote', 'url'])
        writer.writeheader()
        for each in movieList:
            print(each)
            writer.writerow(each)


if __name__ == '__main__':
    movieList = []
    for i in range(10):
        pageLink = doubanUrl.format(i * 25)
        print(pageLink)
        source = getSource(pageLink)
        movieList += getEveryItem(source)
    print(movieList[:10])
    movieList = sorted(movieList, key=lambda k: k['star'], reverse=True)  # 根据字典中的key=star这一项的value来排序,倒序。
    writeData(movieList)
