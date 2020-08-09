# coding=utf-8
from selenium import webdriver
import os
import time
driver = webdriver.Firefox()
file_path='File:///' + os.path.abspath("E://javatest//200808//selenium_html//checkbox.html")
driver.get(file_path)
driver.maximize_window()

# 定位一组元素
# 先获取全部对象，再在这组对象中获取所有 checkbox
inputs = driver.find_elements_by_tag_name("input")
time.sleep(5)
for input in inputs:
    if input.get_attribute('type') == "checkbox":
        # get_attribute：获得属性值
        input.click()
time.sleep(5)
driver.quit()