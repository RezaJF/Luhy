# -*- coding: UTF-8 -*-

from selenium import webdriver
import time


driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com")
data = driver.find_element_by_id('wrapper').text[0:10]
print(data)


