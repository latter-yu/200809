# coding=utf-8
from selenium import webdriver
import os
import time
driver = webdriver.Firefox()
file_path='File:///' + os.path.abspath("E://javatest//200808//selenium_html//level_locate.html")
driver.get(file_path)
driver.maximize_window()

# 层级定位
# 先点击显示出 1 个下拉菜单（link1)
driver.find_element_by_link_text("Link1").click()
time.sleep(5)
# 然后再定位到该下拉菜单所在的 ul(Another action)
btn = driver.find_element_by_link_text("Another action")
# 再定位这个 ul 下的某个具体的 link
# 由鼠标移动实现（move_to_element）
webdriver.ActionChains(driver).move_to_element(btn).perform()

time.sleep(5)
driver.quit()
