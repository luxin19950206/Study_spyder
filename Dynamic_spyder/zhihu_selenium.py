from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


user_name = 'luxin19950206@126.com' #你的账号
pass_word = '2012wuaixingYONG' #你的密码

driver = webdriver.Chrome()
driver.get('https://www.zhihu.com/#signin')

account = driver.find_element_by_name('SignFlow-account')
account.clear()
account.send_keys(user_name)
password = driver.find_element_by_name('SignFlow-password')
password.clear()
password.send_keys(pass_word)
account.send_keys(Keys.RETURN)
time.sleep(10)
print(driver.page_source)
driver.close()
