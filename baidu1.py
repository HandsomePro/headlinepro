from time import sleep

from selenium import webdriver as we
import appium.webdriver


# driver = webdriver.Chrome()
driver = we.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Ie()
# cab={
#     'browserName':'firefox',
#     'version':'',
#     'platform':'WINDOWS'
# }
# driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', cab)
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys('python')
driver.find_element_by_id('su').click()
sleep(3)
driver.quit()
