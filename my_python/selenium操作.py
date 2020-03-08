# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver_path = r"D:\chromedriver\chromedriver80.exe"

driver = webdriver.Chrome(executable_path=driver_path)

driver.get("http://www.baidu.com")

# # inputTag = driver.find_element_by_id("kw")
# # inputTag = driver.find_element_by_name("wd")
# # inputTag = driver.find_element_by_class_name('s_ipt')
# inputTag = driver.find_element_by_xpath('//input[@id="kw"]')
#
# """inputTag.send_keys('python')
#
# click_Tag = driver.find_element_by_id('su')
# sleep(1)
# click_Tag.click()
# sleep(2)
#
# driver.close()"""
# print(driver.page_source)
"""inputTag = driver.find_element_by_id("kw")
clickTag = driver.find_element_by_id("su")

action = ActionChains(driver)

action.move_to_element(inputTag)

action.send_keys_to_element(inputTag, "python")

action.move_to_element(clickTag)

action.click(clickTag)

action.perform()"""
driver.execute_script("window.open('https://www.douban.com')")
print(driver.window_handles)
print(driver.current_url)
print("="*40)
sleep(5)
# driver.switch_to_window(driver.window_handles[1])
driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)
print(driver.page_source)
sleep(5)
driver.switch_to.window(driver.window_handles[0])
print(driver.current_url)
print(driver.page_source)
