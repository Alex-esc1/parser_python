import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox(executable_path=r"C:/test/geckodriver.exe")
browser.get('https://passport.yandex.by/')

emailElem = browser.find_element_by_id('passp-field-login')
emailElem.send_keys('ЛОГИН ПОЧТЫ')
emailElem.send_keys(Keys.ENTER)
time.sleep(2)

passwordElem = browser.find_element_by_id('passp-field-passwd')
passwordElem.send_keys('ПАРОЛЬ ПОЧТЫ')
passwordElem.send_keys(Keys.ENTER)
time.sleep(2)

browser.get('https://mail.yandex.by/')
#browser.find_element_by_link_text('#compose')
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mail-ComposeButton-Text"))).click()
time.sleep(5)

toElem = browser.find_element_by_class_name("composeYabbles")
toElem.send_keys('КОМУ ОТПРАВЛЯЕМ')
time.sleep(2)

subjElem = browser.find_element_by_name("subject")
subjElem.click()
subjElem.send_keys('Test with selenium')
time.sleep(2)

bodyElem = browser.find_element_by_css_selector('.cke_wysiwyg_div')
bodyElem.click()
bodyElem.send_keys('A test email with selenium')
time.sleep(2)

sendElem = browser.find_element_by_css_selector('.Button2_view_default')
sendElem.click()
print("Письмо отправлено успешно")