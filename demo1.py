from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Ie()
cab = {
    'browserName': 'firefox',
    'version': '',
    'platform': 'WINDOWS'
}

cab1 = webdriver.DesiredCapabilities.CHROME.copy()
cab1['platform'] = 'WINDOWS'
print(cab1)
driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', cab1)
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys('python')
driver.find_element_by_id('su').click()
sleep(3)
driver.quit()
