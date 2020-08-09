# coding=utf-8
from selenium import webdriver
import os
import time
driver = webdriver.Firefox()
file_path='File:///' + os.path.abspath("E://javatest//200808//selenium_html//drop_down.html")
driver.get(file_path)
driver.maximize_window()

# 下拉框处理
# 方法一：直接 xpath 定位
# driver.find_element_by_xpath("//*[@id='ShippingMethod']/option[4]").click()

# 方法二：用 option 定位（循环）
lists = driver.find_element_by_tag_name("option")
# for list in lists:
#     if list.get_attribute("value") == '9.03':
#         list.click()
# 或
# lists[3].click()

time.sleep(5)
driver.quit()