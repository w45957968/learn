# -*- coding: utf-8 -*-
import scrapy
from baiduNews.items import BaidunewsItem
from scrapy.http import Request
import urllib.parse
import re



class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['baidu.com']
    start_urls = ["http://news.baidu.com/widget?id=DiscoveryNews&ajax=json"]


    def parse(self, response):
        id = ['EnterNews', 'FinanceNews', 'HealthNews', 'InternationalNews', 'InternetNews',
              'LadyNews', 'LocalNews', 'MilitaryNews', 'PicWall', 'SportNews', 'civilnews']

        data = response.body.decode("utf-8")
        # print("="*40)
        pat_link1 = r'"m_url":"(.*?)"'
        link1 = re.compile(pat_link1).findall(data,re.S)
        for i in range(0,len(link1)):
            if not "cmd" in link1[i]:
                link = re.sub("\\\/","/",link1[i])
                yield Request(link,callback=self.getTitle)


        # print("="*40)
        for j in range(0,len(id)):
            url = "http://news.baidu.com/widget?id=%s&ajax=json" % id[j]
            # print("***"*40)
            yield Request(url,callback=self.parse)

    def getTitle(self,response):
        item = BaidunewsItem()
        item["title"] = response.xpath('/html/head/title/text()').extract()
        item["link"] = response.url
        yield item
        # print(item["link"])