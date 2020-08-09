# coding=utf-8
from selenium import webdriver
import os
import time
driver = webdriver.Firefox()
file_path='File:///' + os.path.abspath("E://javatest//200808//selenium_html//alert.html")
driver.get(file_path)
driver.maximize_window()

# alert: 警告框
# 点击链接, 弹出警告框
# text 返回alert/conﬁrm/prompt 中的文字信息
# accept 点击确认按钮
# dismiss 点击取消按钮(如果有的话)
# send_keys 输入值，这个 alert\conﬁrm 没有对话框就不能用了，不然会报错

# 定位点击按钮
driver.find_element_by_id("tooltip").click()
time.sleep(5)
# 若报错, 大概率是没加载出来, 可适当延长等待时间
# 得到操作 alert 弹出框的句柄
alert = driver.switch_to.alert
# 输出弹出框的按钮
text = alert.text
print("text = " + text)
time.sleep(7)
alert.accept()

time.sleep(5)
driver.quit()