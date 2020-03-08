# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from threading import Thread
from queue import Queue
from lxml import etree
import pymongo


client = pymongo.MongoClient("127.0.0.1", port=27017)
db = client.zhihu
collection = db.lagou
# data = requests.get("http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=9e5b6513d46949a68c14343104c7199a&orderno=YZ20197309806djvxfi&returnType=1&count=5").content.decode()
# proxy_pool =data.split()

# options = webdriver.ChromeOptions()
# options.add_argument("--proxy-server=http://59.57.149.33:49120")

driver_path = r"D:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

worklist = Queue(10000)


class firstSpider():
    global driver, worklist, collection
    url = "https://www.lagou.com/jobs/list_python/p-city_0"

    def spiderList(self):
        driver.get(self.url)
        page_data = driver.page_source
        return page_data

    def get_list(self, page_data):
        html = etree.HTML(page_data)
        list = html.xpath('//a[@class="position_link"]/@href')
        for i in list:
            worklist.put(i)



    def run(self):
        # 1 . 爬取第一页
        page_data = self.spiderList()

        # 2 .获取第一页数据与链接，并加入队列
        self.get_list(page_data)
        while True:
            sleep(2)
            try:

                print("下一页")
                next_Tag = driver.find_element_by_class_name("pager_next ")
                if "pager_next_disabled" in next_Tag.get_attribute("class"):
                    break
                next_Tag.click()
            except Exception as e:
                print(e)
                print("结束")
                driver.quit()
                break
            self.get_list(driver.page_source)
            print(worklist.qsize())

class Get_info(Thread):
    global collection,worklist,driver_path


    def get_info(self):
        print(worklist.qsize())
        url = worklist.get()

        driver1 = webdriver.Chrome(executable_path=driver_path)
        driver1.get(url=url)
        html = etree.HTML(driver1.page_source)
        job_name = html.xpath('//span[@class="ceil-job"]/text()')
        job_salary = html.xpath('//span[@class="ceil-salary"]/text()')
        job_advantage = html.xpath('//dd[@class="job-advantage"]/p/text()')
        job_detail = "".join(html.xpath('//div[@class="job-detail"]//p/text()'))
        job_addr = "".join(html.xpath('//div[@class="work_addr"]/a/text()')[0:-1]) + "".join(
            html.xpath('//div[@class="work_addr"]/text()')).strip()
        com_name = html.xpath('//img[@class="b2"]/@alt')
        com_home = html.xpath('//ul[@class="c_feature"]/li/a/@href')
        job_request = "".join(html.xpath('//dd[@class="job_request"]/h3/span/text()')[1:])
        worklist.task_done()
        data = {
            "职位": job_name,
            "薪资": job_salary,
            "要求": job_request,
            "福利": job_advantage,
            "职责": job_detail,
            "工作地址": job_addr,
            "公司名称": com_name,
            "公司官网": com_home
        }
        collection.insert_one(data)
        sleep(1)
        driver1.quit()

    def run(self):
        print("开始")
        while True:
            if worklist.qsize():
                self.get_info()
            else:
                break


def start():
    for i in range(1,11):
        t = Get_info()
        t.start()



if __name__ == '__main__':
    d = firstSpider()
    d.run()
    start()
    # sleep(10)
    # c = Get_info()
    # c.run()
