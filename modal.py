# coding=utf-8
from selenium import webdriver
import os
import time
driver = webdriver.Firefox()
file_path='File:///' + os.path.abspath("E://javatest//200808//selenium_html//model.html")
driver.get(file_path)
driver.maximize_window()

# 用 class 定位 div（对话框问题）
# 点击 click
driver.find_element_by_id("show_modal").click()
time.sleep(5)

# 定位 modal-body(对话框内容)
div1 = driver.find_element_by_class_name("modal-body")
driver.find_element_by_link_text("click me").click()
time.sleep(5)

# 定位 modal-footer
div2 = driver.find_element_by_class_name("modal-footer")
# 用数组定位 tag name
buttons = div2.find_elements_by_tag_name("button")
# buttons[0]: close
# buttons[1]: Save Changes
buttons[0].click()

time.sleep(5)
driver.quit()

