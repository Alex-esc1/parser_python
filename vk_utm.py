import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from time import sleep
from random import randint
import requests

##Чтение ссылки из текстового файла
f = open('blogurl.txt', 'r')
blogurl = f.readline()
blogurl=blogurl+' '
kolbs = len(blogurl)
print ('Blog url: '+blogurl)
 
print("\nConnection success...")
## настройки мозила
options = Options()
options.headless = True
driver = webdriver.Firefox(executable_path=r"C:/test/geckodriver.exe")
driver.maximize_window()
 
 
#Вход в соцсеть
driver.get("http://vk.com")
sleep(5)
driver.find_element_by_id("index_email").send_keys('+375291111111')##вместо yourlogin вводин свой логин или номер телефона
sleep(2)
pwd = driver.find_element_by_id("index_pass")
pwd.send_keys('123423534345')# Вводим пароль вместо YoUrPaSSwOrD
pwd.send_keys(Keys.ENTER)
sleep(7)
 
driver.implicitly_wait(30)

with open("1.txt", "r", encoding="utf-8") as file:
    for line in file:
      URL = line.strip()
      driver.get(URL)
      sleep(randint(3,5))
      e = driver.find_element_by_id("post_field")
      e.clear()
      act = ActionChains(driver)
      act.move_to_element(e).perform()
      act = ActionChains(driver)
      act.click(e).perform()
      sleep(3)
      act = ActionChains(driver)
      act.send_keys(blogurl).perform()
      sleep(3)
      for _ in range(kolbs):
        act = ActionChains(driver)
        act.send_keys(Keys.BACKSPACE).perform()
      act.send_keys('http://minus50.by/category/stroitelnye-materialy?utm_source=vk').perform()
      sleep(3)
      driver.find_element_by_id("send_post").click()
      sleep(3)

#закрываем браузер
driver.close()
