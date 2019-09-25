from selenium import webdriver
import time
brower = webdriver.Chrome()
url_1 = 'http://hress.sig.dom/hress/login.php'
brower.get(url_1)

brower.find_element_by_name('username').send_keys('CN11321')
brower.find_element_by_name('password').send_keys('sMx141110~')
brower.find_element_by_name('login').click()

#enter
brower.find_element_by_name('submit').click()
print(brower.page_source)

