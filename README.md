# First Selenium

Some sample codes for using **selenium** in **Python** just for fun.

## Selenium Sample Projects

- [x] Google Search
- [x] GitHub Search
- [x] GitHub SignIn
- [x] Yahoo Maktoob News
- [ ] Yahoo Search
- [ ] Gmail Register (Need captcha...)
- [ ] GitHub Register (Need captcha...)

## Selenium Browser Helper

```python
from selenium import webdriver
```

#### Then, you can access the classes like this:

- webdriver.Firefox
- webdriver.FirefoxProfile
- webdriver.Chrome
- webdriver.ChromeOptions
- webdriver.Ie
- webdriver.Opera
- webdriver.PhantomJS
- webdriver.Remote
- webdriver.DesiredCapabilities
- webdriver.ActionChains
- webdriver.TouchActions
- webdriver.Proxy

https://selenium-python.readthedocs.io/api.html

## Selenium Locating Elements Helper

There are various strategies to locate elements in a page. You can use the most appropriate one for your case.

### Selenium provides the following methods to locate elements in a page:

- find_element_by_id
- find_element_by_name
- find_element_by_xpath
- find_element_by_link_text
- find_element_by_partial_link_text
- find_element_by_tag_name
- find_element_by_class_name
- find_element_by_css_selector

### To find multiple elements (these methods will return a list):

- find_elements_by_name
- find_elements_by_xpath
- find_elements_by_link_text
- find_elements_by_partial_link_text
- find_elements_by_tag_name
- find_elements_by_class_name
- find_elements_by_css_selector

Apart from the public methods given above, there are two private methods which might be useful with locators in page objects. These are the two private methods: find_element and find_elements.

### Example usage:

```python
from selenium.webdriver.common.by import By

driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')
```

#### These are the attributes available for By class:

```python
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
```

## Example using Selenium Locating Elements:

```python
login_form = driver.find_element_by_id('loginForm')

heading1 = driver.find_element_by_tag_name('h1')

continue = driver.find_element_by_name('continue')
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

content = driver.find_element_by_class_name('content')

content = driver.find_element_by_css_selector('p.content')

continue_link = driver.find_element_by_link_text('Continue')
continue_link = driver.find_element_by_partial_link_text('Conti')

login_form = driver.find_element_by_xpath("/html/body/form[1]")
login_form = driver.find_element_by_xpath("//form[1]")
login_form = driver.find_element_by_xpath("//form[@id='loginForm']")

username = driver.find_element_by_xpath("//form[input/@name='username']")
username = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")
username = driver.find_element_by_xpath("//input[@name='username']")

clear_button = driver.find_element_by_xpath("//input[@name='continue'][@type='button']")
clear_button = driver.find_element_by_xpath("//form[@id='loginForm']/input[4]")
```

## Selenium Getting Started

### Simple Usage Selenium

If you have installed Selenium Python bindings, you can start using it from Python like this.

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
```

https://chromedriver.chromium.org/getting-started

https://selenium-python.readthedocs.io/getting-started.html

---------

# Max Base

My nickname is Max, Programming language developer, Full-stack programmer. I love computer scientists, researchers, and compilers.

## Asrez Team

A team includes some programmer, developer, designer, researcher(s) especially Max Base.

[Asrez Team](https://www.asrez.com/)
