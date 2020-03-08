# -*- coding: utf-8 -*-
import scrapy


class HttpbinIpSpider(scrapy.Spider):
    name = 'httpbin_ip'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        print("*" * 40)
        ip = response.text
        print("*" * 40)
        print(ip)
        # print(response.header)
        print("*" * 40)
        yield scrapy.Request(self.start_urls[0], dont_filter=True)
