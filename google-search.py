from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://www.google.com/')
print(browser.title)

search = browser.find_element_by_name('input')
search.send_keys('BaseMax' + Keys.RETURN)

browser.quit()
