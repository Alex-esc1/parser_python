import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
 
from time import sleep
    
##открываем текстовый файл, где находится ваша ссылка, которую вы хотите запостить. И копируем из неё 
f = open('blogurl.txt', 'r')
blogurl = f.readline()
f.close()
blogurl=blogurl+' ' #добавляем пробел, чтобы описание ссылки появилось
kolbs = len(blogurl) # определяем количество символов
print ('Blog url: '+blogurl)
 
##начало работы с selenium
 
chrome_Options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2} ## Отключение окон ФБ разрешения уведомлений
chrome_Options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_Options) # запускаем драйвер с указанными опциями
 
 
#Вход в соц сеть
driver.get("http://facebook.com") ## получаем главную страницу ФБ
sleep(2)
driver.find_element_by_id("email").send_keys('your@email.com') # вводим свой логин/почту пароль
sleep(2)
pwd = driver.find_element_by_id("pass")
pwd.send_keys('YourpAsSwOrD') #вводим свой пароль
pwd.send_keys(Keys.ENTER)
sleep(5)
 
driver.implicitly_wait(30) # указываем сколько мы даем времени драйверу на нахождение элементов
 
#переход на собственную страницу
driver.get("http://facebook.com/your page")
sleep(5)
e = driver.find_element_by_xpath("//*[@name='xhpc_message_text']") #находим поле для ввода текста
act = ActionChains(driver)
act.move_to_element(e).perform() # перемещаемся к нему, чтобы он стал видимым
act = ActionChains(driver)
act.click(e).perform() # делаем клик
sleep(3)
act = ActionChains(driver)
act.send_keys(blogurl).perform() # вводим нашу ссылку
sleep(3)
# удаляем текст ссылки, оставляя только описание
for _ in range(kolbs): 
	act = ActionChains(driver)
	act.send_keys(Keys.BACKSPACE).perform()
# находим кнопку отправить и компании по ней. Ждем отправки
e = driver.find_element_by_xpath("//button[@type='submit'][@value='1']/span")
act = ActionChains(driver)
act.move_to_element(e).perform()
sleep(1)
act = ActionChains(driver)
act.click(e).perform()
sleep(3)
 
 
#закрываем драйвер
driver.close()