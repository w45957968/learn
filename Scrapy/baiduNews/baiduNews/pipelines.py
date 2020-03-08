# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BaidunewsPipeline(object):
    def process_item(self, item, spider):
        print(len(item["title"]))
        print(len(item["link"]))

        with open("百度新闻.txt","a")as f:
            f.write(item["title"][0]+"\n"+"".join(item["link"])+"\n")
            f.close()

        return item
