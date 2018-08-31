# 行为链：有时候在页面中的操作有很多步，那么这时候可以使用鼠标行为链来完成
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = 'D:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

# 1、将鼠标移动到某个元素上并执行点击事件
driver.get('https://www.baidu.com/')

inputTag = driver.find_element_by_id('kw')  # 输入框
submitBtn = driver.find_element_by_id('su')  # 按钮

actions = ActionChains(driver)  # 行为链
actions.move_to_element(inputTag)  # 鼠标移动到输入框上
actions.send_keys_to_element(inputTag, 'python')  # 在输入框中输入搜索关键字
actions.move_to_element(submitBtn)  # 鼠标移动到按钮上
actions.click(submitBtn)  # 点击按钮
actions.perform()  # 完成


