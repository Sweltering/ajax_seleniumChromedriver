# 页面等待、切换页面

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver_path = 'D:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

# 1、隐式等待，等待指定时间，没有响应抛出异常
# driver.get("https://www.douban.com/")
# driver.implicitly_wait(60)
# driver.find_element_by_id('sdasdfsdaf')


# 2、显示等待，如果已经获取到，就不需要等待
# driver.get('https://www.douban.com/')
# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, 'form_email'))
# )
# print(element)


# 3、打开一个新的页面
# driver.get('https://www.baidu.com/')
# driver.execute_script('window.open("https://www.douban.com/")')


# 4、切换页面
driver.get('https://www.baidu.com/')
driver.execute_script('window.open("https://www.douban.com/")')
print(driver.current_url)  # 虽然打开了一个新的页面，但是driver还是在百度的页面中
driver.switch_to_window(driver.window_handles[1])  # 切换页面
print(driver.current_url)




