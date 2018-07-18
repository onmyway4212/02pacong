from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox = Options()
# firefox.add_argument('--headless')  # 这个参数后变无头浏览器
driver = webdriver.Firefox(firefox_options=firefox)
driver.get("http://www.baidu.com/")

size = driver.find_element_by_name("wd").size
print(size)
# 搜索框的大小尺寸: {'width': 500, 'height': 22}
'''

'''
news = driver.find_element_by_xpath("//div[@id='u1']/a[1]").text
print(news)
# 文本: 新闻

href = driver.find_element_by_xpath("//div[@id='u1']/a[2]").get_attribute('href')
name = driver.find_element_by_xpath("//div[@id='u1']/a[2]").get_attribute('name')
print(href, name)
# 属性值: http://www.hao123.com/ tj_trhao123

location = driver.find_element_by_xpath("//div[@id='u1']/a[3]").location
print(location)
# 坐标: {'y': 19, 'x': 498}

print(driver.current_url)
# 当前链接: https://www.baidu.com/
print(driver.title)
# 标题: 百度一下， 你就知道

result = location = driver.find_element_by_id("su").is_displayed()
print(result)
# 是否可见: True


'''
    size 获取元素的尺寸
    text 获取元素的文本
    get_attribute(name) 获取属性值
    location 获取元素坐标，先找到要获取的元素，再调用该方法
    page_source 返回页面源码
    driver.title 返回页面标题
    current_url 获取当前页面的URL
    is_displayed() 设置该元素是否可见
    is_enabled() 判断元素是否被使用
    is_selected() 判断元素是否被选中
    tag_name 返回元素的tagName
'''
