# selenium操作Cookie

from selenium import webdriver

driver_path = 'D:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

# 1、获取所有的cookie信息
# driver.get('https://www.baidu.com/')
# for cookie in driver.get_cookies():
#     print(cookie)


# 2、根据cookie的key获取值
# driver.get('https://www.baidu.com/')
# value = driver.get_cookie('PSTM')
# print(value)


# 3、删除所有的cookie
# driver.get('https://www.baidu.com/')
# driver.delete_all_cookies()


# 4、删除某一个cookie
driver.get('https://www.baidu.com/')
print(driver.get_cookie('PSTM'))
driver.delete_cookie('PSTM')
print(driver.get_cookie('PSTM'))
