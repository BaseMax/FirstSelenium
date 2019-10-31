# Max Base
# https://github.com/BaseMax
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.github.com/')

# document.querySelector("input.form-control.input-sm.header-search-input.jump-to-field.js-jump-to-field.js-site-search-focus")
search = browser.find_element_by_css_selector('input.form-control.input-sm.header-search-input.jump-to-field.js-jump-to-field.js-site-search-focus')
search.send_keys('BaseMax' + Keys.RETURN)
print(browser.title)

browser.quit()
