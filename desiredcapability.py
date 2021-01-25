from selenium import webdriver

dic = webdriver.DesiredCapabilities.CHROME.copy()
dic['platform'] = 'WINDOWS'
print(dic)
