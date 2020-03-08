# -*- coding: utf-8 -*-
import scrapy
import json


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        user_agent = response.text

        print("*"*40)
        print(user_agent)
        print("*"*40)
        yield scrapy.Request(self.start_urls[0],dont_filter=True)