# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影名
    name = scrapy.Field()
    # 电影海报
    image = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 电影信息
    info = scrapy.Field()
    # 电影简介
    desc = scrapy.Field()
    # 电影人员
    ower = scrapy.Field()
