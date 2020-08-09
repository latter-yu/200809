# coding=utf-8
from selenium import webdriver
import os
import time
driver = webdriver.Firefox()
file_path='File:///' + os.path.abspath("E://javatest//200808//selenium_html//frame.html")
driver.get(file_path)
driver.maximize_window()

# 多层框架/窗口定位
# 多层框架(frame) 或 窗口(window) 的定位：
# switch_to.frame()
# switch_to.window()
# switch_to.default_content：从frame中嵌入的页面里跳出，跳回到外面的原始页面中

# 多层页面嵌套
# 需要先定位到当前页面进行操作
# driver.switch_to_frame("f1") 已弃用
driver.switch_to.frame("f1")
driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys("三十而已")
driver.find_element_by_id("su").click()
time.sleep(5)
# 要定位 click, 还需回到最开始的默认页面
# driver.switch_to_default_content() 已弃用
driver.switch_to.default_content()
driver.switch_to.frame("f1")
driver.find_element_by_link_text("click").click()
time.sleep(5)
driver.quit()