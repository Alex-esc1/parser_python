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
from bs4 import BeautifulSoup
import os

## настройки мозила
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options,executable_path=r"C:/test/geckodriver.exe")
driver.maximize_window()
 
#Вход
driver.get("")#Вводим урл
sleep(2)
driver.find_element_by_id("email").send_keys('yourlogin') #вместо yourlogin вводин свой логин или номер телефона
sleep(2)
pwd = driver.find_element_by_id("password")
pwd.send_keys('YoUrPaSSwOrD') #Вводим пароль вместо YoUrPaSSwOrD
pwd.send_keys(Keys.ENTER)
print("регистрацию прошел успешно")
sleep(3)

def save():
    with open('1.csv', 'a', encoding="utf-8") as file:
        file.write(f'Сумма:{comp["title"]};Причина: {comp["price"]};статус: {comp["description"]};ссылка: {comp["img"]}\n')

def get_text(parent, name=None, index=0, attrs={}, recursive=True, text=None, **kwargs):
    items = parent.findAll(name, attrs, recursive, text, **kwargs)
    if index >= len(items):
        return ''
    item = items[index]
    try:
        return item.get_text(strip = True)
    except:
        return ''

def get_image_src(item, name=None, attrs={}, recursive=True, text=None, **kwargs):
    text = ''
    try:
        text = item.find(name, attrs, recursive, text, **kwargs).get('src')
    except:
        pass

    return text

def get_href(item, name=None, attrs={}, recursive=True, text=None, **kwargs):
    text = ''
    try:
        text = item.find(name, attrs, recursive, text, **kwargs).get('href')
    except:
        pass

    return text

def get_url(item, name=None, attrs={}, recursive=True, text=None, **kwargs):
    text = ''
    try:
        text = item.find(name, attrs, recursive, text, **kwargs).get('url')
    except:
        pass

    return text


with open("1.txt", "r", encoding="utf-8") as file:
    for line in file:
      URL = line.strip()
      print(URL)
      driver.get(URL)

      soup = BeautifulSoup(driver.page_source)
      items = soup.findAll('table', class_ = 'table table-bordered table-hover table-sm')
      #items = soup.findAll('body') # поиск по всей странице
      comps = []
      
      for item in items:
          NameS = get_text(item, 'td',  index=1)
          priceS =  get_text(item, 'td',  index=2)
          descriptionS =  get_text(item, 'td',  index=3)
          imgSrc = URL

          comps.append({
              'title': NameS,
              'price': priceS,
              'img': imgSrc,
              'description': descriptionS
          })

          global comp
          for comp in comps:
              print(f'{comp["title"]} -> description: {comp["description"]} -> Price: {comp["price"]} -> img: {comp["img"]}')
              save()

#закрываем браузер
driver.close()
