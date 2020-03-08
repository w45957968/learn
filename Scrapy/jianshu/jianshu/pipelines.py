# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class JianshuPipeline(object):

    def __init__(self):
        params = {
            "host":"127.0.0.1",
            "port": 3306,
            "user":"root",
            "password":"c123",
            "database":"xiciip"
        }
        self.conn = pymysql.connect(host="127.0.0.1",
                                    port = 3306,
                                    user ="root",
                                    password = "c123",
                                    database = "xiciip"
        )
        self.sursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """insert into jianshu(ID,Title,Writer,Article,Article_ID) values(null,%s,%s,%s,%s)"""
        self.sursor.execute(insert_sql,((item["title"],item["writer"],item["article"],item["article_id"])))
        print("=+"*40)
        self.conn.commit()
        # self.conn.close()
        return item
