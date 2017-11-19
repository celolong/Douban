# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from openpyxl import Workbook

class DoubanPipeline(object):
    def __init__(self):
        self.file = open('douban.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        str_data = json.dumps(dict(item),ensure_ascii=False) + ',\n'
        self.file.write(str_data)
        return item

    def close_spider(self):
        self.file.close()


# 以excel格式保存
class DbexcelPipeline(object):  # 设置工序一
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['电影名', '电影海报地址', '评分', '电影信息', '电影简介', '电影人员'])  # 设置表头

    def process_item(self, item, spider):  # 工序具体内容
        line = [item['name'], item['image'], item['score'], item['info'], item['desc'], item['ower']]  # 把数据中每一项整理出来
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('douban.xlsx')  # 保存xlsx文件
        return item