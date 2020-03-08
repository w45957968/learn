from selenium import webdriver
from time import sleep
import re

browser = webdriver.PhantomJS()  #建立对象
browser.get("http：//www.baidu.com/")  #浏览网页
a = browser.get_screenshot_as_file("C:/Users/Administrator/Desktop/自己的程序/test.jpg") #截图
browser.find_element_by_xpath('//*[@id="kw"]').clear()  #清楚浏览器输入框
browser.find_element_by_xpath('//*[@id="kw"]').send_keys("要搜索的内容") #在输入框里输入内容
browser.find_element_by_xpath('//*[@id="su"]').click()  #点击按钮
sleep(5)  #等待五秒，给浏览器反应时间
a = browser.get_screenshot_as_file("C:/Users/Administrator/Desktop/自己的程序/test.jpg") #截图
# C:\Users\Administrator\Desktop\自己的程序
data = browser.page_source  #将页面内容赋值给data

browser.quit() #浏览器关闭
pat1 = "<title>(.*?)</title>"
title = re.copmile(pat1).findall(data)

print(title)


