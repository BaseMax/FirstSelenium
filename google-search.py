# Max Base
# https://github.com/BaseMax
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.google.com/')
search = browser.find_element_by_class_name('gLFyf')
search.send_keys('BaseMax' + Keys.RETURN)
print(browser.title)

browser.quit()
