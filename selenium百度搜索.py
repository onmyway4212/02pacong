from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

firefox = Options()
firefox.add_argument('--headless')  # 这个参数后变无头浏览器
driver = webdriver.Firefox(firefox_options=firefox)
driver.get('https://www.baidu.com/')
# id = 'cp'的属性
print(driver.find_element_by_id('cp').text)
print(driver.find_element_by_id('u1').text)

# 搜索框是id='kw'的属性,百度一下是id='su'
driver.find_element_by_id('kw').clear()  # 用于清除输入框的内容
driver.find_element_by_id('kw').send_keys('Hello')  # 在输入框内输入Hello
driver.find_element_by_id('su').click()  # 用于点击按钮
driver.find_element_by_id('su').submit()  # 用于提交表单内容
print(driver.page_source)
