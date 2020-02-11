# -*- coding:utf-8 -*-
import requests
import json
import csv


class TaobaoSpider(object):
    # 由于我的淘宝是海外版,所以会有一个world二级域名。各位在国内没有翻墙的同学,下面这个地址可能会和我的不一样
    JSON_URL = 'https://www.taobao.com'

    def __init__(self, keyword):
        self.url = self.JSON_URL.format(keyword)
        html = self.get_source()
        result_list = self.get_item_list(html)
        self.write_data(result_list)

    def get_source(self):
        html = requests.get(self.url)
        return html.content.decode('GBK')  # 由于返回的数据是GBK编码,所以必须要用解码,否则会有乱码出现

    def get_item_list(self, source):
        item_dict = json.loads(source)
        item_list = item_dict['itemList']
        result_list = []
        for item in item_list:
            result_dict = {}
            result_dict['title'] = item['title'].replace('<span class=H>', '').replace('</span>', '')
            result_dict['url'] = 'http:' + item['href']
            result_dict['location'] = item['loc']
            result_dict['shop'] = item['nick']
            result_dict['price'] = item['price']
            result_dict['price_wap'] = item['priceWap']
            print(result_dict)
            result_list.append(result_dict)
        return result_list

    def write_data(self, result_list):
        with open('result.csv', 'w', encoding='UTF-8') as f:
            writer = csv.DictWriter(f, fieldnames=['title', 'price', 'shop', 'location', 'price_wap', 'url'])
            writer.writeheader()
            writer.writerows(result_list)


if __name__ == '__main__':
    keyword = input('请输入关键词: ')
    TaobaoSpider(keyword)
