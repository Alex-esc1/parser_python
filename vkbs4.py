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
from bs4 import BeautifulSoup
import os

l = os.stat("product.txt").st_size
if l == 0:
    print('Файл пуст?')
    exit()
else:
    print('Файл не пуст!')

##Чтение ссылки из текстового файла (товар)
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

f = open('product.txt', 'r')
URLW = f.readline()
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
response = requests.get(URLW, headers = HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')
items = soup.findAll('body') 
comps = []
    
for item in items:
  NameS = get_text(item, 'h1', class_ = 'product__heading')
  priceS = get_text(item, 'div', class_ = 'product__price-cost')
  descriptionS = get_text(item, 'div', class_ = 'product__price-old-cost')
  imgSrc = get_image_src(item, attrs={"itemprop": 'image'})

print(f'{NameS} -> description: {priceS} -> Price: {descriptionS} -> img: {imgSrc} ')


##Чтение ссылки из текстового файла + UTM
a = '?utm_source=vk'
URLWS = URLW + a
print (URLWS)

##Чтение фото из текстового файла
imgSrc=imgSrc+' '
kolbs = len(imgSrc)
print ('Фото: '+imgSrc)

##Чтение цен из текстового файла
b = ('за единицу'.join(priceS.split('за единицу')[:-1]))
print (f'{b}\n{descriptionS}')

##Чтение скидки в % из текстового файла
c = ('BYN'.join(priceS.split('BYN')[:-1]))
d = ('BYN'.join(descriptionS.split('BYN')[:-1]))
n = (float(c) / float(d)) * 100
u = str(round(n,1))
p = u + '%'
print(p)

print("\nConnection success...")
## настройки мозила
options = Options()
options.headless = True
driver = webdriver.Firefox(executable_path=r"C:/test/geckodriver.exe")
driver.maximize_window()
 
#Вход в соцсеть
driver.get("http://vk.com")
sleep(5)
driver.find_element_by_id("index_email").send_keys('ЛОГИН')##вместо yourlogin вводин свой логин или номер телефона
sleep(2)
pwd = driver.find_element_by_id("index_pass")
pwd.send_keys('ПАРОЛЬ')# Вводим пароль вместо YoUrPaSSwOrD
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
      e = driver.find_element_by_id("post_field")
      e.clear()
      act = ActionChains(driver)
      act.move_to_element(e).perform()
      act = ActionChains(driver)
      act.click(e).perform()
      act.click(e).perform()
      sleep(3)
      act = ActionChains(driver)
      act.send_keys(imgSrc).perform()
      sleep(3)
      for _ in range(kolbs):
        act = ActionChains(driver)
        act.send_keys(Keys.BACKSPACE).perform()
      act.send_keys(f'{NameS}\n\nНовая цена: {b}\nCтарая цена: {descriptionS}\nCкидка: {p}\n{URLWS}').perform()
      sleep(3)
      driver.find_element_by_id("send_post").click()
      sleep(3)


#закрываем браузер
driver.close()
