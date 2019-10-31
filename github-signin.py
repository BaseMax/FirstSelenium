# Max Base
# https://github.com/BaseMax
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

# browser.get('https://www.github.com/')
# document.querySelector("a.HeaderMenu-link.no-underline.mr-3")
# button = browser.find_element_by_css_selector('a.HeaderMenu-link.no-underline.mr-3')
# button.click()

browser.get('https://github.com/login')

username = browser.find_element_by_css_selector('input#login_field')
password = browser.find_element_by_css_selector('input#password')
username.send_keys('username')
password.send_keys('password' + Keys.RETURN)
print(browser.title)

# browser.quit()
