# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WxAppSpider(CrawlSpider):
    name = 'wx_app'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-.+\.html'), callback='parse_item', follow=False),
    )
    # rules = (
    #     Rule(LinkExtractor(allow=r'article-.+\.html'), callback='parse_item', follow=True),
    # )

    def parse_item(self, response):
        item = {}
        title = response.xpath("//div[@class='cl']/h1/text()").extract()[0]
        articlelist = response.xpath('//td[@id="article_content"]//text()').extract()
        article = "".join(articlelist).strip()
        print(article)
