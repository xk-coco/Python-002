#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 22:26
# @File    : mimicLoginshimo.py

from selenium import webdriver
import time
import os

os.putenv('PATH', 'D:\\Program Files\\Mozilla Firefox\\')

try:
    # 需要安装Firefox driver，和浏览器版本保持一致，地址：
    #  	https://github.com/mozilla/geckodriver/releases
    brower = webdriver.Firefox()
    brower.get("https://shimo.im")
    brower.maximize_window()
    time.sleep(2)
    brower.find_element_by_xpath("//a[@href='/login?from=home']/button").click()
    brower.find_element_by_name("mobileOrEmail").send_keys('132****4027')
    brower.find_element_by_xpath("//div[@class='input']/input[@type='password']").send_keys('******')
    time.sleep(2)
    shiMo_login_button = brower.find_element_by_xpath("//div[@class='form-wrapper']/div/div/button")
    shiMo_login_button.click()
    cookies_value = brower.get_cookies()  # 获取cookie值
    print(cookies_value)
    time.sleep(1)

except Exception as e:
    print(e)
finally:
    brower.close()
