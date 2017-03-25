import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox(executable_path='D:\Users\Nishanth18\Desktop\geckodriver')
browser.get("https://www.facebook.com/")
time.sleep(10)
username = browser.find_element_by_css_selector('#email')
username.send_keys('nishanthvydanav@gmail.com')
password = browser.find_element_by_css_selector('#pass')
password.send_keys('v_nishanth18')
login = browser.find_element_by_css_selector('#u_0_q')
login.click()

D:\Users\Nishanth18\PycharmProjects\Selenium\facebook.py