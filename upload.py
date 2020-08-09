# coding=utf-8
from selenium import webdriver
import os
import time
driver = webdriver.Firefox()
file_path='File:///' + os.path.abspath("E://javatest//200808//selenium_html//upload.html")
driver.get(file_path)
driver.maximize_window()

# 上传文件
driver.find_element_by_tag_name("input").send_keys("E://javatest//200808//selenium_html//upload.html");

time.sleep(5)
driver.quit()