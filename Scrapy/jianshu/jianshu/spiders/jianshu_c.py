# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items import JianshuItem


class JianshuCSpider(CrawlSpider):
    name = 'jianshu_c'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/p/[0-9a-z]{12}'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        data = response.text
        # print(data)
        title = response.xpath("//body/div/div/div/div/section/h1/text()").extract()[0]
        writer = response.xpath("//div/header/div/div/div/div/a/span/text()").extract()[0]
        # pub_time = response.xpath("//div[@class='s-dsoj']/time/text()").extract()
        # pageview = response.xpath("//div[@class='s-dsoj']/span/text()").extract()[1]
        # aria = response.xpath("//div[@class='_3BUZPB']/span/text()").extract()
        article = "".join(response.xpath("//body/div/div/div/div/section/article/p/text()").extract())
        article_id = response.url.split("p/")[1][0:12]
        item = JianshuItem(
            title = title,
            writer = writer,
            article = article,
            article_id = article_id
        )
        yield item
        # print("="*40)
        print(title)
        print(writer)
        print(article)
        print(article_id)
        # print("=" * 40)


