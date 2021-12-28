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
#driver = webdriver.Firefox(options=options, executable_path=r"C:/test/geckodriver.exe")
driver = webdriver.Firefox(executable_path=r"C:/test/geckodriver.exe")
driver.maximize_window()
 
 
#Вход в соцсеть
driver.get("http://facebook.com")
sleep(5)
driver.find_element_by_id("email").send_keys('+375333122224')##вместо yourlogin вводин свой логин или номер телефона
sleep(2)
pwd = driver.find_element_by_id("pass")
pwd.send_keys('GarX9FUrMuX9WXb')# Вводим пароль вместо YoUrPaSSwOrD
pwd.send_keys(Keys.ENTER)
print("регистрацию прошел успешно")
sleep(7)

driver.implicitly_wait(30)

with open("1.txt", "r", encoding="utf-8") as file:
    for line in file:
      URL = line.strip()
      print(URL)
      driver.get(URL)
      sleep(randint(3,5))
      e = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span") #находим поле для ввода текста
      act = ActionChains(driver)
      act.move_to_element(e).perform() # перемещаемся к нему, чтобы он стал видимым
      act = ActionChains(driver)
      act.click(e).perform() # делаем клик
      sleep(3)
      act = ActionChains(driver)
      act.send_keys(blogurl).perform() # вводим нашу ссылку
      sleep(3)
      # удаляем текст ссылки, оставляя только описание
      act = ActionChains(driver)
      act.send_keys("https://minus50.by/product/kompyuter-bu-hp-700g1-na-baze-intel-core-i5-4440s-1639392464-?utm_source=fb\n https://minus50.by/product/printer-bu-hp-laserje-2035-1639393042-?utm_source=fb").perform()
      sleep(3)
      e = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div")
      act = ActionChains(driver)
      act.move_to_element(e).perform()
      sleep(1)
      act = ActionChains(driver)
      act.click(e).perform()
      sleep(3)


#закрываем браузер
driver.close()