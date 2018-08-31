# selenium+chromedriver模拟浏览器行为

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver_path = r'D:\chromedriver\chromedriver.exe'  # chromedriver驱动的路径

driver = webdriver.Chrome(executable_path=driver_path)  # 通过chromedriver去驱动谷歌浏览器


# 1、通过driver对象去操作浏览器，driver.get会打开浏览器并访问指定的url
# driver.get('https://www.baidu.com/')


# 2、driver.page_source可以打印出网页HTML代码
# print(driver.page_source)


# 3、close关闭当前页面
# driver.get('https://www.baidu.com/')
# time.sleep(3)
# driver.close()


# 4、quit直接退出浏览器
# driver.get('https://www.baidu.com/')
# time.sleep(3)
# driver.quit()


# 5、定位元素, element获取一个元素，elements获取多个元素，返回一个列表
driver.get('https://www.baidu.com/')  # 打开浏览器
# inputTag = driver.find_element_by_id('kw')  # 定位id
# inputTag = driver.find_element(By.ID, 'kw')  # 定位id

# inputTag = driver.find_element_by_name('wd')  # 定位name
# inputTag = driver.find_element(By.NAME, 'wd')  # 定位name

# inputTag = driver.find_element_by_class_name('s_ipt')  # 定位class name
# inputTag = driver.find_element(By.CLASS_NAME, 's_ipt')  # 定位class name

# inputTag = driver.find_element_by_xpath('//input[@id="kw"]')  # 通过xpath语法定位元素
# inputTag = driver.find_element(By.XPATH, '//input[@id="kw"]')  # 通过xpath语法定位元素


# inputTag = driver.find_element_by_css_selector('.quickdelete-wrap > input')  # 通过css选择器来定位元素
inputTag = driver.find_element(By.CSS_SELECTOR, '.quickdelete-wrap > input')  # 通过css选择器来定位元素
inputTag.send_keys('python')  # 搜索的关键字


