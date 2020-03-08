# -*- coding: utf-8 -*-
import scrapy
from Scrapy_bdj.items import ScrapyBdjItem
from scrapy.http import Request


class BdjSpider(scrapy.Spider):
    name = 'bdj'
    allowed_domains = ['budejie.com']
    start_urls = ['http://www.budejie.com/1']

    def parse(self, response):
        item = ScrapyBdjItem()

        print("=="*40)
        # item["writer"] = response.xpath("//ul/li/div[@class='j-list-user']/div[@class='u-txt']/a/text()").extract()
        item["writer"] = response.xpath("//div[@class='u-txt']/a/text()").extract()
        item["title"] = response.xpath("//div[@class='j-r-list-c-desc']/a/text()").extract()
        item["pic"] = response.xpath("//div[@class='j-r-list-c-img']/a/img/@data-original").extract()

        yield item
        for i in range(2,200):
            url = "http://www.budejie.com/%d"%i
            yield Request(url,callback=self.parse)


        print("==" * 40)
