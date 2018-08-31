# 设置代理ip、WebElement元素


# 1、设置代理ip
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# options.add_argument('--proxy-server=http://114.246.76.193:8118')
#
# driver_path = 'D:\chromedriver\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
#
# driver.get('http://httpbin.org/ip')


# 2、WebElement元素
from selenium import webdriver


driver_path = 'D:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com/')
driver.save_screenshot('baidu.png')  # 保存访问网页的截图

submitBtn = driver.find_element_by_id('su')
print(type(submitBtn))  # <class 'selenium.webdriver.remote.webelement.WebElement'>
print(submitBtn.get_attribute('value'))  # 获取属性值


