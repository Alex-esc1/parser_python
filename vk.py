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
driver.find_element_by_id("index_email").send_keys('+6576856678')##вместо yourlogin вводин свой логин или номер телефона
sleep(2)
pwd = driver.find_element_by_id("index_pass")
pwd.send_keys('56867867')# Вводим пароль вместо YoUrPaSSwOrD
pwd.send_keys(Keys.ENTER)
sleep(7)
 
driver.implicitly_wait(30)
 
#Переход на собственную страницу и постинг
driver.get("https://vk.com/minus50by") ## вводим свой ник или id вместо yourprofile
sleep(7)
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
e = driver.find_element_by_id("send_post")
act = ActionChains(driver)
act.move_to_element(e).perform()
act = ActionChains(driver)
act.click(e).perform()
sleep(3)
#нажимаем разместить
driver.find_element_by_css_selector('.button .c_button .s_button').click()

#закрываем браузер
driver.close()