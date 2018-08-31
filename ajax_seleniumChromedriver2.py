# 操作表单元素

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver_path = 'D:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)


# 1、操作输入框
# driver.get('https://www.baidu.com/')
# inputTag = driver.find_element_by_id('kw')
# inputTag.send_keys('python')  # 输入框中输入关键字
# time.sleep(3)
# inputTag.clear()  # 清除输入框中的搜索关键字


# 2、操作checkbox选中框
# driver.get('https://www.douban.com/')
# rememberBtn = driver.find_element_by_name('remember')
# rememberBtn.click()  # 选中记住我前面的√


# 3、操作select下拉框
# driver.get('http://www.dobai.cn/')
# selectBtn = Select(driver.find_element_by_name('jumpMenu'))
# # selectBtn.select_by_index(1)  # 通过索引来访问下拉列表中的选项
# # selectBtn.select_by_value('http://m.95xiu.com/')  # 通过value元素来访问下拉列表中的选项
# selectBtn.select_by_visible_text('95秀客户端')  # 通过下拉列表中的文本来访问选项


# 操作按钮
driver.get('https://www.baidu.com/')
inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('python')

submitTag = driver.find_element_by_id('su')  # 定位百度一下的按钮id
submitTag.click()  # 点击按钮


