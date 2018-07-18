import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

# 鼠标移动至图片上 右键保存图片
elem_pic = driver.find_element_by_xpath("//div[@id='lg']/img")
print(elem_pic.get_attribute("src"))
action = ActionChains(driver).move_to_element(elem_pic)
action.context_click(elem_pic)

# 重点:当右键鼠标点击键盘光标向下则移动至右键菜单第一个选项
action.send_keys(Keys.ARROW_DOWN)
time.sleep(3)
action.send_keys('v')  # 另存为
action.perform()

# # 获取另存为对话框(失败)
# alert.switch_to_alert()
# alert.accept()