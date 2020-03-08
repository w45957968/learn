# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://59.57.149.33:49120")
# options.add_argument("--proxy-server=http://49.70.208.143:31414")
driver_path = r"D:\chromedriver\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)
driver = webdriver.Chrome(executable_path=driver_path)

# driver.get("http://httpbin.org/ip")
driver.get("http://www.baidu.com")
inputTag = driver.find_element_by_id("kw")

inputTag.send_keys("IP")

clickTag = driver.find_element_by_id("ss")

# clickTag.click()