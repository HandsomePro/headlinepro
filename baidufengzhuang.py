from selenium import webdriver
from time import sleep
import threading


def get_baidu(driver):
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys('python doc')
    driver.find_element_by_id('su').click()
    sleep(3)
    driver.quit()


def get_driver(browser):
    cap = {}
    if 'chrome' == browser:
        cap = webdriver.DesiredCapabilities.CHROME.copy()
    elif 'firefox' == browser:
        cap = webdriver.DesiredCapabilities.FIREFOX.copy()
    cap['platform'] = 'WINDOWS'
    return webdriver.Remote('http://127.0.0.1:4444/wd/hub', cap)


browsername = ['firefox', 'chrome']
for browser in browsername:
    driver = get_driver(browser)
    threading.Thread(target=get_baidu, args=(driver,)).start()
