# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Douban.items import DoubanItem

class MoviesSpider(CrawlSpider):
    name = 'movies'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    rules = (
        # 提取每一页
        Rule(LinkExtractor(allow=r'\?start=\d+&filter='), callback='parse_item', follow=True),
        # # 提取到详情页面的链接,这里记得将follow改为False,否则进入详情页面后会继续筛选(以下是单独筛选直接进入详情页面)
        # Rule(LinkExtractor(allow=r'https://movie.douban.com/subject/\d+?/'), callback='parse_detail', follow=False)
    )

    def parse_item(self, response):
        # 获取所有电影节点列表
        movie_list = response.xpath('//div[@class="item"]')
        for movie in movie_list:
            # 创建item实例
            item = DoubanItem()
            item['name'] = movie.xpath('./div[2]/div[1]/a/span[1]/text()').extract()[0]
            item['image'] = movie.xpath('./div[1]/a/img/@src').extract()[0]
            item['score'] = movie.xpath('./div[2]/div[2]/div/span[2]/text()').extract()[0]
            item['info'] = movie.xpath('./div[2]/div[2]/p[2]/span/text()').extract()[0]
            item['ower'] = ''.join([i.strip() for i in movie.xpath('./div[2]/div[2]/p[1]/text()').extract()]).replace('\xa0','')
            url = movie.xpath('./div[1]/a/@href').extract()[0]
            print(url,'++++++++++++++++++++++')
            yield scrapy.Request(url,callback=self.parse_detail,meta={'mymeta':item})

    def parse_detail(self,response):
        item = response.meta['mymeta']
        item['desc'] = response.xpath('//*[@id="link-report"]/span[1]/text()').extract()[0].strip().replace('\u2022','')
        print(item)
        yield item




