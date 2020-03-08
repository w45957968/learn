# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ScrapyBdjPipeline(object):
    def process_item(self, item, spider):
        # conn = pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="库名")

        for i in range(0,len(item["writer"])):
            writer = item["writer"][i]
            title = item["title"][i]
            # pic = item["pic"][i]
            # print(writer+":\n"+title)
            # spl = "insert into 表名(列标题1，列标题2，列标题3) values('"+值1+"','"+值2+"','"+值3+"')"
            with open("不得姐笑话.txt","a")as f:
                f.write(writer+":\n------"+title+"\n")
                f.close()
        for i in range(0,len(item["pic"])):
            pic = item["pic"][i]
            with open("不得姐图片链接.txt","a")as f:
                f.write(pic+"\n")
                f.close()
            # try:
                # conn.query(sql)
            # except Exception as e:
                # print(e)
        # conn.close()
        return item
