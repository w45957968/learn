# -*- coding: utf-8 -*-
from lxml import etree
import re


parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('拉钩1.html',parser=parser)

link_list = html.xpath('//a[@class="position_link"]/@href')
print(link_list)
